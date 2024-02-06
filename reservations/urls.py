# reservations/urls.py
from django.urls import path
from . import views

app_name = 'reservations'  # Here I am defining the app namespace

urlpatterns = [
    path('reserve/', views.reserve_table, name='reserve_table'),
    path('user_reservations/', views.user_reservations, name='user_reservations'),
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('make_reservation/', views.reserve_table, name='make_reservation'),
    path('reserve_confirmation/', views.reserve_table, name='reserve_confirmation'),  # Use the same view as reserve_table
]
