from django.urls import path
from .views import home, profile, RegisterView, Dashboard
from API.views import Redirect

urlpatterns = [
    path('', home, name='users-home'),
    path('<str:url>', Redirect, name='redirect'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('dashboard/', Dashboard, name='users-dashboard'),
]
