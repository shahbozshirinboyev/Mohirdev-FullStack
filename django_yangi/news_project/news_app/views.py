from django.shortcuts import render, get_object_or_404
from .models import Category, News
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import TemplateView

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
  news_list = News.published.all().order_by('-publish_time')
  categories = Category.objects.all()
  context = {
    'news_list': news_list,
    'categories': categories
  }
  return render(request, 'news/index.html', context)

def categoryPageView(request):
    return render(request, 'news/catagory.html')

# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#        form.save()
#        return HttpResponse("<h2>Biz bilan bog'langaningiz uchun rahmat!</h2>")
#     context = {
#        'form': form
#     }
#     return render(request, 'news/contact.html', context)

# contactPageView'ni class orqali ham qilib ko'ramiz:
class ContactPageView(TemplateView):
   template_name = 'news/contact.html'

   def get(self, request, *args, **kwargs):
      form = ContactForm
      context = {
         'form': form,
      }
      return render(request, 'news/contact.html', context)

   def post(self, request, *args, **kwargs):
      form = ContactForm(request.POST)
      if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("<h2>Biz bilan bog'langaningiz uchun rahmat!</h2>")
      context = {
         'form': form,
      }
      return render(request, 'news/contact.html', context)