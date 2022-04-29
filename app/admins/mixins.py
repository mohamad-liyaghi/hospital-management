from django.shortcuts import redirect
class RegisterAdminMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.admin_stat == "dr":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class ConfirmAdminPageMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.admin_stat == "ac":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")