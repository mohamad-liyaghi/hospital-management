from django import forms
from django.forms import ModelForm
from .models import Hospital

class RegisterHospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ("name","address","picture","hospital_id","phone_number","status","owner","description",)
        help_texts= {
            "name" : "Hospital's name",
            "address": "Hospital's address",
            "picture" : "Hospital's picture",
            "hospital_id" : "Unique hospital id",
            "phone_number":"hospital's phone number",
            "description" : "Tell us about hospital, hospitals owner and ...."
        }


