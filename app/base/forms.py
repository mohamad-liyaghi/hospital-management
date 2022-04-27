from django import forms
from  django.contrib.auth.forms import UserCreationForm
from base.models import BaseUser

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('username','first_name','last_name','email','picture','birthday','description','user_id','token', 'password1', 'password2')
        help_texts = {
            'username': None,
            'first_name': "Enter your first name",
            'last_name' : "Enter your last name",
            "birthday" : "Enter your date of birth format yyyy-mm-dd",
            "description" : "Enter extra notes such as disease ",
            "user_id" : "Enter your id",

        }
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = "Enter a valid password like: 4020TrKu (dont use this!)"
        self.fields['password2'].help_text = 'confirm your password'
