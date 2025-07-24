from django.urls import path
from .views import BookListApiView, BookDetailApiView, BookDeleteApiView, \
                  BookUpdateApiView, BookCreateApiView, BookListCreateApiView, \
                  BookListUpdateDeleteApiView

urlpatterns = [
  path('bookslist/', BookListCreateApiView.as_view(),),
  path('bookslist/<int:pk>', BookListUpdateDeleteApiView.as_view(),),
  path('books/', BookListApiView.as_view(),),
  path('books/create/', BookCreateApiView.as_view(),),
  path('books/<int:pk>/', BookDetailApiView.as_view(),),
  path('books/<int:pk>/delete/', BookDeleteApiView.as_view(),),
  path('books/<int:pk>/update/', BookUpdateApiView.as_view(),),
]