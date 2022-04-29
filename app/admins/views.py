from django.shortcuts import render,redirect
from django.views.generic import FormView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from base.models import BaseUser
from .mixins import RegisterAdminMixin,ConfirmAdminPageMixin
from .forms import RegisterAdminForm
# Create your views here.

class RegisterAdminView(LoginRequiredMixin,RegisterAdminMixin,FormView):
    form_class = RegisterAdminForm
    template_name = "admins/RegisterAdmin.html"
    def form_valid(self, form):
        user = BaseUser.objects.filter(username=self.request.user.username)
        form = form.save(commit=False)
        user.update(
            admin_stat="re",
            admin_description=form.admin_description
        )
        messages.success(self.request, "request has been sent, please wait for results.")
        return redirect("base:home")
    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong please try again later")
        return redirect("base:home")


class ConfirmAdminListView(LoginRequiredMixin,ConfirmAdminPageMixin, ListView):
    template_name = "admins/ConfirmAdmin.html"
    def get_queryset(self):
        object = BaseUser.objects.filter(admin_stat="re")
        return object