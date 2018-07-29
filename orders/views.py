from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Pizza_Topping, Pizza_Size, Pizza_Type, Sub_Size, Sub_Add_On, Dinner_Platter_Size, Sub, Pizza, Pasta, Salad, Platter, Order, Confirmed_Order

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user
    }
    return HttpResponseRedirect(reverse("menu"))

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

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def menu(request):
    context = {
        "toppings": Pizza_Topping.objects.all(),
        "sizes": Pizza_Size.objects.all(),
        "types": Pizza_Type.objects.all(),
        "your_orders": Order.objects.filter(order_name=request.user).all(),
        "sub": Sub.objects.all(),
        "salads": Salad.objects.all(),
        "sub_add_on": Sub_Add_On.objects.all(),
        "sub_size": Sub_Size.objects.all(),
        "platters": Platter.objects.all(),
        "pastas": Pasta.objects.all()

    }
    return render(request, "menu.html", context)

def add_salad_order (request):
    order_name = request.user
    order_item = request.POST["salad"]
    price = Salad.objects.get(name=order_item).price
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))

def add_platter_order (request):
    order_name = request.user
    order_item = request.POST["platter"]
    price = Platter.objects.get(name=order_item).price
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))

def add_pasta_order (request):
    order_name = request.user
    order_item = request.POST["pasta"]
    price = Pasta.objects.get(name=order_item).price
    f = Order(order_name=order_name,order_item=order_item,price=price)
    f.save()
    return HttpResponseRedirect(reverse("menu"))



def add_pizza_order (request):
    order_name = request.user
    pizza_size = request.POST["size"]
    pizza_type = request.POST["type"]
    toppings = request.POST.getlist("toppings")
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
    context = {
        "your_order": your_order,
        "total": total
    }
    return render(request, "checkout.html", context)




