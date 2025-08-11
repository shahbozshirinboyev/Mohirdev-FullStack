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

    self.client.login(username='jahongir', password='thisispassword')

  def test_book_review_detail(self):
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')
    br = BookReview.objects.create(book=book, user=self.user, stars_given='1', comment='comment1')

    response = self.client.get(reverse('api:reviews-detail', kwargs={'id': br.id}))

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

  def test_delete_review(self):
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')
    br = BookReview.objects.create(book=book, user=self.user, stars_given='1', comment='comment1')

    response = self.client.delete(reverse('api:reviews-detail', kwargs={'id': br.id}))

    self.assertEqual(response.status_code, 204)
    self.assertFalse(BookReview.objects.filter(id=br.id).exists())

  def test_patch_review(self):
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')
    br = BookReview.objects.create(book=book, user=self.user, stars_given='1', comment='comment1')

    response = self.client.patch(
      reverse('api:reviews-detail', kwargs={'id': br.id}),
      data={'stars_given': 4}
      )
    br.refresh_from_db()

    self.assertEqual(response.status_code, 200)
    self.assertEqual(br.stars_given, 4)

  def test_put_review(self):
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')
    br = BookReview.objects.create(book=book, user=self.user, stars_given='1', comment='comment1')

    response = self.client.put(
      reverse('api:reviews-detail', kwargs={'id': br.id}),
      data={"stars_given": 4, "comment": "Very good book", "user_id": self.user.id, "book_id": book.id}
      )
    br.refresh_from_db()

    self.assertEqual(response.status_code, 200)
    self.assertEqual(br.stars_given, 4)
    self.assertEqual(br.comment, "Very good book")

  def test_create_review(self):
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')

    data = {
      'stars_given': 2,
      'comment': 'bad book',
      'user_id': self.user.id,
      'book_id': book.id
    }

    response = self.client.post(reverse('api:reviews-list'), data=data)
    br = BookReview.objects.get(book=book)

    self.assertEqual(response.status_code, 201)
    self.assertEqual(br.stars_given, 2)
    self.assertEqual(br.comment, "bad book")


  def test_book_review_list(self):
    user_two = CustomUser.objects.create(username='jahongir2', first_name='jahongir2', last_name='umarov2')
    book = Book.objects.create(title='book1', description='description1', isbn='123456789')
    br = BookReview.objects.create(book=book, user=self.user, stars_given=1, comment='comment1')
    br_two = BookReview.objects.create(book=book, user=user_two, stars_given=2, comment='comment2')

    response = self.client.get(reverse('api:reviews-list'))

    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data['results']), 2)
    self.assertEqual(response.data['count'], 2)
    self.assertIn('next', response.data)
    self.assertIn('previous', response.data)

    self.assertEqual(response.data['results'][0]['id'], br_two.id)
    self.assertEqual(response.data['results'][0]['stars_given'], br_two.stars_given)
    self.assertEqual(response.data['results'][0]['comment'], br_two.comment)
    self.assertEqual(response.data['results'][1]['id'], br.id)
    self.assertEqual(response.data['results'][1]['stars_given'], br.stars_given)
    self.assertEqual(response.data['results'][1]['comment'], br.comment)