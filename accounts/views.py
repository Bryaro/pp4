from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile

from django.contrib.auth.decorators import login_required
from reservations.models import Reservation
from django.contrib import messages
from allauth.account.utils import send_email_confirmation
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from django.db import transaction


@login_required
def create_profile(request):
    if UserProfile.objects.filter(user=request.user).exists():
        return redirect('accounts:profile_detail')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:profile_detail')
    else:
        form = UserProfileForm()
    return render(request, 'accounts/profile_form.html', {'form': form})


@login_required
def profile_detail(request):
    user = request.user
    if not user.is_active:
        messages.error(
            request, 'Make sure to verify email to view your profile')
        return redirect('home')

    try:
        profile = UserProfile.objects.get(user=request.user)
        reservations = Reservation.objects.filter(user=request.user)

        # Fetch email verification status
        email_verified = EmailAddress.objects.filter(
            user=request.user, verified=True).exists()

    except UserProfile.DoesNotExist:
        return redirect('accounts:create_profile')

    return render(
        request, 'accounts/profile_detail.html',
        {'profile': profile, 'reservations': reservations})


@login_required
def edit_profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Check if a new email address is provided
            new_email = form.cleaned_data.get('new_email')
            if new_email:
                # Trigger verification email sending process
                user.email = new_email
                user.save()
                send_email_confirmation(request, user)

            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('accounts:profile_detail')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        # If the user confirms deletion,
        # delete the profile and associated reservations
        profile = request.user.profile
        reservations = Reservation.objects.filter(user=request.user)
        with transaction.atomic():
            profile.delete()
            reservations.delete()
        # Optionally, you can add a message to indicate successful deletion
        messages.success(request, 'Your profile has been deleted.')
        return redirect('home')  # Redirect to home page or wherever you want
    return render(
        request,
        'accounts/profile_confirm_delete.html', {'delete_account': False})


@login_required
def delete_account(request):
    if request.method == 'POST':
        # If the user confirms deletion, delete the entire account
        request.user.delete()
        return redirect('home')  # Redirect to home page or wherever you want
    return render(
        request,
        'accounts/profile_confirm_delete.html', {'delete_account': True})
