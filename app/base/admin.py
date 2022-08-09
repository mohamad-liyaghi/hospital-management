from django.contrib import admin
from .models import BaseUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "user_id", "user_status")
    readonly_fields = ("last_login", "password", "is_staff", "is_superuser", "date_joined", "user_status", "user_id")

admin.site.register(BaseUser, UserAdmin)

