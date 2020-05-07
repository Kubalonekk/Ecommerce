from django import template
from portfolio.models import Order, OrderItem


register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
            qs_1 = OrderItem.objects.filter(user=user, ordered=False)
            objects = 0
            for q in qs_1:
                objects += q.quantity
            return objects
    return 0




@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)