from django.shortcuts import render, get_object_or_404
from .models import Category, News

# Create your views here.
def news_list(request):
  news_list_published = News.published.all()
  news_list_draft = News.objects.filter(status=News.Status.Draft)
  context = {
    'news_list_published': news_list_published,
    'news_list_draft': news_list_draft
  }
  return render(request, 'news/news_list.html', context)

def news_detail(request, id):
  news = get_object_or_404(News, id=id, status=News.Status.Published)
  context = {
    'news': news,
  }
  return render(request, 'news/news_detail_page.html', context)

def homePageView(request):
  news = News.published.all()
  categories = Category.objects.all()
  context = {
    'news': news,
    'categories': categories
  }
  return render(request, 'news/index.html', context)