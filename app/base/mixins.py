from django.shortcuts import redirect
from django.contrib import messages

class LoginMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.success(request,"you are already logged in!")
            return redirect("base:home")
        else:
            return super().dispatch(request, *args, **kwargs)