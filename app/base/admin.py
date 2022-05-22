from django.contrib import admin
from .models import BaseUser, Admin, Doctor
# Register your models here.
admin.site.register(BaseUser)
admin.site.register(Admin)
admin.site.register(Doctor)