from django.shortcuts import render
from .models import Category, News

# Create your views here.
def news_list(request):
  news_list = News.objects.all()
  context = {
    'new_list': news_list
  }
  return render(request, 'news/news_list.html', context)