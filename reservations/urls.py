# reservations/urls.py
from django.urls import path
from . import views

app_name = 'reservations'  # Here I am defining the app namespace

urlpatterns = [
    path('make_reservation/', views.reserve_table, name='make_reservation'),
]
