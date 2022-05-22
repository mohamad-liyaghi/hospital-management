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

class loginPage(LoginMixin,LoginView):
    template_name = "base-app/authentication/login.html"
    def get_success_url(self):
        messages.success(self.request,"you are now logged in")
        return reverse_lazy('base:home')

class registerPage(LoginMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'base-app/authentication/register.html'
    @transaction.atomic
    def form_valid(self, form):
        user = self.form_class(self.request.POST, self.request.FILES)
        user = user.save(commit=False)
        user.username = user.first_name+user.last_name+uuid.uuid4().hex.upper()[0:4]
        user.token = uuid.uuid4().hex.upper()[0:15]
        user.save()
        messages.success(self.request, "you are now registered")
        return redirect('base:home')
    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong, please try again")


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "you were logged out!")
        return redirect('base:home')
    else:
        return redirect('base:login')


class ProfileView(LoginRequiredMixin,DetailView):
    template_name = "base-app/other/profile.html"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(BaseUser,username=self.kwargs['username'])
        return object
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['doctor_request'] = Doctor.objects.filter(applier=BaseUser.objects.filter(username=self.kwargs['username'])[0], doctor_status="re")
        context['admin_request'] = Admin.objects.filter(applier=BaseUser.objects.filter(username=self.kwargs['username'])[0], admin_stat="re")
        return context

def page_not_found(request, exception):
    return render(request, "base-app/404.html", {})

def server_error(request, exception=None):
    return render(request, "base-app/other/500.html", {})


