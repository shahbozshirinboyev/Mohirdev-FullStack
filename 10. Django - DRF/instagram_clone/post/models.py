from django.db import models
from shared.models import BaseModel
from django.db.models import UniqueConstraint
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MaxLengthValidator

User = get_user_model()

# Create your models here.
class Post(BaseModel):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  image = models.ImageField(upload_to='post_images', validators=[
    FileExtensionValidator(
      allowed_extensions=['jpeg', 'jpg', 'png']
    )
  ])
  caption = models.TextField(validators=[MaxLengthValidator(2000)])

  class Meta:
    db_table = 'posts'
    verbose_name = 'post'
    verbose_name_plural = 'posts'

  def __str__(self):
    return f"{self.author} -> {self.caption}"

class PostComment(BaseModel):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  comment = models.TextField()
  parent = models.ForeignKey(
    'self',
    on_delete=models.CASCADE,
    related_name='child',
    null=True,
    blank=True
  )

  class Meta:
    db_table = 'PostComment'
    verbose_name = 'PostComment'
    verbose_name_plural = 'PostComments'

  def __str__(self):
    return f"{self.author} -> {self.comment}"

class PostLike(BaseModel):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

  class Meta:
    constraints = [
      UniqueConstraint(
        fields=['author', 'post'],
        name='unique_author_post_like',
      )
    ]

  class Meta:
    db_table = 'PostLike'
    verbose_name = 'PostLike'
    verbose_name_plural = 'PostLikes'

class CommentLike(BaseModel):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name='likes')

  class Meta:
    constraints = [
      UniqueConstraint(
        fields=['author', 'comment'],
        name='unique_author_comment_like',
      )
    ]

  class Meta:
    db_table = 'CommentLike'
    verbose_name = 'CommentLike'
    verbose_name_plural = 'CommentLikes'