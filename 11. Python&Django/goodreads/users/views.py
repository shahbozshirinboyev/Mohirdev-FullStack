from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from users.forms import UserCreateForm
from django.contrib import messages

class RegisterView(View):
  def get(self, request):
    create_form = UserCreateForm()
    context = {
      "form": create_form
    }
    return render(request, 'users/register.html', context)

  def post(self, request):
    create_form = UserCreateForm(data=request.POST)
    if create_form.is_valid():
      create_form.save()
      return redirect('users:login')
    else:
      context = { "form": create_form }
      return render(request, 'users/register.html', context)

class ProfileView(LoginRequiredMixin, View):
  def get(self, request):
    context = { 'user': request.user }
    return render(request, 'users/profile.html', context)

class LoginView(View):
  def get(self, request):
    login_form = AuthenticationForm()
    return render(request, 'users/login.html', {"login_form": login_form})

  def post(self, request):
    login_form = AuthenticationForm(data=request.POST)
    if login_form.is_valid():
      user = login_form.get_user()
      login(request, user)
      messages.success(request, 'You have successfully logged in.')
      return redirect('books:list')
    else:
      return render(request, 'users/login.html', {"login_form": login_form})

class LogoutView(LoginRequiredMixin, View):
  def get(self, request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('index')