from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
    path('admin/', admin.site.urls),
]
