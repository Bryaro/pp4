from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile

from django.contrib.auth.decorators import login_required
from reservations.models import Reservation
from django.contrib import messages
from allauth.account.utils import send_email_confirmation
from allauth.account.models import EmailAddress


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
            form.save()

            # Get the new email address from the form
            new_email = form.cleaned_data.get('email')
            if new_email != user.email:
                # Create a new EmailAddress instance for the new email
                email_address = EmailAddress.objects.add_email(request, user, new_email, confirm=False)

                # Send email verification for the new email
                send_email_confirmation(request, user, email_address)

                messages.success(request, 'A verification email has been sent to the new email address. Please verify your email to complete the update.')
            else:
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