# profiles/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('accounts/signup/', views.signup, name='signup'),  # Signup page
    path('accounts/login/', LoginView.as_view(template_name='profiles/login.html'), name='login'),  # Login page
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Logout page
    path('profile/', views.profile, name='profile'),  # User profile page
    path('accounts/profile/', views.profile, name='account_profile'),  # Profile page after login (optional)
]
