from django import forms
from  django.contrib.auth.forms import UserCreationForm
from base.models import BaseUser

import random

class RegisterUserForm(UserCreationForm):
    token = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model = BaseUser
        fields = ('first_name','last_name','email','picture','birthday','description','user_id', "token")
        help_texts = {
            'first_name': "Enter your first name",
            'last_name' : "Enter your last name",
            "birthday" : "Enter your date of birth format yyyy-mm-dd",
            "description" : "Enter extra notes such as disease ",
            "user_id" : "Enter your id",
        }

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.token = random.randint(1, 99999999999999)
        if commit:
            user.save()

        return user