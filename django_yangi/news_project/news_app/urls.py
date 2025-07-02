from django.urls import path
from .views import news_list, news_detail, homePageView, contactPageView

urlpatterns = [
  path('', homePageView, name='home_page'),
  path('contact/', contactPageView, name='contact'),
  path('news/', news_list, name='all_news_list'),
  path('news/<int:id>/', news_detail, name='news_detail_page')
]