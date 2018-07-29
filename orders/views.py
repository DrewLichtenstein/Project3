from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Pizza_Topping, Pizza_Size, Pizza_Type, Dinner_Platter_Size, Pasta, Salad, Platter, Order, Confirmed_Order, Sub_Sandwich

import random

# index default view is login page, with redirect to the menu if they are already logged-in
def index(request):
    if not request.user.is_authenticated:
        return render(request, "signup.html", {"message": None})
    context = {
        "user": request.user
    }
    return HttpResponseRedirect(reverse("menu"))

#registration page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#login function
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

def login_redirect(request):
    return render(request, "login.html")


#logout function
def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

#menu function -- requires user to be logged-in
def menu(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user
    }
    context = {
        "toppings": Pizza_Topping.objects.all(),
        "sizes": Pizza_Size.objects.all(),
        "types": Pizza_Type.objects.all(),
        "your_orders": Order.objects.filter(order_name=request.user).all(),
        "salads": Salad.objects.all(),
        "platters": Platter.objects.all(),
        "pastas": Pasta.objects.all()

    }
    # menu items are rendered as drop down selections
    return render(request, "menu.html", context)

# on selection, add salad to the Order Class
def add_salad_order (request):
    order_name = request.user
    order_item = request.POST["salad"]
    price = Salad.objects.get(name=order_item).price
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))

# on selection, add platter to the Order Class
def add_platter_order (request):
    order_name = request.user
    order_item = request.POST["platter"]
    price = Platter.objects.get(name=order_item).price
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))

# on selection, add pasta to the Order Class
def add_pasta_order (request):
    order_name = request.user
    order_item = request.POST["pasta"]
    price = Pasta.objects.get(name=order_item).price
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))

# allows user to build a pizza of size, type, and up to three toppings
def add_pizza_order (request):
    order_name = request.user
    pizza_size = request.POST["size"]
    pizza_type = request.POST["type"]
    toppings = request.POST.getlist("toppings")
    if len(toppings) > 3:
        # My main issue here is I couldn't figure out how to send a message along with HttpResponse Redirect
        # There's documentation here (https://docs.djangoproject.com/en/2.0/ref/contrib/messages/), but I couldn't grok here...
        return HttpResponseRedirect(reverse("menu"))
    toppings_string = str(toppings)
    order_item = pizza_size + " " + pizza_type + " with " + toppings_string
    def pizza_calculator(pizza_size,pizza_type,toppings):
        if pizza_size == "Small" and pizza_type == "Regular":
            x = 12.20
            y = len(toppings)*1
            return x + y
        elif pizza_size == "Large" and pizza_type == "Regular":
            x = 17.45
            y = len(toppings)*2
            return x + y
        elif pizza_size == "Small" and pizza_type == "Sicilian":
            x = 23.45
            y = len(toppings)*2
            return x + y
        elif pizza_size == "Large" and pizza_type == "Sicilian":
            x = 37.70
            y = len(toppings)*2
            return x + y
    price = pizza_calculator(pizza_size,pizza_type,toppings)
    print(price)
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))

#special pizza is 5 random ingredients (user can still pick size and type)
def special_pizza (request):
    order_name = request.user
    pizza_size = request.POST["size"]
    pizza_type = request.POST["type"]
    all_toppings = Pizza_Topping.objects.all()
    toppings_list = []
    for topping in all_toppings:
        toppings_list.append(topping.name)
    random_list = []
    random_list += random.sample(toppings_list, 5)
    string_random_list = str(random_list)
    order_item = "Special with " + string_random_list
    def pizza_calculator(pizza_size, pizza_type):
        if pizza_size == "Small" and pizza_type == "Regular":
            return 17.25
        elif pizza_size == "Large" and pizza_type == "Regular":
            return 25.45
        elif pizza_size == "Small" and pizza_type == "Sicilian":
            return 29.45
        elif pizza_size == "Large" and pizza_type == "Sicilian":
            return 44.70
    price = pizza_calculator(pizza_size, pizza_type)
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))

# User can finalize an order, which send them to a Final Order page that moves their Order to the
# includes the everything they ordered (with the total) Confirmed_Order database, deletes their order from the Order database,
# and renders a confirmation page with -- orders that have not been confirmed (Boolean finished == "False") are noted
# as "processing" and orders that have been confirmed (Boolean finished == "True") are noted as "done."
def checkout(request):
    your_order = Order.objects.filter(order_name=request.user).all()
    all_the_items = []
    for y in your_order:
        all_the_items.append(y.order_item)
    all_the_items_price = []
    for x in your_order:
        all_the_items_price.append(x.price)
    total = sum(all_the_items_price)
    f = Confirmed_Order(order_name=request.user,final_order=all_the_items,total=total)
    f.save()
    your_confirmed_order = Confirmed_Order.objects.filter(order_name=request.user).all()
    context = {
        "your_confirmed_order": your_confirmed_order
    }
    your_order.delete()
    return render(request, "checkout.html", context)

# Confirmed Orders page (only viewable by the admin)
def confirmed_orders(request):
    if not request.user.is_staff:
        return render(request, "login.html", {"message": "Log-in as staff to see Confirmed Orders."})
    context = {
        "user": request.user
    }
    context = {
    "all_confirmed_orders": Confirmed_Order.objects.all()
    }
    return render(request, "confirmed_orders.html", context)

# On the Confirmed Orders page, admin can switch an Order to "Finished," which removes it from this page.
def confirm_final_order(request):
    final_order_id = request.POST["final_order_id"]
    set_order_to_confirm = Confirmed_Order.objects.get(pk=final_order_id)
    set_order_to_confirm.finished = True
    set_order_to_confirm.save()
    print(set_order_to_confirm)
    return HttpResponseRedirect(reverse("confirmed_orders"))





