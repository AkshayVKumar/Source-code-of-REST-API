from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
# Register your models here.
class AdminUserProfile(ModelAdmin):
    list_display=('email','name','is_active','is_staff','is_superuser')
admin.site.register(UserProfile,AdminUserProfile)
