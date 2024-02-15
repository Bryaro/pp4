from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'number_of_guests')
    list_filter = ('date', 'time')
    search_fields = ('user__username', 'date')
    date_hierarchy = 'date'
