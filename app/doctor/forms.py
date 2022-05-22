from django import forms
from django.forms import ModelForm
from doctor.models import Doctor
from hospital.models import Message

class RegisterDoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ("applier","doctor_id","hospital_to_request","more_info","doctor_status")


class MessageForm(ModelForm):
    hospital_id = forms.CharField()
    patient_id = forms.CharField()
    class Meta:
        model = Message
        fields = ("title","doctor","patient","to_hospital","description","token")
