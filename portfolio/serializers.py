from rest_framework import serializers
from  .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'title', 'price', 'size', 'ilosc', 'img','description',
        )
