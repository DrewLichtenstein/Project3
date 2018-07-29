from django.contrib import admin

# Register your models here.

from .models import Pizza_Topping, Pizza_Size, Pizza_Type, Sub_Size, Sub_Add_On, Dinner_Platter_Size, Sub, Pizza, Pasta, Salad, Platter, Order, Confirmed_Order

admin.site.register(Pizza_Topping)
admin.site.register(Pizza_Size)
admin.site.register(Pizza_Type)
admin.site.register(Sub_Size)
admin.site.register(Sub_Add_On)
admin.site.register(Dinner_Platter_Size)
admin.site.register(Sub)
admin.site.register(Pizza)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(Order)
admin.site.register(Confirmed_Order)