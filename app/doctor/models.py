from django.db import models
from hospital.models import Hospital
from base.models import BaseUser
# Create your models here.
class Doctor(models.Model):
    class doctor_status(models.TextChoices):
        requested = ("re", "requested")
        didnt_requested = ("dr", "didnt_requested")
        accepted = ("ac", "accepted")
        declined = ("de", "declined")
        
    applier = models.ForeignKey(BaseUser,on_delete=models.CASCADE,blank=True, related_name="applier")
    doctor_id = models.PositiveIntegerField(blank=True,unique=True,null=True)
    hospital_to_request = models.ForeignKey(Hospital,blank=True, null=True, on_delete=models.CASCADE)
    more_info = models.TextField(blank=True,null=True)
    doctor_status = models.CharField(max_length=2, choices=doctor_status.choices, default=doctor_status.didnt_requested,blank=True,null=True)
    def __str__(self) :
        return self.applier.username