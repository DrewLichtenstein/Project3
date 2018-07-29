from django.contrib import admin

# Register your models here.

from .models import Pizza_Topping, Pizza_Size, Pizza_Type, Dinner_Platter_Size, Pasta, Salad, Platter, Order, Confirmed_Order, Sub_Sandwich

admin.site.register(Pizza_Topping)
admin.site.register(Pizza_Size)
admin.site.register(Pizza_Type)
admin.site.register(Dinner_Platter_Size)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(Order)
admin.site.register(Confirmed_Order)
admin.site.register(Sub_Sandwich)
