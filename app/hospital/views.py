from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView ,ListView, DetailView
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Hospital
from base.models import BaseUser
from .forms import RegisterHospitalForm
from .mixins import ConfirmHospitalMixin, HospitalViewMixin
# Create your views here.

class RegisterHospitalView(LoginRequiredMixin, HospitalViewMixin,FormView):
    '''Register a Hospital'''
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
    '''List of hospital requests'''
    template_name = "hospital/ConfirmHospital.html"
    def get_queryset(self):
        object = Hospital.objects.filter(status="n")
        return object


class HospitalProfileView(LoginRequiredMixin,DetailView):
    '''Hospital profile page'''
    template_name = "hospital/HospitalProfile.html"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(Hospital,hospital_id=self.kwargs['id'])
        return object


class AcceptHospitalView(LoginRequiredMixin,ConfirmHospitalMixin,DetailView):
    def get(self,request, *args, **kwargs):
        id = self.kwargs['id']
        hospital_id = self.kwargs["hospital_id"]

        hospital = get_object_or_404(Hospital, id= id, hospital_id=hospital_id)

        hospital.status = "a"
        hospital.save()
        return redirect("hospital:hospital-confirm-list")

class DeclineHospitalView(LoginRequiredMixin,ConfirmHospitalMixin,DetailView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs['id']
        hospital_id = self.kwargs["hospital_id"]

        hospital = get_object_or_404(Hospital, id= id, hospital_id=hospital_id)

        hospital.status = "r"
        hospital.save()
        return redirect("hospital:hospital-confirm-list")

