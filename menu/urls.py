from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_menu/', views.add_menu_item, name='add_menu_item'),
    path('menu/', views.menu_list, name='menu_list'),
]