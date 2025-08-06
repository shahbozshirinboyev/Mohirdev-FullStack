from django.test import TestCase
from django.urls import reverse
from books.models import Book
from users.models import CustomUser

# Create your tests here.
class BookTestCase(TestCase):

  def test_no_books(self):
    response = self.client.get(
      reverse('books:list'),
    )
    self.assertContains(response, 'No books found.')

  def test_books_list(self):
    book1 = Book.objects.create( title='book1', description = 'description1', isbn='1231' )
    book2 = Book.objects.create( title='book2', description = 'description2', isbn='1232' )
    book3 = Book.objects.create( title='book3', description = 'description3', isbn='1233' )
    book4 = Book.objects.create( title='book4', description = 'description4', isbn='1234' )
    book5 = Book.objects.create( title='book5', description = 'description5', isbn='1235' )
    book6 = Book.objects.create( title='book6', description = 'description6', isbn='1236' )

    response1 = self.client.get( reverse('books:list'), )
    for book in [book1, book2, book3]:
      self.assertContains(response1, book.title)

    response2 = self.client.get( reverse('books:list')+"?page=2", )
    for book in [book4, book5, book6]:
      self.assertContains(response2, book.title)

  def test_detail_page(self):
    book = Book.objects.create( title='book1', description = 'description1', isbn='1231' )
    response = self.client.get(
      reverse('books:detail', kwargs={"id": book.id}),
    )

    self.assertContains(response, book.title)
    self.assertContains(response, book.description)

  def test_search_books(self):
    book1 = Book.objects.create( title='Sport Health', description = 'description1', isbn='1231' )
    book2 = Book.objects.create( title='Guide book', description = 'description2', isbn='1232' )
    book3 = Book.objects.create( title='Shoe Dog', description = 'description3', isbn='1233' )

    response = self.client.get(reverse('books:list')+'?q=sport')
    self.assertContains(response, book1.title)
    self.assertNotContains(response, book2.title)
    self.assertNotContains(response, book3.title)

    response = self.client.get(reverse('books:list')+'?q=guide')
    self.assertContains(response, book2.title)
    self.assertNotContains(response, book1.title)
    self.assertNotContains(response, book3.title)

    response = self.client.get(reverse('books:list')+'?q=shoe')
    self.assertContains(response, book3.title)
    self.assertNotContains(response, book2.title)
    self.assertNotContains(response, book1.title)

class BookReviewTestCase(TestCase):

  def test_add_review(self):
    book = Book.objects.create( title='book1', description = 'description1', isbn='1231' )
    user = CustomUser.objects.create(
      username = 'shahboz',
      first_name = 'shahboz',
      last_name = 'shirinboyev',
      email = 'shahboz.sh.b@gmail.com'
    )
    user.set_password('thisispassword')
    user.save()
    self.client.login(username='shahboz', password='thisispassword')

    self.client.post(
      reverse("books:reviews", kwargs={"id": book.id}),
      data={"stars_given": 3, "comment": "Nice book"}
    )
    book_reviews = book.bookreview_set.all()

    self.assertEqual(book_reviews.count(), 1)
    self.assertEqual(book_reviews[0].stars_given, 3)
    self.assertEqual(book_reviews[0].comment, "Nice book")
    self.assertEqual(book_reviews[0].book, book)
    self.assertEqual(book_reviews[0].user, user)