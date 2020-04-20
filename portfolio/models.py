from django.db import models
from django.conf import settings


rozmiarowka = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
]

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    img = models.ImageField(null=True)
    description = models.TextField(null=True)
    dostepna_ilosc_s = models.IntegerField(null=True, default=0, blank=True)
    dostepna_ilosc_m = models.IntegerField(null=True, default=0, blank=True)
    dostepna_ilosc_l = models.IntegerField(null=True, default=0, blank=True)
    dostepna_ilosc_xl = models.IntegerField(null=True, default=0, blank=True)
    dostepna_ilosc_xxl = models.IntegerField(null=True, default=0, blank=True)
  

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    rozmiar = models.CharField(max_length=3, choices = rozmiarowka, null=True)

    def __str__(self):
        return  f"{self.quantity} of {self.item.title}"  # przy pomocy f mozemy łączyc i dodawac wyniki

    def get_total_item_price(self):
        return self.quantity * self.item.price    # ilosc mnozymy przez cene ( jest to cena calosci za dany produkt, czyli jak mam rower kupujemy dwie sztuki to policzy nam rower * 2 a nie calosc zamowienia)

    def get_final_price(self):
        return self.get_total_item_price() #pobriera cala cene jednego produktu(cala cena jednego produktu to ilosc razy cena produktu)



class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=30, null=True)
    items=models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(null=True, auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, blank=True, null=True)
    cupon = models.ForeignKey('PrimaryCupon', on_delete=models.SET_NULL, blank=True, null=True)
    w_trakcie_dostarczania = models.BooleanField(default=False)
    odebrana = models.BooleanField(default=False)
    zadanie_zwrotu = models.BooleanField(default=False)
    zwrot = models.BooleanField(default=False)
    



    def __str__(self):
        return self.user.username

    def get_total(self):
        # ustawiamy zmienna total na zero pozniej robimy petle w polu many to many field aby dodac wszystko do siebie
        total = 0
        for order_item in self.items.all():  #.all poniewaz robimy petle w polu manytomany
            total += order_item.get_final_price()
        try:
            total -= self.cupon.cupon_fk.amount
            return total
        except:
                return total

        
     


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True ,on_delete=models.SET_NULL,)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=150)
    kod_pocztowy = models.CharField(max_length=100)
    miejscowosc = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.IntegerField()

    def __str__(self):
        return f"Zamówienie użytkownika o nicku: {self.user.username}. Imie:{self.name}  Nazwisko:{self.second_name }" 


class PrimaryCupon(models.Model):
    
    cupon_fk = models.ForeignKey("Cupon", on_delete=models.CASCADE)

    def __str__(self):
        return self.cupon_fk.code
    
class Cupon(models.Model):
    code = models.CharField(max_length=15, null=True, blank=True)
    amount = models.FloatField(default=0)
    cena = models.FloatField(default=0)

    def __str__(self):
        return self.code

class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    powod = models.TextField()
    przyjety = models.BooleanField(default=False)
    email = models.EmailField(null=True)

    def __str__(self):
        return f" ID: {self.pk} {self.order}"
