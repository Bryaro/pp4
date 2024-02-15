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
    """
    View for creating a new user profile. If the user already has a profile,
    redirects to the profile detail page. On POST, validates and saves the new
    profile form, then redirects to the profile detail page.
    Otherwise, displays a blank profile form.
    """
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
    """
    View for displaying the details of the user's profile,
    including any reservations.
    A permanent text showing users always to make sure to verify their email,
    if they have updated their email.
    If the profile does not exist, redirects to the profile creation page.
    """
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
    """
    View for editing an existing user profile.
    On POST, updates the user's profile with the form data.
    If a new email is provided, triggers an email verification process.
    On success, redirects to the profile detail page.
    Otherwise, displays the profile form pre-filled with user's profile data.
    """
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
    """
    View for deleting the user's profile and users reservations.
    On POST, deletes the user's profile and all associated reservations,
    within an atomic transaction to ensure data integrity, then redirects to
    the home page. Otherwise, displays a confirmation prompt.
    """
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
    """
    View for deleting the user's account.
    On POST, deletes the user's account and redirects to the home page.
    Otherwise, displays a confirmation prompt indicating account deletion.
    """
    if request.method == 'POST':
        # If the user confirms deletion, delete the entire account
        request.user.delete()
        return redirect('home')  # Redirect to home page or wherever you want
    return render(
        request,
        'accounts/profile_confirm_delete.html', {'delete_account': True})
