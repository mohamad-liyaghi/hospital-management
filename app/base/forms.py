from django import forms
from  django.contrib.auth.forms import UserCreationForm
from base.models import BaseUser

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('first_name','last_name','email','picture','birthday','description','user_id')
        help_texts = {
            'first_name': "Enter your first name",
            'last_name' : "Enter your last name",
            "birthday" : "Enter your date of birth format yyyy-mm-dd",
            "description" : "Enter extra notes such as disease ",
            "user_id" : "Enter your id",

        }

