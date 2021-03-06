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
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('index/', views.index, name='index'),
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name="item_detail"),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name="add-to-cart"),
    # path('remove-from-cart/<int:pk>/', views.remove_from_cart, name="remove-from-cart"),
    path('order-summary/', views.OrderSummary, name="order-summary"),
    path('add_to_cart_single_item/<int:pk>/', views.add_to_cart_single_item, name="add_to_cart_single_item"),
    path('remove_from_cart_single_item/<int:pk>/', views.remove_from_cart_single_item, name="remove_from_cart_single_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('platnosc/',views.platnosc, name="platnosc"),
    path('complete_paymant', views.complete_paymant, name='complete_paymant'),
    path('add_cupon/', views.add_cupon, name='add_cupon'),
    path('request_refund/', views.request_refund, name='request_refund'),
    path('podsumowanie/', views.podsumowanie, name='podsumowanie'),
    path('cupon_check/', views.cupon_check, name='cupon_check'),
    path('delete_cupon/', views.delete_cupon, name='delete_cupon'),
    # path('testing/', views.testing, name='testing'),
    path('delete_cupon_order/', views.delete_cupon_order, name='delete_cupon_order'),
    path('rozmiar/<int:pk>/', views.rozmiar, name='rozmiar'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    path('ocena_produktu/<int:pk>/', views.ocena_produktu, name='ocena_produktu'),
    path('edit_ocena_produktu/<int:pk>/<int:id>/', views.edit_ocena_produktu, name='edit_ocena_produktu'),
    path('zamowienia', views.zamowienia, name="zamowienia"),
    path('zamowienia/<int:pk>/', views.zamowienia_detail, name='zamowienia_detail'),
    path('item/<int:pk>/comments/', views.item_detail_comments, name='item_detail_comments'),
    path('delete_comment/<int:pk>/<int:id>/', views.delete_comment, name='delete_comment'),
]


# REST API paths

urlpatterns += [
    path('itemview/', views.ItemView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token'), # przy pomocy tego mozemy stworzyc token dostepu
]