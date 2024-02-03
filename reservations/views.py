from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib.auth.decorations import login_required


@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            # Redirects to new URL:
            return redirect('reservations:reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reserve_table.html',{'form': form})