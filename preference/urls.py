from django.urls import path
from .views import pizzaList , pizzaDetail , pizzaToppingList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("pizza/" , pizzaList.as_view()),
    path("pizza/<int:pk>" , pizzaDetail.as_view()),
    path("pizzaToppings/" , pizzaToppingList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)