from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("applier", "doctor_id", "hospital_to_request", "doctor_status")


admin.site.register(Doctor, DoctorAdmin)