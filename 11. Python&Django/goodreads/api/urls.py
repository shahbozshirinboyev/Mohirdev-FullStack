from django.urls import path
from api.views import BookReviewDetailAPIView, BookReviewListAPIView

app_name = 'api'
urlpatterns = [
    path('reviews/', BookReviewListAPIView.as_view(), name="book-reviews-list"),
    path('reviews/<int:id>/', BookReviewDetailAPIView.as_view(), name="book-detail-review"),
]