from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  print(request.user.is_authenticated)
  return render(request, 'index.html')