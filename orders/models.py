from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pizza_Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza_Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza_Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Sub_Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Sub_Add_On(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Dinner_Platter_Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    size = models.ForeignKey(Sub_Size, on_delete=models.CASCADE, related_name="sub_by_size")
    price = models.FloatField()


class Pizza(models.Model):
    size = models.ForeignKey(Pizza_Size, on_delete=models.CASCADE, related_name="pizzas_by_size")
    regular_sicilian = models.ForeignKey(Pizza_Type, on_delete=models.CASCADE, related_name="pizzas_by_type")
    toppings = models.ManyToManyField(Pizza_Topping, blank=True, related_name="pizza_by_toppings")

    def __str__(self):
        return f"{self.size} {self.regular_sicilian} with {self.toppings}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class Platter(models.Model):
    name = models.CharField(max_length=64)
    size = models.ForeignKey(Dinner_Platter_Size, on_delete=models.CASCADE, related_name="platters_by_size")
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    order_name = models.CharField(max_length=128)
    order_item = models.CharField(max_length=128)
    price = models.FloatField()

class Confirmed_Order(models.Model):
    order_name = models.CharField(max_length=128)
    final_order = models.CharField(max_length=999)
    total = models.FloatField()



