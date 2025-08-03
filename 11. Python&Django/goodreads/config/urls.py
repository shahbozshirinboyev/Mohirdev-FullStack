from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('users/', include('users.urls'), name='users'),

    path('admin/', admin.site.urls),
]
