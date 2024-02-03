from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_profile(request):
    if UserProfile.objects.filter(user=request.user).exists():
        return redirect('accounts:profile_detail')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, unique=True)
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
    try:
        profile = UserProfile.objects.get(user=request.user)
        print(f"User ID: {profile.user.id}")
        print(f"User Full Name: {profile.user.get_full_name()}")
    except UserProfile.DoesNotExist:
        return redirect('accounts:create_profile')
    
    return render(request, 'accounts/profile_detail.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
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