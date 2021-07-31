from django.db import models
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField


# Create your models here.
PIZZA_TYPE = (
    ('Regular' , 'Regular'),
    ('Square' , 'Square'),
)
PIZZA_SIZE = (
    ('Small' , 'Small'),
    ('Medium' , 'Medium'),
    ('Large' , 'Large'),
)
PIZZA_TOPPINGS = (
    ('Corn' , 'Corn'),
    ('Onions' , 'Onions'),
    ('Jalapenos' , 'Jalapenos'),
    ('Tomato' , 'Tomato'),
    ('Bellpepper' , 'Bellpepper'),
    ('Olives' , 'Olives'),
    ('Extra Cheese' , 'Cheese'),
    )

class Toppings(models.Model):
    topping = MultiSelectField(choices=PIZZA_TOPPINGS , max_length=64)

    def __str__(self):
        return(str(self.topping))


class pizzaModel(models.Model):
    type = models.CharField(choices = PIZZA_TYPE , max_length= 20)
    size = models.CharField(choices = PIZZA_SIZE , max_length= 20)
    topping =models.ManyToManyField(Toppings, blank=True)


    def __str__(self):
        return str(self.type) + '--' +str(self.size) + '-- Topping Number: ' + str(self.topping)