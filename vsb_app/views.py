from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomepageView(TemplateView):
    template_name = "vsb_app/index.html"


class ShopView(TemplateView):
    template_name = "vsb_app/shop.html"


class MyTransactionView(TemplateView):
    template_name = "vsb_app/my_transaction.html"


class SellMyCarView(TemplateView):
    template_name = "vsb_app/sell_my_car.html"


class SignInView(TemplateView):
    template_name = "vsb_app/sign_in.html"


class SignUpView(TemplateView):
    template_name = "vsb_app/sign_up.html"


class SingleProductView(TemplateView):
    template_name = "vsb_app/single_product.html"
