from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class Index(TemplateView):
    template_name = 'accounts/index.html'

class LoginPage(LoginView):
    template_name = 'accounts/login.html'

class SignInPage(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signin.html'  # サインアップフォームのテンプレート
    success_url = '/'  # ログイン後のリダイレクト先URL

    def form_valid(self, form):
        response = super().form_valid(form)
        self.login(self.request, self.object)  # ログイン処理
        return response

    def login(self, request, user):
        from django.contrib.auth import login
        login(request, user)

class ProfilePage(TemplateView):
    template_name = 'accounts/profile.html'

class LogoutPage(LogoutView):
    template_name = 'accounts/index.html'