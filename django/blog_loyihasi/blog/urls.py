from .views import Bloglistview, BlogDetailView
from django.urls import path

urlpatterns = [
  path("", Bloglistview.as_view(), name="blog_list_view"),
  path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog_detail_view"),
]