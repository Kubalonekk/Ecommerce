from django.contrib import admin

from .models import Item, OrderItem, Order, Address, Cupon, Refund

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(zadanie_zwrotu=False, zwrot=True) # w nawiasach podajemy co ma zrobic dana funkcja
make_refund_accepted.short_description = 'Zaaktualizuj zamowienia jako przyjete do zwrotu' # okreslnie pod jaka nazwa bedzie wykonowala sie funkcja wyzej


class OrderAdmin(admin.ModelAdmin):  # w modelu Order bedziemy wskazywac co ma sie wyswietlac w panelu admina
    list_display = [                        # wskazujemy pola ktore maja sie wyswietlic
        'user',
        'ordered',
        'w_trakcie_dostarczania',
        'odebrana',
        'zadanie_zwrotu',
        'zwrot',
        'address',
        ]  
    list_display_links = [
        'user',
        'address',
    ]
    list_filter = [     #ustawienei filtrów w panelu admina
        'ordered',
        'w_trakcie_dostarczania',
        'odebrana',
        'zadanie_zwrotu',
        'zwrot'
        ]  
    search_fields = [
        'user__username',
        'ref_code',


    ]

    actions = [make_refund_accepted] # dodanie to tej listy z akcjami

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['__str__','user','ordered',]

admin.site.register(Item)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address)
admin.site.register(Cupon)
admin.site.register(Refund)