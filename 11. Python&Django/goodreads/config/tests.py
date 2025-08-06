from django.test import TestCase
from books.models import Book, BookReview
from django.urls import reverse
from users.models import CustomUser

class HomePageTestCase(TestCase):
  def test_paginated_list(self):
    book1 = Book.objects.create( title='book1', description = 'description1', isbn='1231' )
    book2 = Book.objects.create( title='book2', description = 'description2', isbn='1232' )
    book3 = Book.objects.create( title='book3', description = 'description3', isbn='1233' )

    user = CustomUser.objects.create(
      username = 'shahboz',
      first_name = 'shahboz',
      last_name = 'shirinboyev',
      email = 'shahboz.sh.b@gmail.com'
    )
    user.set_password('thisispassword')
    user.save()

    self.client.login(username='shahboz', password='thisispassword')
    review1 = BookReview.objects.create(book=book1, user=user, stars_given=1, comment="Very good book 1")
    review2 = BookReview.objects.create(book=book2, user=user, stars_given=2, comment="Very good book 2")
    review3 = BookReview.objects.create(book=book3, user=user, stars_given=3, comment="Very good book 3")

    response = self.client.get(reverse('home')+ '?page_size=2')

    self.assertNotContains(response, review1.comment)
    self.assertContains(response, review2.comment)
    self.assertContains(response, review3.comment)
