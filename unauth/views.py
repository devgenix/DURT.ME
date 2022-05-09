
import os
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .models import Analytics, AuthModel
from .serializers import UrlSerializer
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm


@api_view(['POST'])  
def Shortener(request):

    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        returned_data = serializer.data.get('short_url')
        
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'unauth/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'unauth/password_reset.html'
    email_template_name = 'unauth/password_reset_email.html'
    subject_template_name = 'unauth/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'unauth/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='unauth-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'unauth/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def Dashboard(request): 
    Data = AuthModel.objects.all()
    short_urls = AuthModel.objects.order_by('-visits')[0:10]
    return render(request, 'unauth/dashboard.html', {'Analytics': Data, 'short_urls': enumerate(short_urls, 1)})