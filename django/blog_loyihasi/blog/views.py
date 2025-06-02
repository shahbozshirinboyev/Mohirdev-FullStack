from django.shortcuts import render
from .models import Blog

# Create your views here.
def bloglistview(request):
  blogs = Blog.objects.all()
  users = User.objects.all()

  context = {
    "blogs": blogs
  }
02.20