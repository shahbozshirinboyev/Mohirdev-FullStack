from books.models import BookReview
from api.serializers import BookReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookReviewDetailAPIView(APIView):
  permission_classes = [IsAuthenticated, ]

  def get(self, request, id):
    book_review = BookReview.objects.get(id=id)
    serializer = BookReviewSerializer(book_review)
    return Response(data=serializer.data)

class BookReviewListAPIView(APIView):
  permission_classes = [IsAuthenticated, ]

  def get(self, request):
    book_reviews = BookReview.objects.all().order_by('-created_at')
    serializer = BookReviewSerializer(book_reviews, many=True)
    return Response(data=serializer.data)