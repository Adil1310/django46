from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import CustomUser
from .forms import RegisterForm

# Create your views here.

class RegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'