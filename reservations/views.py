from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Reservation
from django.contrib.auth.decorators import login_required

@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            # As my userstory, I want to send confirmation email to user
            # using users email that was registered on sign up
            subject = 'Reservation Confirmation'
            message = f'Your reservation details:\nNumber of Guests: {reservation.number_of_guests}\nDate: {reservation.date}\nTime: {reservation.time}'
            from_email = 'bryarosman.bo@gmail.com'
            recipient_list = [request.user.email]

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

            # Debug message
            print(f"Email sent to {request.user.email} for reservation on {reservation.date} at {reservation.time}")
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

@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/user_reservations.html', {'reservations': reservations})

@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        # Add a success message here if you want
        return redirect('reservations:user_reservations')
    return render(request, 'reservations/cancel_reservation.html', {'reservation': reservation})