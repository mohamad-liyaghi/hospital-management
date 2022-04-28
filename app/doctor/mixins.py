from django.shortcuts import redirect
class RegisterDoctorMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.doc_stat == "dr":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")