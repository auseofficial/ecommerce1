from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('', views.store, name="cart"),
    path('', views.store, name="checkout"),
]
