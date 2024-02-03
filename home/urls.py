from django.urls import path
from .views import index, about, contact, reserve_table

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('reserve-table/', reserve_table, name='reserve_table'),
]