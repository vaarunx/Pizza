from django.shortcuts import render
from .models import pizzaModel , Toppings
from .serializers import pizzaSerializers , pizzaToppingSerializers
from rest_framework import generics

# Create your views here.

class pizzaList(generics.ListCreateAPIView):
    queryset = pizzaModel.objects.all()
    serializer_class = pizzaSerializers

class pizzaToppingList(generics.ListCreateAPIView):
    queryset = Toppings.objects.all()
    serializer_class = pizzaToppingSerializers

class pizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = pizzaModel.objects.all()
    serializer_class = pizzaSerializers    
