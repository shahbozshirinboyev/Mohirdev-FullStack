from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, \
                  PostCommentsListView, PostCommentsCreateView, PostLikeListView, \
                  CommentListCreateApiView, CommentRetrieveView, CommentLikeListView, \
                  LikesListView, LikeCreateView, LikeDeleteView

urlpatterns = [
  path('list/', PostListApiView.as_view()),
  path('create/', PostCreateView.as_view()),
  path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
  path('<uuid:pk>/likes/', PostLikeListView.as_view()),
  path('<uuid:pk>/comments/', PostCommentsListView.as_view()),
  path('<uuid:pk>/comments/create/', PostCommentsCreateView.as_view()),

  path('comments/', CommentListCreateApiView.as_view()),
  path('comments/<uuid:pk>/', CommentRetrieveView.as_view()),
  path('comments/<uuid:pk>/likes/', CommentLikeListView.as_view()),

  path('likes/', LikesListView.as_view() ),
  path('likes/create/', LikeCreateView.as_view() ),
  path('likes/delete/', LikeDeleteView.as_view() ),
]