from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction

import uuid

from base.models import BaseUser
from doctor.models import Doctor
from hospital.models import Hospital,Message
from .forms import RegisterDoctorForm,MessageForm
from .mixins import RegisterDoctorMixin,ConfirmDoctorMixin, ConfirmDoctorPageMixin ,MessageMixin

# Create your views here.
class RegisterDoctorView(LoginRequiredMixin,RegisterDoctorMixin,FormView):
    form_class = RegisterDoctorForm
    template_name = "doctor/RegisterDoctor.html"
    @transaction.atomic
    def form_valid(self, form):
        hospital_token = self.request.POST["hospital_token"]
        form = form.save(commit=False)
        form.applier = self.request.user
        for hospital in Hospital.objects.filter(hospital_id=hospital_token):
            form.hospital_to_request = hospital
        form.doctor_status = "re"
        form.save()
        messages.success(self.request, "request has been sent, please wait for results.")
        return redirect("base:home")
    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong please try again later")
        return redirect("base:home")


class ConfirmDoctorListView(LoginRequiredMixin,ConfirmDoctorPageMixin, ListView):
    template_name = "doctor/ConfirmDoctor.html"
    def get_queryset(self):
        object = Doctor.objects.filter(doctor_status="re")
        return object

class AcceptDoctorView(LoginRequiredMixin,ConfirmDoctorMixin,DetailView):
    def get(self,request, *args, **kwargs):
        Doctor.objects.filter(applier__username=self.kwargs['username']).update(doctor_status="ac")
        BaseUser.objects.filter(username=self.kwargs['username']).update(user_status="do")
        return redirect("doctor:confirm-doctor-page")

class DeclineDoctorView(LoginRequiredMixin,ConfirmDoctorMixin,DetailView):
    def get(self,request,username, *args, **kwargs):
        Doctor.objects.filter(applier__username=self.kwargs['username']).update(doctor_status="de")
        BaseUser.objects.filter(username=self.kwargs['username']).update(user_status="pa")
        return redirect("doctor:confirm-doctor-page")


class SendMessage(LoginRequiredMixin,MessageMixin,FormView):
    form_class = MessageForm
    template_name = "doctor/AddMessage.html"
    @transaction.atomic()
    def form_valid(self, form):
        patient_id =self.request.POST["patient_id"]
        hospital_id = self.request.POST["hospital_id"]
        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:10]
        form.doctor = self.request.user
        user = BaseUser.objects.filter(user_id=patient_id)
        for patient in  user:
            form.patient = patient
        for hospital in Hospital.objects.filter(hospital_id=hospital_id):
            form.to_hospital  = hospital
        form.save()
        messages.success(self.request, "message sent.")
        return redirect("base:home")
    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong...")


class UnreadMessageList(LoginRequiredMixin,MessageMixin,ListView):
    template_name = "doctor/MessageList.html"
    def get_queryset(self):
        object = Message.objects.filter(to_hospital=self.request.user.hospital_to_request
                                        ,status=["s","r"])
        return object

class AllMessageList(LoginRequiredMixin,MessageMixin,ListView):
    template_name = "doctor/MessageList.html"
    def get_queryset(self):
        object = Message.objects.filter(to_hospital=self.request.user.hospital_to_request)
        return object

class MessageDetail(LoginRequiredMixin,MessageMixin,DetailView):
    template_name = "doctor/MessageDetail.html"
    def get_object(self,*args,**kwargs):
        return  get_object_or_404(
            Message,
            token = self.kwargs['token']
        )

class ReadMessageStatus(LoginRequiredMixin,MessageMixin,DetailView):
    def get(self,*args, **kwargs):
        object = Message.objects.filter(token=self.kwargs['token'])
        object.update(status="r")
        return redirect("doctor:messages")

class CloseMessageStatus(LoginRequiredMixin,MessageMixin,DetailView):
    def get(self,*args, **kwargs):
        object = Message.objects.filter(token=self.kwargs['token'])
        object.update(status="c")
