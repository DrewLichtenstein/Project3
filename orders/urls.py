from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.signup, name='signup'),
    path("menu", views.menu,name="menu"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("add_pizza_order", views.add_pizza_order, name="add_pizza_order"),
    path("checkout",views.checkout, name="checkout"),
    path("add_salad_order", views.add_salad_order, name="add_salad_order"),
    path("add_platter_order", views.add_platter_order, name="add_platter_order"),
    path("add_pasta_order", views.add_pasta_order, name="add_pasta_order"),
    path("", views.index, name="index")
]
