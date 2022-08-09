from django.contrib import admin
from .models import Hospital,Message

class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital_id", "status", "owner")
    readonly_fields = ("name", "hospital_id", "status", "owner", "address")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("title","doctor", "to_hospital" ,"status")
    readonly_fields = ("title","doctor", "to_hospital" ,"status", "token", "patient", "description")



admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Message, MessageAdmin)