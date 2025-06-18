from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return HttpResponse("Hell0, I am Shahboz and this is my first Project!")