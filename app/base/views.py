from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.db import transaction


import uuid

from base.models import BaseUser
from doctor.models import Doctor
from admins.models import Admin
from .mixins import LoginMixin
from .forms import RegisterUserForm
# Create your views here.


def homePage(request):
    return  render(request,"base-app/other/home.html")



class ProfileView(LoginRequiredMixin,DetailView):
    template_name = "base-app/other/profile.html"
    context_object_name = "user"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(BaseUser, id= self.kwargs["id"], email=self.kwargs['email'])
        return object
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['doctor_request'] = self.request.user.applier.filter(doctor_status = "re")
        context['admin_request'] = self.request.user.admin_applier.filter(admin_stat= "re")
        return context

def page_not_found(request, exception):
    return render(request, "base-app/404.html", {})

def server_error(request, exception=None):
    return render(request, "base-app/other/500.html", {})


