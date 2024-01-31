from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('about/', about, name='about'),
]