from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Donation, WasteTracking, Request
from .forms import DonationForm, WasteTrackingForm, RequestForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# @login_required
# def home(request):
#     # Redirect admin users to the admin panel if they try to access the user site
#     if request.user.is_superuser:
#         return redirect('/admin') 
#     else:
#         return redirect('/home')# Admin should be redirected to the admin site
    
#     # For normal users, show the regular user home page
#     donations = Donation.objects.all()
#     waste_tracks = WasteTracking.objects.all()
#     requests = Request.objects.all()

#     return render(request, 'waste_app/home.html', {
#         'donations': donations,
#         'waste_tracks': waste_tracks,
#         'requests': requests,
#     })


# Home View
def home(request):
    donations = Donation.objects.all()
    waste_tracks = WasteTracking.objects.all()
    requests = Request.objects.all()
    
    return render(request, 'waste_app/home.html', {
        'donations': donations, 
        'waste_tracks': waste_tracks, 
        'requests': requests
    })

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after signup
            return redirect('home')  # Redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, 'waste_app/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'waste_app/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'waste_app/logout.html')

# Donate Food View
@login_required
def donate_food(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DonationForm()
    return render(request, 'waste_app/donate_food.html', {'form': form})

# Request Food View
@login_required
def request_food(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            food_request = form.save(commit=False)
            food_request.user = request.user  # Assign request to logged-in user
            food_request.save()
            return redirect('home')
    else:
        form = RequestForm()
    return render(request, 'waste_app/request_food.html', {'form': form})

# Waste Tracking View
@login_required
def waste_tracking(request):
    if request.method == 'POST':
        form = WasteTrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WasteTrackingForm()
    return render(request, 'waste_app/track_waste.html', {'form': form})
