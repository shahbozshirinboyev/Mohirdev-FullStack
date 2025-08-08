from rest_framework import serializers
from books.models import Book, BookReview
from users.models import CustomUser

class BookSerializer(serializers.ModelSerializer):

  class Meta:
    model = Book
    fields = ('id', 'title', 'description', 'isbn')

class UserSerialzer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ('id', 'username', 'first_name', 'last_name', 'email')

class BookReviewSerializer(serializers.ModelSerializer):

  user = UserSerialzer()
  book = BookSerializer()

  class Meta:
    model = BookReview
    fields = ('id', 'created_at', 'stars_given', 'comment', 'book', 'user')
