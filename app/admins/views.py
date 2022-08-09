from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from base.models import BaseUser
from admins.models import Admin
from .mixins import RegisterAdminMixin, ConfirmAdminPageMixin, ChangeAdminPageMixin
from .forms import RegisterAdminForm


class RegisterAdminView(LoginRequiredMixin,RegisterAdminMixin,FormView):
    '''Register an admin'''
    form_class = RegisterAdminForm
    template_name = "admins/RegisterAdmin.html"
    def form_valid(self, form):
        form = form.save(commit= False)        
        form.applier = self.request.user
        form.admin_stat = "re"
        form.save()
        messages.success(self.request, "request has been sent, please wait for results.")
        return redirect("base:home")

    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong please try again later")
        return redirect("base:home")


class ConfirmAdminListView(LoginRequiredMixin,ConfirmAdminPageMixin, ListView):
    '''List of admin requests'''
    template_name = "admins/ConfirmAdmin.html"
    def get_queryset(self):
        object = Admin.objects.filter(admin_stat="re")
        return object


class AcceptAdminView(LoginRequiredMixin, ChangeAdminPageMixin, DetailView):
    '''Accept an admin request'''
    def get(self,request, email, *args, **kwargs):
        user = get_object_or_404(BaseUser, email= self.kwargs["email"])
        admin = get_object_or_404(Admin, applier__email= self.kwargs["email"])

        user.user_stat = "ad"
        admin.admin_stat = "ac"

        user.save()
        admin.save()
        return redirect("admins:confrim-admin-list")

class DeclineAdminView(LoginRequiredMixin, ChangeAdminPageMixin, DetailView):
    ''' Decline an admin reques '''
    def get(self,request,username, *args, **kwargs):
        user = get_object_or_404(BaseUser, email=self.kwargs["email"])
        admin = get_object_or_404(Admin, applier__email=self.kwargs["email"])

        user.user_stat = "pa"
        admin.admin_stat = "de"

        user.save()
        admin.save()
        return redirect("admins:confrim-admin-list")