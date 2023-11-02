from django.urls import path
from .views import RegisterView, Login

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('', Login.as_view(), name='login'),
]