from django.shortcuts import redirect
class RegisterAdminMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.admin_stat == "dr" and request.user.doc_stat != "ac" or "re":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")

class ConfirmAdminPageMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.admin_stat == "ac":
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")


class ChangeAdminStatusMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.admin_stat == "ac" and add_admin == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("base:home")