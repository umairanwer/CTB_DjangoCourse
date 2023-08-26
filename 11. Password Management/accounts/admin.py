from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email')
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)