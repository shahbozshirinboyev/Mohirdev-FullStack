from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, UserRegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def UserLogin(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = authenticate(request,
                          username = data['username'],
                          password = data['password']
                          )
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponse('Muvaffaqiyatli login amalga oshirildi!')
        else:
          return HttpResponse('Sizning accountingiz faol holatda emas.')
      else:
        return HttpResponse('Login va Parolda xatolik bor!')
  else:
    form = LoginForm()
    context = {
      'form': form
    }
  return render(request, 'registration/login.html', context)

def DashboardView(request):
  user = request.user
  context = {
    'user': user,
  }
  return render(request, 'pages/profile.html', context)

def UserRegister(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(
        user_form.cleaned_data['password']
      )
      new_user.save()
      context = {
        'new_user': new_user
      }
      return render(request, 'account/register_done.html', context)
  else:
    user_form = UserRegistrationForm()
    context = {
      'user_form': user_form
    }
    return render(request, 'account/register.html', context)

class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'account/register.html'
