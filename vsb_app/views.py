from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomepageView(TemplateView):
    template_name = "vsb_app/index.html"


class ShopView(TemplateView):
    template_name = "vsb_app/shop.html"


# class ShopView(TemplateView):
#     template_name = "vsb_app/my_transaction.html"
#
#
# class ShopView(TemplateView):
#     template_name = "vsb_app/sell_my_car.html"
#
#
# class ShopView(TemplateView):
#     template_name = "vsb_app/sign_in.html"
#
#
# class ShopView(TemplateView):
#     template_name = "vsb_app/sign_up.html"
#
#
# class ShopView(TemplateView):
#     template_name = "vsb_app/single_product.html"
