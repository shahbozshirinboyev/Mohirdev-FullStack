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

class PostCommentsListView(generics.ListAPIView):
  serializer_class = CommentSerializer
  permission_classes = [AllowAny, ]

  def get_queryset(self):
    post_id = self.kwargs['pk']
    queryset = PostComment.objects.filter(post__id=post_id)
    return queryset

class PostCommentsCreateView(generics.CreateAPIView):
  serializer_class = CommentSerializer
  permission_classes = [IsAuthenticated, ]

  def perform_create(self, serializer):
    post_id = self.kwargs['pk']
    serializer.save(author=self.request.user, post_id=post_id)
    return super().perform_create(serializer)

class CommentListCreateApiView(generics.ListCreateAPIView):
  serializer_class = CommentSerializer
  permission_classes = [IsAuthenticatedOrReadOnly, ]
  queryset = PostComment.objects.all()
  pagination_class = CustomPagination

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)