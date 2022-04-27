from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.db import transaction


import uuid

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
        user.username = uuid.uuid4().hex.upper()[0:30]
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