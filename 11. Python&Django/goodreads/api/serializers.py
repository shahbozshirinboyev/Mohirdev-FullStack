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

  user = UserSerialzer(read_only=True)
  book = BookSerializer(read_only=True)

  user_id = serializers.IntegerField(write_only=True)
  book_id = serializers.IntegerField(write_only=True)

  class Meta:
    model = BookReview
    fields = ('id', 'created_at', 'stars_given', 'comment', 'book', 'user', "user_id", "book_id")
