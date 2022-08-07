from django.shortcuts import redirect
from doctor.models import Doctor
class RegisterDoctorMixin():
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.applier or self.request.user.admin_applier:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class ConfirmDoctorMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_status == "ad" or self.request.user.user_status == "su" :
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class ConfirmDoctorPageMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_status == "ad" or self.request.user.user_status == "su" :
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class MessageMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_status == "do":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")