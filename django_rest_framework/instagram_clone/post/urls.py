from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
  path('posts/', PostListApiView.as_view()),
  path('create/', PostCreateView.as_view()),
  path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
]