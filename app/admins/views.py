from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from base.models import BaseUser
from admins.models import Admin
from .mixins import RegisterAdminMixin,ConfirmAdminPageMixin,ChangeAdminStatusMixin
from .forms import RegisterAdminForm
# Create your views here.

class RegisterAdminView(LoginRequiredMixin,RegisterAdminMixin,FormView):
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
    template_name = "admins/ConfirmAdmin.html"
    def get_queryset(self):
        object = Admin.objects.filter(admin_stat="re")
        return object


class AcceptAdminView(LoginRequiredMixin,DetailView):
    def get(self,request,username, *args, **kwargs):
        BaseUser.objects.filter(username=self.kwargs['username']).update(user_status = "ad")
        Admin.objects.filter(applier__username=self.kwargs['username']).update(admin_stat= "ac")
        return redirect("admins:confrim-admin-list")

class DeclineAdminView(LoginRequiredMixin,DetailView):
    def get(self,request,username, *args, **kwargs):
        BaseUser.objects.filter(username=self.kwargs['username']).update(user_status = "pa")
        Admin.objects.filter(applier__username=self.kwargs['username']).update(admin_stat= "de")
        return redirect("admins:confrim-admin-list")