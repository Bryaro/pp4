from django.views.generic import TemplateView
from django.shortcuts import render


class index(TemplateView):
    """
    A class-based view that renders the homepage of the website,
    using the specified template.
    Inherits from Django's generic TemplateView.
    """
    template_name = 'home/index.html'


def about(request):
    """
    Function-based view that renders the 'About' page of the website.
    Simply returns the 'about.html' template.
    """
    return render(request, 'home/about.html')


def contact(request):
    """
    Function-based view that renders the 'Contact' page of the website.
    Displays contact/opening hours information using the 'contact.html'.
    """
    return render(request, 'home/contact.html')


def reserve_table(request):
    """
    Function-based view that renders table reservation page for the website.
    Provides a form or interface for users to reserve a table,
    using the 'reserve_table.html' template.
    """
    return render(request, 'reservations/reserve_table.html')
