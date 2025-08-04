from django.urls import path
from books.views import BooksListView, BookDetailView

app_name = 'books'
urlpatterns = [
  path('', BooksListView.as_view(), name='list'),
  path('<int:id>/', BookDetailView.as_view(), name='detail')
]