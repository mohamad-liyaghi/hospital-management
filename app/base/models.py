from django.db import models
from django.contrib.auth.models import AbstractUser
from hospital.models import Hospital
# Create your models here.

class BaseUser(AbstractUser):
    # base info
    class status(models.TextChoices):
        patient = ("pa","patient")
        superuser = ("su","superuser")
        admin = ("ad","admin")
        doctor = ("do","doctor")

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True,blank=True,null=True)
    picture = models.ImageField(blank=True,null=True, upload_to="user-profiles/")
    birthday = models.DateField(blank=True,null=True)
    user_id = models.PositiveIntegerField(unique=True,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    token = models.CharField(max_length=15,null=True,blank=True,unique=True)
    user_status = models.CharField(max_length=2,choices=status.choices,default=status.patient,blank=True,null=True)
    def __str__(self):
        return self.first_name

