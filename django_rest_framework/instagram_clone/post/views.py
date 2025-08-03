from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from shared.custom_pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Post, PostComment, PostLike, CommentLike
from .serializers import PostSerializer, PostLikeSerializer, CommentSerializer, \
                        CommentLikeSerializer, LikeSerializer

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

class CommentRetrieveView(generics.RetrieveAPIView):
  serializer_class = CommentSerializer
  permission_classes = [AllowAny, ]
  queryset = PostComment.objects.all()

class PostLikeListView(generics.ListAPIView):
  serializer_class = PostLikeSerializer
  permission_classes = [AllowAny, ]

  def get_queryset(self):
    post_id = self.kwargs['pk']
    return PostLike.objects.filter(post_id=post_id)

class CommentLikeListView(generics.ListAPIView):
  serializer_class = CommentLikeSerializer
  permission_classes = [AllowAny, ]

  def get_queryset(self):
    comment_id = self.kwargs['pk']
    return CommentLike.objects.filter(comment_id=comment_id)

class LikesListView(generics.ListAPIView):
  serializer_class = LikeSerializer
  permission_classes = [IsAuthenticated, ]
  pagination_class = CustomPagination

  def get_queryset(self):
      user = self.request.user
      post_likes = PostLike.objects.filter(author=user)
      comment_likes = CommentLike.objects.filter(author=user)

      for like in post_likes:
          like.type = 'post'
      for like in comment_likes:
          like.type = 'comment'

      all_likes = list(post_likes) + list(comment_likes)
      all_likes = sorted(all_likes, key=lambda x: x.created_time, reverse=True)
      return all_likes

class LikeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        post_id = request.data.get("post_id")
        comment_id = request.data.get("comment_id")

        if post_id:
            try:
                post = Post.objects.get(id=post_id)
                like, created = PostLike.objects.get_or_create(post=post, author=user)
                if created:
                    return Response({"message": "Postga like qo‘shildi"}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "Postga allaqachon like bosilgan"}, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({"error": "Post topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        elif comment_id:
            try:
                comment = PostComment.objects.get(id=comment_id)
                like, created = CommentLike.objects.get_or_create(comment=comment, author=user)
                if created:
                    return Response({"message": "Kommentga like qo‘shildi"}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "Kommentga allaqachon like bosilgan"}, status=status.HTTP_200_OK)
            except PostComment.DoesNotExist:
                return Response({"error": "Komment topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "post_id yoki comment_id yuboring"}, status=status.HTTP_400_BAD_REQUEST)

class LikeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        post_id = request.data.get("post_id")
        comment_id = request.data.get("comment_id")

        if post_id:
            deleted, _ = PostLike.objects.filter(post_id=post_id, author=user).delete()
            if deleted:
                return Response({"message": "Post layki olib tashlandi"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Postga bosilgan layk topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        elif comment_id:
            deleted, _ = CommentLike.objects.filter(comment_id=comment_id, author=user).delete()
            if deleted:
                return Response({"message": "Komment layki olib tashlandi"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Kommentga bosilgan layk topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "post_id yoki comment_id yuboring"}, status=status.HTTP_400_BAD_REQUEST)


class PostLikeApiView(APIView):

   def post(self, request, pk):
      try:
         post_like = PostLike.objects.get(author=self.request.user, post_id=pk)
         post_like.delete()
         data = {
            'success': True,
            'message': "Postdan layk muvafaqqiyatli o'chirildi."
         }
         return Response(data, status=status.HTTP_204_NO_CONTENT)

      except PostLike.DoesNotExist:
         post_like = PostLike.objects.create(author=self.request.user, post_id=pk)
         serializer = PostLikeSerializer(post_like)
         data = {
            'success': True,
            'message': "Postga layk muvafaqqiyatli qo'shildi.",
            'data': serializer.data
         }
         return Response(data, status=status.HTTP_201_CREATED)

class CommentLikeApiView(APIView):

   def post(self, request, pk):
      try:
         comment_like = CommentLike.objects.get(
            author = self.request.user,
            comment_id = pk
         )
         comment_like.delete()
         data = {
            'success': True,
            'message': "Commentda layk muvafaqqiyatli o'chirildi.",
         }
         return Response(data, status=status.HTTP_204_NO_CONTENT)
      except CommentLike.DoesNotExist:
         comment_like = CommentLike.objects.create(author=self.request.user, comment_id=pk)
         serializer = CommentLikeSerializer(comment_like)
         data = {
            'success': False,
            'message': "Commentga layk muvafaqqiyatli qo'shildi.",
            'data': serializer.data
         }
         return Response(data, status=status.HTTP_201_CREATED)