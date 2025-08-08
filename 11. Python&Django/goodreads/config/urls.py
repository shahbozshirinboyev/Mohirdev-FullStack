from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import index, home_page

urlpatterns = [
    path('', index, name="index"),
    path('home/', home_page, name="home"),
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)