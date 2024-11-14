# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def home(request):
    """
    Home page view - Display the homepage where users can 
    navigate to login or signup.
    """
    return render(request, 'profiles/home.html')

def signup(request):
    """
    Signup view - Handles the user registration. 
    If the form is valid, the user will be logged in and redirected to the profile page.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the new user
            login(request, user)  # Log the user in immediately after signup
            return redirect('profile')  # Redirect to the profile page
    else:
        form = SignupForm()  # Display the form when the request is not POST
    return render(request, 'profiles/signup.html', {'form': form})

@login_required
def profile(request):
    """
    Profile view - Displays the user's profile page. This view is protected by login_required.
    Only logged-in users can access this page.
    """
    return render(request, 'profiles/profile.html')
