from django.contrib import admin
from admins.models import Admin

class AdminModel(admin.ModelAdmin):
    list_display = ("applier", "admin_stat")
    readonly_fields = ("applier", "admin_stat", "admin_description")


admin.site.register(Admin, AdminModel)