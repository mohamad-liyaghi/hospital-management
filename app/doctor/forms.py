from django import forms
from django.forms import ModelForm
from base.models import BaseUser
from hospital.models import Message

class RegisterDoctorForm(ModelForm):
    class Meta:
        model = BaseUser
        fields = ("doctor_id","hospital_to_request","more_info","doc_stat")


class MessageForm(ModelForm):
    hospital_id = forms.CharField()
    patient_id = forms.CharField()
    class Meta:
        model = Message
        fields = ("title","doctor","patient","to_hospital","description","token")
