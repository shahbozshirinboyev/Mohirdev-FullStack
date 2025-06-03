from .views import bloglistview, blogdetailview
from django.urls import path

urlpatterns = [
  path("", bloglistview, name="blog_list_view"),
  path("blogs/<int:id>/", blogdetailview, name="blog_detail"),
]