from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction

import uuid

from base.models import BaseUser
from hospital.models import Hospital,Message
from .forms import RegisterDoctorForm,MessageForm
from .mixins import RegisterDoctorMixin,ConfirmDoctorMixin,MessageMixin

# Create your views here.
class RegisterDoctorView(LoginRequiredMixin,RegisterDoctorMixin,FormView):
    form_class = RegisterDoctorForm
    template_name = "doctor/RegisterDoctor.html"
    @transaction.atomic
    def form_valid(self, form):
        user = BaseUser.objects.filter(username=self.request.user.username)
        form = form.save(commit=False)
        print(form.doc_stat)
        form.doc_stat = "requested"
        user.update(doctor_id=form.doctor_id,
                    hospital_to_request=form.hospital_to_request,
                    doc_stat="re",
                    more_info=form.more_info)
        messages.success(self.request, "request has been sent, please wait for results.")
        return redirect("base:home")
    def form_invalid(self, form):
        messages.success(self.request, "sth went wrong please try again later")
        return redirect("base:home")


class ConfirmDoctorListView(LoginRequiredMixin,ConfirmDoctorMixin, ListView):
    template_name = "doctor/ConfirmDoctor.html"
    def get_queryset(self):
        object = BaseUser.objects.filter(doc_stat="re")
        return object

class AcceptDoctorView(LoginRequiredMixin,ConfirmDoctorMixin,DetailView):
    def get(self,request,username, *args, **kwargs):
        object =BaseUser.objects.filter(username=self.kwargs['username'])
        object.update(doc_stat="ac",user_status="do")
        return redirect("doctor:confirm-doctor-page")

class DeclineDoctorView(LoginRequiredMixin,ConfirmDoctorMixin,DetailView):
    def get(self,request,username, *args, **kwargs):
        object =BaseUser.objects.filter(username=self.kwargs['username'])
        object.update(doc_stat="de",user_status="pa")
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
        return redirect("doctor:messages")