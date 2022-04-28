from django.forms import ModelForm
from  base.models import BaseUser

class RegisterAdminForm(ModelForm):
    class Meta:
        model = BaseUser
        fields = ("admin_stat","admin_description")
        help_texts ={
            "admin_description" : "tell us about yourself and why u wanna become admin"
        }