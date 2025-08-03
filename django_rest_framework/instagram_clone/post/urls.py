from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, \
                  PostCommentsListView, PostCommentsCreateView, CommentListCreateApiView

urlpatterns = [
  path('list/', PostListApiView.as_view()),
  path('create/', PostCreateView.as_view()),
  path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
  path('<uuid:pk>/comments/', PostCommentsListView.as_view()),
  path('<uuid:pk>/comments/create/', PostCommentsCreateView.as_view()),
  path('comments/', CommentListCreateApiView.as_view()),
]