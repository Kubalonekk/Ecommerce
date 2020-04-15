"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name="item_detail"),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name="remove-from-cart"),
    path('order-summary/', views.OrderSummary, name="order-summary"),
    path('add_to_cart_single_item/<int:pk>/', views.add_to_cart_single_item, name="add_to_cart_single_item"),
    path('remove_from_cart_single_item/<int:pk>/', views.remove_from_cart_single_item, name="remove_from_cart_single_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('platnosc/',views.platnosc, name="platnosc"),
    path('complete_paymant', views.complete_paymant, name='complete_paymant'),
    path('add_cupon/', views.add_cupon, name='add_cupon'),
    path('request_refund/', views.request_refund, name='request_refund'),
    path('podsumowanie/', views.podsumowanie, name='podsumowanie'),
]