from django.urls import path
from .views import index, about, contact


urlpatterns = [
    path('', index.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
