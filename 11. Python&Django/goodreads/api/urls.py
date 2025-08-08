from django.urls import path
from api.views import BookReviewDetailAPIView, BookListAPIView

app_name = 'api'
urlpatterns = [
    path('reviews/', BookListAPIView.as_view(), name="book-list-reviews"),
    path('reviews/<int:id>/', BookReviewDetailAPIView.as_view(), name="book-detail-review"),
]