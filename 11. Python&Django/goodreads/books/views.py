from django.shortcuts import render
from django.views import View
from books.models import Book
from django.views import generic

# Create your views here.
class BooksListView(generic.ListView):
  template_name = 'books/list.html'
  queryset = Book.objects.all()
  context_object_name = 'books'

class BookDetailView(generic.DetailView):
  template_name = 'books/detail.html'
  pk_url_kwarg = 'id'
  model = Book
  context_object_name = 'book'

# class BooksListView(View):
#   def get(self, request):
#     books = Book.objects.all()
#     context = {
#       'books': books,
#     }
#     return render(request, 'books/list.html', context)

# class BookDetailView(View):
#   def get(self, request, id):
#     book = Book.objects.get(id=id)
#     context = {
#       'book': book,
#     }
#     return render(request, 'books/detail.html', context)