from django.urls import path
from .views import news_list, news_detail, HomePageView, ContactPageView, categoryPageView, AboutPageView, \
  SportNewsView, SiyosatNewsView, TexnologiyaNewsView, JamiyatNewsView, IqtisodiyotNewsView

urlpatterns = [
  path('', HomePageView.as_view(), name='home_page'),
  path('categories/', categoryPageView, name='categories'),
  path('about/', AboutPageView, name='about'),
  path('contact/', ContactPageView.as_view(), name='contact'),
  path('news/', news_list, name='all_news_list'),
  path('news/<slug:news>/', news_detail, name='news_detail_page'),
  path('sport/', SportNewsView.as_view(), name='sport'),
  path('siyosat/', SiyosatNewsView.as_view(), name='siyosat'),
  path('texnologiya/', TexnologiyaNewsView.as_view(), name='texnologiya'),
  path('jamiyat/', JamiyatNewsView.as_view(), name='jamiyat'),
  path('iqtisodiyot/', IqtisodiyotNewsView.as_view(), name='iqtisodiyot'),
]