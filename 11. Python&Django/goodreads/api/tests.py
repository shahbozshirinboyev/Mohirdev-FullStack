from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from users.models import CustomUser
from books.models import Book, BookReview

# Create your tests here.
class BookReviewDetailAPITestCase(APITestCase):

  def setUp(self):
    # DRY - Don't repeat yourself
    self.user  = CustomUser.objects.create(username='jahongir', first_name='jahongir', last_name='umarov')
    self.user.set_password('thisispassword')
    self.user.save()

  def test_book_review_detail(self):
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')
    br = BookReview.objects.create(book=book, user=self.user, stars_given='1', comment='comment1')

    response = self.client.get(reverse('api:book-detail-review', kwargs={'id': br.id}))

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['id'], br.id)
    self.assertEqual(response.data['stars_given'], 1)
    self.assertEqual(response.data['comment'], 'comment1')

    self.assertEqual(response.data['book']['id'], br.book.id)
    self.assertEqual(response.data['book']['title'], 'book1')
    self.assertEqual(response.data['book']['description'], 'description1')
    self.assertEqual(response.data['book']['isbn'], '123456789')

    self.assertEqual(response.data['user']['id'], self.user.id)
    self.assertEqual(response.data['user']['username'], 'jahongir')
    self.assertEqual(response.data['user']['first_name'], 'jahongir')
    self.assertEqual(response.data['user']['last_name'], 'umarov')

  def test_book_review_list(self):
    user_two = CustomUser.objects.create(username='jahongir2', first_name='jahongir2', last_name='umarov2')
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')
    br = BookReview.objects.create(book=book, user=self.user, stars_given=1, comment='comment1')
    br_two = BookReview.objects.create(book=book, user=user_two, stars_given=2, comment='comment2')

    response = self.client.get(reverse('api:book-reviews-list'))

    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]['id'], br_two.id)
    self.assertEqual(response.data[0]['stars_given'], br_two.stars_given)
    self.assertEqual(response.data[0]['comment'], br_two.comment)
    self.assertEqual(response.data[1]['id'], br.id)
    self.assertEqual(response.data[1]['stars_given'], br.stars_given)
    self.assertEqual(response.data[1]['comment'], br.comment)