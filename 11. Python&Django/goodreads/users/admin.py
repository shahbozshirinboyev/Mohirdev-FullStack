from django.contrib import admin
from users.models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
  search_fields = ('username', 'first_name', 'last_name')
  list_display  = ['username', 'first_name', 'last_name', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
