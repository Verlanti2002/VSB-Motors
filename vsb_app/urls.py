"""VSB_Motors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import HomepageView, ShopView, SellMyCarView, SignInView, SignUpView, SingleProductView, \
    MyTransactionSalesView, MyTransactionRegistrationsView

app_name = "vsb_app"

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('shop/', ShopView.as_view(), name="shop"),
    path('sell_my_car/', SellMyCarView.as_view(), name="sell_my_car"),
    path('my_transaction_sales/', MyTransactionSalesView.as_view(), name="my_transaction_sales"),
    path('my_transaction_registrations', MyTransactionRegistrationsView.as_view(), name="my_transaction_registrations"),
    path('sign_in/', SignInView.as_view(), name="sign_in"),
    path('sign_up/', SignUpView.as_view(), name="sign_up"),
    path('single_product/', SingleProductView.as_view(), name="single_product")
]
