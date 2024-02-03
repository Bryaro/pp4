from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]