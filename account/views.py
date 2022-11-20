from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from django.views.generic import CreateView


class MySignupView(CreateView):
    form_class = UserRegistrationForm
    success_url = 'login'
    template_name = 'account/login.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'account/login.html'
