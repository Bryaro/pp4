from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile

from django.contrib.auth.decorators import login_required
from reservations.models import Reservation
from django.contrib import messages
from allauth.account.utils import send_email_confirmation
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User


# Create your views here.

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
    return render(request, 'accounts/profile_create.html', {'form': form})


@login_required
def profile_detail(request):
    user = request.user
    if not user.is_active:
        messages.error(request, 'Make sure to verify email to view your profile')
        return redirect('home')

    try:
        profile = UserProfile.objects.get(user=request.user)
        reservations = Reservation.objects.filter(user=request.user)

        # Check if the user's email is verified
        if EmailAddress.objects.filter(user=request.user, verified=True).exists():
            email_message = f"<p><strong>Email:</strong> {profile.user.email}</p>"
        else:
            email_message = f"<p><strong>Email:</strong> Email verification pending for {profile.user.email}. Check your inbox for verification email.</p>"


    except UserProfile.DoesNotExist:
        return redirect('accounts:create_profile')
    
    return render(request, 'accounts/profile_detail.html', {'profile': profile, 'reservations': reservations})


@login_required
def edit_profile(request):
    user = request.user
    if not user.is_active:
        messages.error(request, 'Make sure to verify your email address before editing your profile')
        return redirect ('accounts:profile_detail')

    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Get the new email address from the form
            change_email = form.cleaned_data.get('change_email', False)
            if change_email:
                new_email = form.cleaned_data.get('new_email')
                if new_email != user.email:
                    # Create a new EmailAddress instance for the new email
                    user.email = new_email
                    user.save()

                    # Send email verification for the new email
                    send_email_confirmation(request, user)
                    # Set email_verified to False to reflect pending verification status
                    user.email_verified = False
                    user.save() 

            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('accounts:profile_detail')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        profile = get_object_or_404(UserProfile, user=request.user)
        profile.delete()
        return redirect('home') # Redirect to the home page or another appropriate page
    else:
        return redirect('profile_detail')