from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction

import uuid

from base.models import BaseUser
from doctor.models import Doctor
from hospital.models import Hospital, Message
from .forms import RegisterDoctorForm, MessageForm
from .mixins import RegisterDoctorMixin, ConfirmDoctorMixin, ConfirmDoctorPageMixin, MessageMixin

# Create your views here.
class RegisterDoctorView(LoginRequiredMixin,RegisterDoctorMixin,FormView):
    '''Register a doctor'''
    form_class = RegisterDoctorForm
    template_name = "doctor/RegisterDoctor.html"
    @transaction.atomic
    def form_valid(self, form):
        hospital_token = self.request.POST["hospital_token"]
        hospital = Hospital.objects.filter(hospital_id=hospital_token).first()

        form = form.save(commit=False)
        form.applier = self.request.user
        form.hospital_to_request = hospital
        form.doctor_status = "re"

        form.save()
        messages.success(self.request, "request has been sent, please wait for results.")
        return redirect("base:home")
    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong please try again later")
        return redirect("base:home")


class ConfirmDoctorListView(LoginRequiredMixin,ConfirmDoctorPageMixin, ListView):
    '''List of doctor requests'''
    template_name = "doctor/ConfirmDoctor.html"
    def get_queryset(self):
        object = Doctor.objects.filter(doctor_status="re")
        return object

class AcceptDoctorView(LoginRequiredMixin,ConfirmDoctorMixin,DetailView):
    '''Accept a doctor request'''
    def get(self,request, *args, **kwargs):
        doctor = get_object_or_404(Doctor, applier__email=self.kwargs['email'])
        user = get_object_or_404(BaseUser, email=self.kwargs['email'])

        doctor.doctor_status = "ac"
        user.user_status = "do"

        doctor.save()
        user.save()
        return redirect("doctor:confirm-doctor-page")

class DeclineDoctorView(LoginRequiredMixin,ConfirmDoctorMixin,DetailView):
    '''Decline a doctor request'''
    def get(self,request,username, *args, **kwargs):
        doctor = get_object_or_404(Doctor, applier__email=self.kwargs['email'])
        user = get_object_or_404(BaseUser, email=self.kwargs['email'])

        doctor.doctor_status = "de"
        user.user_status = "pa"

        doctor.save()
        user.save()
        return redirect("doctor:confirm-doctor-page")


class SendMessage(LoginRequiredMixin,MessageMixin,FormView):
    form_class = MessageForm
    template_name = "doctor/AddMessage.html"
    @transaction.atomic()
    def form_valid(self, form):
        patient_id =self.request.POST["patient_id"]
        hospital_id = self.request.POST["hospital_id"]

        patient = BaseUser.objects.filter(user_id=patient_id).first()
        hospital = Hospital.objects.filter(hospital_id=hospital_id).first()

        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:10]
        form.doctor = self.request.user
        form.patient = patient
        form.to_hospital  = hospital
        form.save()
        messages.success(self.request, "message sent.")
        return redirect("base:home")

    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong...")


class UnreadMessageList(LoginRequiredMixin,MessageMixin,ListView):
    template_name = "doctor/MessageList.html"
    def get_queryset(self):
        user = self.request.user.applier.first()
        object = Message.objects.filter(to_hospital=user.hospital_to_request,
                                        status=["s","r"])
        return object

class AllMessageList(LoginRequiredMixin,MessageMixin,ListView):
    template_name = "doctor/MessageList.html"
    def get_queryset(self):
        user = self.request.user.applier.first()
        object = Message.objects.filter(to_hospital= user.hospital_to_request)
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
        token = self.kwargs['token']
        object = Message.objects.filter(token= token)
        object.update(status="r")
        return redirect("doctor:message-detail", token= token)

class CloseMessageStatus(LoginRequiredMixin,MessageMixin,DetailView):
    def get(self,*args, **kwargs):
        object = get_object_or_404(Message, token=self.kwargs['token'])
        object.update(status="c")
        return  redirect("doctor:unread-messages")
