from django.db import models
from base.models import BaseUser
# Create your models here.
class Admin(models.Model):
    class admin_status(models.TextChoices):
        requested = ("re", "requested")
        didnt_requested = ("dr", "didnt_requested")
        accepted = ("ac", "accepted")
        declined = ("de", "declined")

    applier = models.ForeignKey(BaseUser,on_delete=models.CASCADE,blank=True, related_name="admin_applier")
    admin_stat = models.CharField(max_length=2, choices=admin_status.choices, default=admin_status.didnt_requested, blank=True, null=True)
    admin_description = models.TextField(blank=True,null=True)

    def __str__(self) :
        return self.applier.email