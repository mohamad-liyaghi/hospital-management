from django.shortcuts import redirect
from admins.models import Admin

class RegisterAdminMixin():
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.applier or self.request.user.admin_applier:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class ConfirmAdminPageMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.user_status == "ad" or self.request.user.user_status == "su":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class ChangeAdminPageMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.user_status == "ad" and\
                Admin.objects.filter(applier__email=self.kwargs.get["email"], admin_stat="re"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")