from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from .forms import AutomobileForm, ImmaginiAutomobiliForm
from django.forms import modelformset_factory
from .models import ImmaginiAutomobili, Automobile, Concessionaria, CustomUser


# Create your views here.
class HomepageView(TemplateView):
    template_name = "vsb_app/index.html"


class ShopView(ListView):
    template_name = "vsb_app/shop.html"
    model = Automobile


class MyTransactionRegistrationsView(TemplateView):
    template_name = "vsb_app/my_transaction_registrations.html"


class MyTransactionSalesView(TemplateView):
    template_name = "vsb_app/my_transaction_sales.html"


class SellMyCarView(TemplateView):
    template_name = "vsb_app/sell_my_car.html"
    success_url = "/sell_my_car/"

    def post(self, request, *args, **kwargs):
        immagine_form = ImmaginiAutomobiliForm(request.POST, request.FILES)
        automobile_form = AutomobileForm(request.POST)
        context = {}
        if automobile_form.is_valid():
            automobile = automobile_form.save()

            images = request.FILES.getlist("immagine")
            print(images)
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


class SignInView(TemplateView):
    template_name = "vsb_app/sign_in.html"


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
            user = CustomUser(email=email, telefono=telefono)
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
        return render(request, 'vsb_app/sign_in.html', context)


class SingleProductView(TemplateView):
    template_name = "vsb_app/single_product.html"
