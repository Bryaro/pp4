from django.views.generic import TemplateView
from django.shortcuts import render


class index(TemplateView):
    template_name = 'home/index.html'

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')