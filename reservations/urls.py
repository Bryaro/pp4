from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('reserve/', views.reserve_table, name='reserve_table'),
    path('user_reservations/', views.user_reservations, name='user_reservations'),
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('make_reservation/', views.reserve_table, name='make_reservation'),
    path('reserve_confirmation/', views.reserve_table, name='reserve_confirmation'),
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
]
