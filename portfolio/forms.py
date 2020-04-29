from django import forms
from .models import Cupon, OrderItem, ItemWariant, ItemWariant2
from django.forms import ModelForm

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    second_name = forms.CharField(max_length=100)
    street_address = forms.CharField(max_length=150)
    kod_pocztowy = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Podaj kod pocztowy bez -'}))
    miejscowosc = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = forms.IntegerField()

class CuponForm(forms.Form):
    code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Jeśli posiadasz kupon, wpisz go tutaj'}))



class RefundForm(forms.Form):
    ref_code = forms.CharField(max_length=30)
    wiadomosc = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

class RozmiarForm(forms.Form):
    
    rozmiar = forms.ModelChoiceField(empty_label="Wybierz swój rozmiar", queryset=ItemWariant.objects.all())
    # kolor = forms.ModelChoiceField(queryset=ItemWariant2.objects.all())
    
        

