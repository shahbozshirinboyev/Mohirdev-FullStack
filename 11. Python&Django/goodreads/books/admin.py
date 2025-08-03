from django.contrib import admin
from books.models import Book, Author, BookAuthor, BookReview

class BookAdmin(admin.ModelAdmin):
  search_fields = ('title', 'isbn')
  list_display = ('title', 'isbn', 'description')

class AuthorAdmin(admin.ModelAdmin):
  search_fields = ('first_name', 'last_name')
  list_display = ('first_name', 'last_name', 'email', 'bio')

class BookAuthorAdmin(admin.ModelAdmin):
  search_fields = ('book', 'author')
  list_display = ('book', 'author')

class BookReviewAdmin(admin.ModelAdmin):
  search_fields = ('user', 'book', 'stars_given')
  list_display = ('user', 'book', 'stars_given', 'comment')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)