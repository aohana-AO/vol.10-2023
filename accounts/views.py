from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts/index.html')

class SignInPage(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/signin.html'

class ProfilePage(TemplateView):
    template_name = 'accounts/profile.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/index.html'