from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, \
                  PostCommentsListView, PostCommentsCreateView

urlpatterns = [
  path('posts/', PostListApiView.as_view()),
  path('create/', PostCreateView.as_view()),
  path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
  path('comments/<uuid:pk>/', PostCommentsListView.as_view()),
  path('comments/<uuid:pk>/create/', PostCommentsCreateView.as_view()),
]