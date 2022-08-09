from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid

from base.models import BaseUser
from doctor.models import Doctor
from admins.models import Admin
# Create your views here.


def homePage(request):
    return  render(request,"base-app/home.html")


class ProfileView(LoginRequiredMixin,DetailView):
    template_name = "base-app/profile.html"
    context_object_name = "user"

    def get_object(self, *args, **kwargs):
        object = get_object_or_404(BaseUser, id= self.kwargs["id"], email=self.kwargs['email'])
        return object

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = BaseUser.objects.filter(email= self.kwargs["email"], pk= self.kwargs["id"]).first()
        context['doctor_request'] = user.applier.filter(doctor_status = "re")
        context['admin_request'] = user.admin_applier.filter(admin_stat= "re")
        return context

def page_not_found(request, exception):
    return render(request, "base-app/404.html", {})

def server_error(request, exception=None):
    return render(request, "base-app/500.html", {})


