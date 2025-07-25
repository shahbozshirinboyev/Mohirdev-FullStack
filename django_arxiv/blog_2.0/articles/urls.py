from django.urls import path
from .views import (
  ArticleListView,
  ArticleUpdateView,
  ArticleDeleteView,
  ArticleDetailView,
  ArticleCreateView,
)

urlpatterns = [
  path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
  path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
  path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
  path('add/', ArticleCreateView.as_view(), name='article_add'),
  path('', ArticleListView.as_view(), name='article_list')
]