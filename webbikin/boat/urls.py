from django.urls import path
from . import views

urlpatterns = [
    path('', views.boat, name="boat"),
    path('cart/', views.cart, name="cart"),
    path('boatsearch/', views.boatsearch, name="boatsearch"),
    path('checkout/', views.checkout, name="checkout")
]