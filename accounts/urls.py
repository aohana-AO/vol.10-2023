from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('accounts/profile/', views.ProfilePage.as_view(), name='profile'),
    path('logout/', views.LogoutPage.as_view(), name='logout'),
    path('signin/', views.SignInPage.as_view(), name='signin'),
]