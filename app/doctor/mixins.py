from django.shortcuts import redirect

class RegisterDoctorMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.doc_stat == "dr":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class ConfirmDoctorMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.admin_stat == "ac" and add_doctor == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")


class MessageMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.doc_stat == "ac":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")