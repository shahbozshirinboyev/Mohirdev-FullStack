# from django.urls import path
# from api.views import BookReviewDetailAPIView, BookReviewListAPIView

# app_name = 'api'
# urlpatterns = [
#     path('reviews/', BookReviewListAPIView.as_view(), name="book-reviews-list"),
#     path('reviews/<int:id>/', BookReviewDetailAPIView.as_view(), name="book-detail-review"),
# ]

from rest_framework.routers import DefaultRouter
from api.views import BookReviewsViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'reviews', BookReviewsViewSet, basename='reviews')
urlpatterns = router.urls