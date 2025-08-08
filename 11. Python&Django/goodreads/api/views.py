from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from books.models import BookReview

# Create your views here.
class BookReviewDetailAPIView(View):
  def get(self, request, id):
    book_review = BookReview.objects.get(id=id)
    json_response = {
      "id": book_review.id,
      "stars_given": book_review.stars_given,
      "comment": book_review.comment,
      "book": {
        "id": book_review.book.id,
        "title": book_review.book.title,
        "description": book_review.book.description,
        "isbn": book_review.book.isbn
      },
      "user": {
        "id": book_review.user.id,
        "username": book_review.user.username,
        "first_name": book_review.user.first_name,
        "last_name": book_review.user.last_name,
        "avatar": book_review.user.avatar.url
      }
    }
    return JsonResponse(json_response)
