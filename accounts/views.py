from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class ProfilePage(TemplateView):
    template_name = 'accounts/profile.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/index.html'