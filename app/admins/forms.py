from django.forms import ModelForm
from  admins.models import Admin

class RegisterAdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = ("applier","admin_stat","admin_description")
