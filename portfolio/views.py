from django.shortcuts import render
from .models import Item, OrderItem, Order, Address, Cupon, Refund
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .forms import CheckoutForm, CuponForm, RefundForm
import random
import string


def create_ref_code():
    #tworzy losowy kod znaków
    return ''.join(random.choices(string.ascii_lowercase + string.digits,k=30))


def item_list(request):

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'portfolio/item_list.html', context)



def item_detail(request, pk):

    detail = Item.objects.get(id=pk)

    context = {
        'detail': detail,
    }

    return render(request, 'portfolio/item_detail.html', context)



def OrderSummary(request):
    try:
        total_price = Order.objects.get(user=request.user, ordered=False)
    except Order.DoesNotExist:
        messages.info(request,"Brak zamówienia")
        return redirect("/")

    try:
        orders = OrderItem.objects.filter(user=request.user, ordered=False)
        context = {
        'orders':orders,
        'total_price':total_price,
        'cuponform': CuponForm(),
        }

        return render(request, 'portfolio/order_summary.html', context)
    except ObjectDoesNotExist:
        messages.error(request, "Nie masz aktywnego zamowienia")
        return redirect("/")





@login_required(login_url='/accounts/login/')
def add_to_cart(request, pk):
    item = get_object_or_404(Item, id=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    ) # tworzymy OrderItem przypisujemy item pobrany wyzej, uzytkownika ktory jest wlasnie zalogowany a takze ustawiamy Ordered false
    order_qs = Order.objects.filter(user=request.user, ordered=False) # sprawdzamy czy zamowienie juz istnieje.
    if order_qs.exists(): # jesli istnieje do przypisujemy je do zmiennej order
        order = order_qs[0] # pobranie pierwszego wyinku czyli zamowienia
        if order.items.filter(item__id=item.id).exists(): # sprawdzenie czy w  OrderItem  jest juz przedmiot ktory bedziemy dodawawc ponownie po to aby po wcisnieciu przycisu dodaj do koszyka, zwiekszyla sie ilosc
            order_item.quantity += 1 # dodanie kolejnego zamowienia
            order_item.save()
            messages.info(request,"Ilosc przedmiotow zostala zwiekszona")
        else:
            order.items.add(order_item)
            messages.info(request,"Przedmiot zostal dodany do koszyka")
    else: # jesli nie istnieje to tworzymy nowe zamowienie
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"Przedmiot zostal dodany do koszyka")
    return redirect('item_detail', pk)


@login_required(login_url='/accounts/login/')
def remove_from_cart(request, pk):
    item = get_object_or_404(Item, id=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False) # sprawdzamy czy zamowienie juz istnieje.
    if order_qs.exists(): # sprawdzamy czy zamowienie juz istnieje.
        order = order_qs[0] # pobranie pierwszego wyinku czyli zamowienia
        if order.items.filter(item__id=item.id).exists(): # sprawdzenie czy w koszyku mam przedmioty do usuniecia
            order_item = OrderItem.objects.filter(  # 
                item=item,
                user=request.user,
                ordered=False,
            )[0] # zero do pobranie tego obiektu
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request,"Przedmiot zostal usuniety z koszyka")
        else:
            messages.info(request, "Brak przedmiotów do usuniecia")
            # brak przedmiotow do usuniecia
            return redirect('item_detail', pk)
    else:
        messages.info(request, "Nie masz aktywnego zamowienia")
        # brak zamowien w ktorym mozna usunac przedmioty
        return redirect('item_detail', pk)
    return redirect('item_detail', pk)





@login_required
def add_to_cart_single_item(request, pk):
    # Ta sama funkcja co ta pierwsza tylko przekierwuje w inne miejsce
    item = get_object_or_404(Item, id=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    ) # tworzymy OrderItem przypisujemy item pobrany wyzej, uzytkownika ktory jest wlasnie zalogowany a takze ustawiamy Ordered false
    order_qs = Order.objects.filter(user=request.user, ordered=False) # sprawdzamy czy zamowienie juz istnieje.
    if order_qs.exists(): # jesli istnieje do przypisujemy je do zmiennej order
        order = order_qs[0] # pobranie pierwszego wyinku czyli zamowienia
        if order.items.filter(item__id=item.id).exists(): # sprawdzenie czy w  OrderItem  jest juz przedmiot ktory bedziemy dodawawc ponownie po to aby po wcisnieciu przycisu dodaj do koszyka, zwiekszyla sie ilosc
            order_item.quantity += 1 # zwiekszenie ilosci
            order_item.save()
            messages.info(request,"Ilosc przedmiotow zostala zwiekszona")
        else:
            order.items.add(order_item)
            messages.info(request,"Przedmiot zostal dodany do koszyka")
    else: # jesli nie istnieje to tworzymy nowe zamowienie
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"Przedmiot zostal dodany do koszyka")
    return redirect('order-summary')



@login_required
def remove_from_cart_single_item(request, pk):
    item = get_object_or_404(Item, id=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False) # sprawdzamy czy zamowienie juz istnieje.
    if order_qs.exists(): # sprawdzamy czy zamowienie juz istnieje.
        order = order_qs[0] # pobranie pierwszego wyinku czyli zamowienia
        if order.items.filter(item__id=item.id).exists(): # sprawdzenie czy w koszyku mam przedmioty do usuniecia
            order_item = OrderItem.objects.filter(  # 
                item=item,
                user=request.user,
                ordered=False,
            )[0] # zero do pobranie tego obiektu
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request,"Przedmiot zostal usuniety z koszyka")
        else:
            messages.info(request, "Brak przedmiotów do usuniecia")
            # brak przedmiotow do usuniecia
            return redirect('item_detail', pk)
    else:
        messages.info(request, "Nie masz aktywnego zamowienia")
        # brak zamowien w ktorym mozna usunac przedmioty
        return redirect('item_detail', pk)
    return redirect('order-summary')


def checkout(request):
 
    try:
        total_price = Order.objects.get(user=request.user, ordered=False)
    except Order.DoesNotExist:
        messages.info(request,"Brak zamówienia")
        return redirect("/")

    try:
        orders = OrderItem.objects.filter(user=request.user, ordered=False)
    except ObjectDoesNotExist:
        messages.error(request, "Nie masz aktywnego zamowienia")
        return redirect("/")
    
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            second_name = form.cleaned_data.get('second_name')
            street_address = form.cleaned_data.get('street_address')
            kod_pocztowy = form.cleaned_data.get('kod_pocztowy')
            miejscowosc = form.cleaned_data.get('miejscowosc')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            try:
                qs = Address.objects.get(user=request.user, 
                name=name,
                second_name=second_name,
                street_address=street_address,
                kod_pocztowy=kod_pocztowy,
                miejscowosc=miejscowosc,
                email=email,
                phone_number=phone_number,
                )
            
                total_price.address = qs
                total_price.save()
                return redirect('platnosc')
            except:
                address = Address.objects.create(
                user=request.user, 
                name=name,
                second_name=second_name,
                street_address=street_address,
                kod_pocztowy=kod_pocztowy,
                miejscowosc=miejscowosc,
                email=email,
                phone_number=phone_number,
                )
                address.save()
                total_price.address = address # total_price to zmienna do ktorej pobralismy Order na samym poczatku widoku . teraz przypisujemy do foreginkey to co stworzylismy wyzej
                total_price.save()
                return redirect('platnosc')
            
    else:
        form = CheckoutForm()     
    context = {
        'form': form,
        'total_price':total_price,
        'orders': orders,
    }    
    return render(request, 'portfolio/checkout.html', context)


def platnosc(request):

    total_price = Order.objects.get(user=request.user, ordered=False)
    orders = OrderItem.objects.filter(user=request.user, ordered=False)

    context = {
        'orders':orders,
        'total_price':total_price,
        }

    return render(request, 'portfolio/platnosc.html', context)

def complete_paymant(request):
    qs = Order.objects.get(user=request.user, ordered=False)
    qs1 = OrderItem.objects.filter(user=request.user, ordered=False)
    qs.ref_code = create_ref_code() # w tym miejscu wykorzystujemy funkcje create ref code ktora jest napisana wyzej do przypisania losowych liczb
    qs.ordered = True
    qs.save()
    for q in qs1:
        q.ordered = True
        q.save()
        
    
    return redirect('item_list')


def get_cupon(request, code):
    try:
        cupon = Cupon.objects.get(code=code) # jesli pobierze to znaczy ze kod wpisany przez uzytkownika w formularzu jest taki sam jak ten ktory my utworzlismy za pomoca admina
        return cupon
    except ObjectDoesNotExist:
        messages.info(request,"Ten kupon nie działa")
        return redirect('order-summary')



# trzeba ogarnac dlaczego nie moge ustawic dynamicznie wartosci od jakiegj mozna dodac
#  do przerobenia jest szablon z checkout, poniewaz tam mozna zmieniac ilosc przedmiotów i w taki prosty sposób mozna ominąć wartosc zamowienia od jakiego bedzie dodawany kupon
def add_cupon(request):
    if request.method == 'POST':
        form = CuponForm(request.POST or None)
        if form.is_valid():
                try:
                    order = Order.objects.get(user= request.user, ordered=False)
                    if order.cupon:
                        messages.warning(request,"W koszyku moze byc aktywny tylko jeden kupon")
                        return redirect ('order-summary')
                    code = form.cleaned_data.get('code') # 'code' to pole które uzupelnia uzytkownik w formularz
                    try: 
                        if order.get_total() >= 200:
                            order.cupon = get_cupon(request, code) # tutaj do Order.cupon dodajemy funkcje ktora ma prametr code czyli to co wpisal uzytkownik i przechodzimy do funkcji get cupon
                            messages.success(request,"Kupon dodany prawidłowo")
                            order.save()
                            return redirect ('order-summary')
                        else:
                            messages.warning(request,"Aby dodać kupon twój koszyk musi mieć wartość powyżej 200 zł")
                            return redirect('order-summary')
                    except:
                        return redirect('order-summary')
                except ObjectDoesNotExist:
                    messages.info(request,"Brak zamówienia")
                    return redirect('order-summary')
    return None


@login_required(login_url='/accounts/login/')
def request_refund(request):

    if request.method == "POST":
         form = RefundForm(request.POST or None)
         if form.is_valid():
            ref_code  = form.cleaned_data.get('ref_code')
            powod = form.cleaned_data.get('wiadomosc')
            email = form.cleaned_data.get('email')
            try:
                order = Order.objects.get(ref_code=ref_code)
                order.zadanie_zwrotu = True
                order.save()

                refund = Refund()  # stowrzenie modelu Refund
                refund.order = order
                refund.powod = powod
                refund.email  = email
                refund.save()

                messages.info(request,"Poprawnie wyslano wiadomosc")
                return redirect('request_refund')
            
                
            except ObjectDoesNotExist:
                 messages.info(request,"Nie ma takiego zamowienia")
                 return redirect('request_refund')
    else:
        form = RefundForm()
               
    context = {
                'form': form,
            }

    return render(request, 'portfolio/refund.html', context)    

    





