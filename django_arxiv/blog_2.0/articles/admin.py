from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
  model = Comment
  extra = 0 #qo'shimcha bo'sh joy uchun

class ArticleAdmin(admin.ModelAdmin):
  inlines = [CommentInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)