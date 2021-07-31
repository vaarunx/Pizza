from django.db.models import fields
from preference.models import pizzaModel , Toppings
from rest_framework import serializers
from .models import pizzaModel

class pizzaSerializers(serializers.ModelSerializer):
    class Meta:
        model = pizzaModel
        fields = "__all__"


class pizzaToppingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Toppings
        fields = "__all__"