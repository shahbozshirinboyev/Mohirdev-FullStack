from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserLogin

urlpatterns = [
  # path('login/', UserLogin, name='login'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
]