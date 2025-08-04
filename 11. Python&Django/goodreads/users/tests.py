from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.urls import reverse

# Create your tests here.
class RegistrationTestCase(TestCase):
  def test_user_account_is_created(self):
    self.client.post(
      # '/users/register/',
      reverse("users:register"), # /users/register/
      data = {
        'username':'jahongir',
        'first_name': 'Jahongitr',
        'last_name':'Rahmanov',
        'email': 'jrahmanov@gmail.com',
        'password': 'jrahmanov@'
        }
    )
    user = User.objects.get(username="jahongir")
    self.assertEqual(user.first_name, "Jahongitr")
    self.assertEqual(user.last_name, "Rahmanov")
    self.assertEqual(user.email, "jrahmanov@gmail.com")
    self.assertNotEqual(user.password, "jrahmanov@")
    self.assertTrue(user.check_password('jrahmanov@'))

  def test_required_fields(self):
    response = self.client.post(
        reverse("users:register"),
        data={
            "first_name": "Jahongitr",
            "email": "jrahmanov@gmail.com"
        }
    )

    form = response.context.get("form")
    self.assertIsNotNone(form, "Form kontekstda mavjud emas!")
    user_count = User.objects.count()
    self.assertEqual(user_count, 0)

    self.assertFormError(form, "username", "This field is required.")
    self.assertFormError(form, "password", "This field is required.")

  def test_invalid_email(self):
     response = self.client.post(
      # '/users/register/',
      reverse("users:register"), # /users/register/
      data = {
        'username':'jahongir',
        'first_name': 'Jahongitr',
        'last_name':'Rahmanov',
        'email': 'jrahmanovgmail.com',
        'password': 'jrahmanov@'
        }
    )
     user_count = User.objects.count()
     self.assertEqual(user_count, 0)
     form = response.context.get("form")
     self.assertFormError(form, "email", "Enter a valid email address.")

  # XATOLIK BOR ---------------------------------------------------------------------------------------
  # def test_unique_username(self):
  #   # 1. create a user
  #   user = User.objects.create(username="jahongirname", first_name="Jagongir")
  #   user.set_password("somepas2ws")
  #   user.save()
  #   # 2. try to create another user with that same username
  #   response = self.client.post(
  #     reverse("users:register"), # /users/register/
  #     data = {
  #       'username':'jahongirname',
  #       'first_name': 'Jahongitr123',
  #       'last_name':'Rahmanov1123',
  #       'email': 'jrahmanov123@gmail.com',
  #       'password': 'jrahmanov@123'
  #       }
  #   )
  #   # 3. check that the second user was not created
  #   self.assertEqual(User.objects.count(), 1)
  #   # 4. check that the form contains the error message
  #   form = response.context.get("form")
  #   self.assertFormError(form, "username", "A user with that username already exists.")
  # XATOLIK BOR ---------------------------------------------------------------------------------------

class LoginTestCase(TestCase):

  def test_successful_login(self):
    db_user  = User.objects.create(username='jahongir', first_name='jahongir', last_name='umarov')
    db_user.set_password('thisispassword')
    db_user.save()

    self.client.post(
      reverse('users:login'),
      data={
        'username': 'jahongir',
        'password': 'thisispassword'
      }
    )
    user = get_user(self.client)
    self.assertTrue(user.is_authenticated)

  def test_wrong_credentials(self):
    db_user  = User.objects.create(username='jahongir', first_name='jahongir', last_name='umarov')
    db_user.set_password('thisispassword')
    db_user.save()

    self.client.post(
      reverse('users:login'),
      data={
        'username': 'jahongir1',
        'password': 'thisispassword1'
      }
    )
    user = get_user(self.client)
    self.assertFalse(user.is_authenticated)

    self.client.post(
      reverse('users:login'),
      data={
        'username': 'jahongir',
        'password': 'thisispassword1'
      }
    )
    user = get_user(self.client)
    self.assertFalse(user.is_authenticated)

class ProfileTestCase(TestCase):
  def test_login_required(self):
    response = self.client.get(reverse('users:profile'))
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response.url, reverse('users:login') + "?next=/users/profile/")

  def test_profile_details(self):
    user = User.objects.create(
      username = 'shahboz',
      first_name = 'shahboz',
      last_name = 'shirinboyev',
      email = 'shahboz.sh.b@gmail.com'
    )
    user.set_password('thisispassword')
    user.save()

    self.client.login(username='shahboz', password='thisispassword')

    response = self.client.get(reverse("users:profile"))
    self.assertAlmostEqual(response.status_code, 200)

    self.assertContains(response, user.username)
    self.assertContains(response, user.first_name)
    self.assertContains(response, user.last_name)
    self.assertContains(response, user.email)
