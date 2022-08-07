from django.shortcuts import redirect


class HospitalViewMixin():
    def dispatch(self,request,*args,**kwargs):
        if self.request.user.hospital_owner.count() == 0:
            return super().dispatch(request,*args,**kwargs)
        else:
            return redirect("base:home")


class ConfirmHospitalMixin():
    def dispatch(self,request,*args,**kwargs):
        if self.request.user.admin_stat == "ac":
            return super().dispatch(request,*args,**kwargs)
        else:
            return redirect("base:home")