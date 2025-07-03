from django.urls import path
from .views import news_list, news_detail, HomePageView, ContactPageView, categoryPageView, AboutPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home_page'),
  path('catagory/', categoryPageView, name='catagory'),
  path('about/', AboutPageView, name='about'),
  path('contact/', ContactPageView.as_view(), name='contact'),
  path('news/', news_list, name='all_news_list'),
  path('news/<int:id>/', news_detail, name='news_detail_page')
]