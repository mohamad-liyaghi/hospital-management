from django.shortcuts import render,redirect
from django.views.generic import FormView,ListView
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import BaseUser

from .models import Hospital
from .forms import RegisterHospitalForm
from .mixins import ConfirmHospitalMixin
# Create your views here.

class RegisterHospitalView(LoginRequiredMixin,FormView):
    form_class = RegisterHospitalForm
    template_name = "hospital/Register_hospital.html"
    @transaction.atomic
    def form_valid(self, form):
        hospital = self.form_class(self.request.POST, self.request.FILES)
        hospital = hospital.save(commit=False)
        hospital.owner = self.request.user
        hospital.status = "n"
        hospital.save()
        messages.success(self.request,"request has been sent, please wait for results.")
        return redirect("base:home")
    def form_invalid(self, form):
        print(form.errors)
        messages.success(self.request, "sth went wrong, please try again later")
        return redirect("base:home")




class ConfirmHospitalListView(LoginRequiredMixin,ConfirmHospitalMixin, ListView):
    template_name = "hospital/ConfirmHospital.html"
    def get_queryset(self):
        object = Hospital.objects.filter(status="n")
        return object