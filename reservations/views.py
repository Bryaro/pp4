from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required


@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            # Display to user their booking info in the confirmation page
            context = {
                'number_of_guests': reservation.number_of_guests,
                'date': reservation.date,
                'time': reservation.time,
            }
            # Redirects to new URL:
            return render(request, 'reservations/reserve_confirmation.html', context)
    else:
        form = ReservationForm(initial={'name': request.user.username})
    return render(request, 'reservations/reserve_table.html',{'form': form})