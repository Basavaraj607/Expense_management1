from django.contrib.auth import views as auth_views
from .forms import LoginForm

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm

class LogoutView(auth_views.LogoutView):
    next_page = "accounts:login"
