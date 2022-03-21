from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from .forms import AutomobileForm, ImmaginiAutomobiliForm
from django.forms import modelformset_factory
from .models import ImmaginiAutomobili, Automobile


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


class SingleProductView(TemplateView):
    template_name = "vsb_app/single_product.html"
