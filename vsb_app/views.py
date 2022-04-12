from datetime import datetime

from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from .forms import AutomobileForm, ImmaginiAutomobiliForm, LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.db.models import Q
from .models import ImmaginiAutomobili, Automobile, Concessionaria, CustomUser, Ordine, Marca


# Create your views here.
class HomepageView(TemplateView):
    template_name = "vsb_app/index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["shop_cars_list"] = Automobile.objects.filter(is_purchased=False)
        return render(request, self.template_name, context)


class ShopView(TemplateView):
    template_name = "vsb_app/shop.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        context = {}
        context["object_list"] = Automobile.objects.filter(is_purchased=False)
        context["marche"] = Marca.objects.all()
        context["stati"] = Automobile.STATE_CHOICES
        context["neopatentato"] = Automobile.NEW_DRIVER_CHOICES
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = {}
        marca_value = self.request.POST.get('marca')
        if marca_value:
            marca_value = Marca.objects.get(nome=marca_value)
        filter_dict = {
            "stato": self.request.POST.get('stato'),
            "prezzo__lte": self.request.POST.get('prezzo_max'),
            "marca": marca_value,
            "modello__icontains": self.request.POST.get('modello'),
            "km_percorsi": self.request.POST.get('kilometraggio'),
            "neopatentato": self.request.POST.get('neopatentato'),
            "concessionaria__citta": self.request.POST.get('citta'),
            "anno_immatricolazione": self.request.POST.get('anno')
        }
        filter_dict = {key: value for key, value in filter_dict.items() if value}
        # context["object_list"] = Automobile.objects.all()
        context["marche"] = Marca.objects.all()
        context["stati"] = Automobile.STATE_CHOICES
        context["neopatentato"] = Automobile.NEW_DRIVER_CHOICES
        context["object_list"] = Automobile.objects.filter(**filter_dict)
        # context["object_list"] = Automobile.objects.filter(
        #     Q(stato=filter_dict.get("stato")) |
        #     Q(prezzo__lte=filter_dict.get("prezzo")) |
        #     Q(modello=filter_dict.get("modello")) |
        #     Q(km_percorsi=filter_dict.get("km_percorsi")) |
        #     Q(neopatentato=filter_dict.get("neopatentato")) |
        #     Q(citta__concessionaria=filter_dict.get("citta")) |
        #     Q(anno_immatricolazione=filter_dict.get("anno_immatricolazione"))
        # )
        return render(request, self.template_name, context)


class MyTransactionsView(LoginRequiredMixin, TemplateView):
    template_name = "vsb_app/my_transactions.html"

    def get(self, request, *args, **kwargs):
        context = {}
        if request.user.is_client:
            context["ordini_cliente"] = Ordine.objects.filter(acquirente=request.user).all()
            return render(request, self.template_name, context)

        context["ordini_concessionaria"] = Ordine.objects.filter(
            automobile__concessionaria=request.user.concessionaria
        ).all()

        context["automobile_registrate"] = Automobile.objects.filter(
            concessionaria=request.user.concessionaria,
            is_purchased=False
        ).all()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        automobile_pk = self.request.POST["delete_car"]
        automobile_selezionata = Automobile.objects.get(pk=automobile_pk)
        automobile_selezionata.delete()
        return redirect('vsb_app:my_transactions')


class SellMyCarView(LoginRequiredMixin, TemplateView):
    template_name = "vsb_app/sell_my_car.html"
    success_url = "/sell_my_car/"

    def post(self, request, *args, **kwargs):
        immagine_form = ImmaginiAutomobiliForm(request.POST, request.FILES)
        automobile_form = AutomobileForm(request.POST)
        context = {}
        if automobile_form.is_valid():
            automobile = automobile_form.save(commit=False)
            automobile.concessionaria = request.user.concessionaria
            automobile.save()

            images = request.FILES.getlist("immagine")
            for form_immagine in images:
                photo = ImmaginiAutomobili(automobile=automobile, immagine=form_immagine)
                photo.save()
            context["message"] = "Registrazione avvenuta correttamente!"
            immagine_form = ImmaginiAutomobiliForm()
            automobile_form = AutomobileForm()

        context["automobile_form"] = automobile_form
        context["image_form"] = immagine_form
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):

        immagine_form = ImmaginiAutomobiliForm()
        automobile_form = AutomobileForm()

        return render(request, self.template_name, {'automobile_form': automobile_form, 'image_form': immagine_form})


class SignInView(LoginView):
    template_name = "vsb_app/sign_in.html"
    authentication_form = LoginForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "vsb_app/profile.html"

    def post(self, request, *args, **kwargs):
        context = {}
        user = request.user
        type_request = self.request.POST["type_request"]
        if type_request == "delete":
            user.delete()
            return redirect('vsb_app:sign_up')

        user.telefono = self.request.POST.get('telefono')
        user.email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        if password:
            user.set_password(password)
        if user.is_client:
            user.first_name = self.request.POST.get('nome')
            user.last_name = self.request.POST.get('cognome')
        else:
            user.concessionaria.ragione_sociale = self.request.POST.get('ragione_sociale')
            user.concessionaria.partita_IVA = self.request.POST.get('partita_iva')
            user.concessionaria.indirizzo = self.request.POST.get('indirizzo')
            user.concessionaria.citta = self.request.POST.get('citta')

        try:
            user.save()
        except (ValueError, ValidationError):
            context['error'] = 'Aggiornamento non avvenuto!'

        if "error" in context:
            return render(request, self.template_name, context)
        return render(request, self.template_name, context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('vsb_app:sign_in')


class SignUpView(TemplateView):
    template_name = "vsb_app/sign_up.html"

    def post(self, request, *args, **kwargs):
        context = {"error": {}}
        ragione_sociale = self.request.POST.get('ragione_sociale')
        partita_IVA = self.request.POST.get('partita_iva')
        indirizzo = self.request.POST.get('indirizzo')
        citta = self.request.POST.get('citta')
        nome = self.request.POST.get('nome')
        cognome = self.request.POST.get('cognome')
        telefono = self.request.POST.get('telefono')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        conferma_password = self.request.POST.get('password2')

        if password != conferma_password:
            context['error']['password'] = 'Le password non corrispondono!'
            return render(request, self.template_name, context)

        if nome is not None and cognome is not None:
            user = CustomUser(first_name=nome, last_name=cognome, email=email, telefono=telefono)
            user.set_password(password)
            try:
                user.save()
            except (ValueError, ValidationError):
                context['error']['save'] = 'Registrazione non avvenuta!'
        else:
            user = CustomUser(email=email, telefono=telefono, is_client=False)
            user.set_password(password)
            try:
                user.save()
            except (ValueError, ValidationError):
                context['error']['save'] = 'Registrazione non avvenuta!'

            concessionaria = Concessionaria(user=user, ragione_sociale=ragione_sociale, partita_IVA=partita_IVA, indirizzo=indirizzo, citta=citta)
            try:
                concessionaria.save()
            except (ValueError, ValidationError):
                context['error']['save'] = 'Registrazione non avvenuta!'

        if context["error"]:
            return render(request, self.template_name, context)
        return redirect('vsb_app:sign_in')


class SingleProductView(LoginRequiredMixin, DetailView):
    template_name = "vsb_app/single_product.html"
    model = Automobile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        automobile_selezionata = self.get_object()
        automobili_correlate = Automobile.objects.exclude(pk=automobile_selezionata.pk)
        context["automobili_correlate"] = automobili_correlate
        return context

    def post(self, request, *args, **kwargs):
        automobile_selezionata = self.get_object()
        automobile_selezionata.is_purchased = True
        automobile_selezionata.save()
        ordine = Ordine(automobile=automobile_selezionata, acquirente=request.user)
        ordine.save()
        return redirect('vsb_app:my_transactions')
