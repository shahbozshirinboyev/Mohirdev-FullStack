"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
  openapi.Info(
    title="Book List Api",
    default_version='v1',
    description='Library demo project',
    terms_of_service='demo.com',
    contact=openapi.Contact(email='shahboz.sh.b@gmail.com'),
    license=openapi.License(name='demo licence')
  ),
  public=True,
  permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

    # ReDoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]

