from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Reservation
from django.db import transaction
from django.utils import timezone


@login_required
def reserve_table(request):
    """
    Allows logged-in users to make a table reservation.
    Validates the form data to ensure,
    no double bookings for the same date and time.
    Sends a confirmation email upon successful reservation,
    and displays a confirmation page.
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user

            # Check if reservation exists for the selected date and time
            existing_reservation = Reservation.objects.filter(
                date=reservation.date, time=reservation.time).exists()

            if existing_reservation:
                return render(request,
                              'reservations/reserve_exists.html',
                              {
                                  'date': reservation.date,
                                  'time': reservation.time
                              })

            with transaction.atomic():
                reservation.save()

            # As my userstory, I want to send confirmation email to user
            # using users email that was registered on sign up
            subject = 'Reservation Confirmation'
            message = (
                f'Your reservation details:\n'
                f'Number of Guests: {reservation.number_of_guests}\n'
                f'Date: {reservation.date}\n'
                f'Time: {reservation.time}'
            )
            from_email = 'bryarosman.bo@gmail.com'
            recipient_list = [request.user.email]

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

            context = {
                'number_of_guests': reservation.number_of_guests,
                'date': reservation.date,
                'time': reservation.time,
            }
            # Redirects to new URL:
            return render(request, 'reservations/reserve_confirmation.html',
                          context)
    else:
        form = ReservationForm(initial={'name': request.user.username})
    return render(request, 'reservations/reserve_table.html', {'form': form})


@login_required
def user_reservations(request):
    """
    Displays a list of all reservations made by the logged-in user,
    visible on their profile page.
    """
    reservations = Reservation.objects.filter(user=request.user)
    return render(request,
                  'accounts/profile_detail.html',
                  {'reservations': reservations})


@login_required
def edit_reservation(request, reservation_id):
    """
    Allows users to edit their reservation details,
    given the reservation date is more than 2 days ahead.
    If the reservation date is less than 2 days, then
    editing is not allowed and a specific page is shown to guide user.
    """
    reservation = get_object_or_404(
     Reservation, id=reservation_id, user=request.user)

    difference = (reservation.date - timezone.now().date()).days

    if difference < 2:
        return render(request,
                      'reservations/cancel_not_allowed.html',
                      {'reservation': reservation})

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_detail')
    else:
        form = ReservationForm(instance=reservation)
    return render(request,
                  'reservations/edit_reservation.html', {'form': form})


@login_required
def cancel_reservation(request, reservation_id):
    """
    Enables users to cancel their reservations,
    user can only cancel if the reservation date is less than 2 days away.
    Sends a cancellation confirmation email upon successful cancellation.
    """
    reservation = get_object_or_404(
        Reservation, id=reservation_id, user=request.user)

    difference = (reservation.date - timezone.now().date()).days

    if request.method == 'POST':

        if difference < 2:
            return render(request,
                          'reservations/cancel_not_allowed.html',
                          {'reservation': reservation})

        # send cancellation email to user
        subject = 'Cancellation Confirmed!'
        message = (
            f'Your reservation for {reservation.date} at '
            f'{reservation.time} has been canceled'
        )

        from_email = 'bryarosman.bo@gmail.com'
        recipient_list = [request.user.email]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )

        reservation.delete()
        # Add a success message here if you want
        return redirect('accounts:profile_detail')
    return render(request,
                  'reservations/cancel_reservation.html',
                  {'reservation': reservation})
