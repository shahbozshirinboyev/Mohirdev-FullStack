from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from shared.custom_pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Post, PostComment, PostLike, CommentLike
from .serializers import PostSerializer, PostLikeSerializer, CommentSerializer, CommentLikeSerializer

# Create your views here.
class PostListApiView(generics.ListAPIView):
  serializer_class = PostSerializer
  permission_classes = [AllowAny, ] #IsAuthenticatedOrReadOnly - if login requiere
  pagination_class = CustomPagination

  def get_queryset(self):
    return Post.objects.all()

class PostCreateView(generics.CreateAPIView):
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticated, ]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    return super().perform_create(serializer)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticatedOrReadOnly, ]

  def put(self, request, *args, **kwargs):
    post = self.get_object()
    serializer = self.serializer_class(post, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
      {
        'success': True,
        'code': status.HTTP_200_OK,
        'message': 'Post successfully updated.',
        'data': serializer.data
      }
    )

  def delete(self, request, *args, **kwargs):
    post = self.get_object()
    post.delete()
    return Response(
      {
        'success': True,
        'code': status.HTTP_204_NO_CONTENT,
        'message': 'Post successfully deleted.'
      }
    )