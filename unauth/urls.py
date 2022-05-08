from django.urls import path
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, ResetPasswordView, ChangePasswordView, profile, RegisterView, Dashboard
from .forms import LoginForm
from users.views import  home



urlpatterns = [
    
    path('', home, name='users-home'),
    
    path('register/', RegisterView.as_view(), name='users-register'),
    
    path('profile/', profile, name='users-profile'),
    
    path('dashboard/', Dashboard, name='users-dashboard'),
    
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='unauth/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/home.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='unauth/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='unauth/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)