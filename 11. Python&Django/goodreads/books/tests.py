from django.test import TestCase
from django.urls import reverse
from books.models import Book

# Create your tests here.
class BookTestCase(TestCase):

  def test_no_books(self):
    response = self.client.get(
      reverse('books:list'),
    )
    self.assertContains(response, 'No books found.')

  def test_books_list(self):
    Book.objects.create( title='book1', description = 'description1', isbn='1231' )
    Book.objects.create( title='book2', description = 'description2', isbn='1232' )
    Book.objects.create( title='book3', description = 'description3', isbn='1233' )

    books = Book.objects.all()
    response = self.client.get(
      reverse('books:list'),
    )

    for book in books:
      self.assertContains(response, book.title)

  def test_detail_page(self):
    book = Book.objects.create( title='book1', description = 'description1', isbn='1231' )
    response = self.client.get(
      reverse('books:detail', kwargs={"id": book.id}),
    )

    self.assertContains(response, book.title)
    self.assertContains(response, book.description)
