from django.forms import ModelForm
from base.models import BaseUser

class RegisterDoctorForm(ModelForm):
    class Meta:
        model = BaseUser
        fields = ("doctor_id","hospital_to_request","more_info","doc_stat")