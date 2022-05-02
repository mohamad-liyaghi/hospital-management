from django.db import models
# Create your models here.

class Hospital(models.Model):
    class status(models.TextChoices):
        accepted = ("a","accepted")
        rejected = ("r","rejected")
        no_answer = ("n","no_answer")
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    picture = models.ImageField(upload_to="hospital_picture/",null=True,blank=True)
    hospital_id = models.CharField(max_length=20,unique=True)
    phone_number = models.CharField(max_length=12)
    status = models.CharField(max_length=2,choices=status.choices,default=status.no_answer,blank=True,null=True)
    owner = models.ForeignKey(to="base.BaseUser",on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Message(models.Model):
    title = models.CharField(max_length=30)
    doctor = models.ForeignKey(to="base.BaseUser",related_name="doctor",on_delete=models.CASCADE,blank=True,null=True)
    patient = models.ForeignKey(to="base.BaseUser", on_delete=models.CASCADE, blank=True, null=True)
    to_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    token = models.CharField(max_length=10)

    class status(models.TextChoices):
        sent = ("s", "sent")
        received = ("r", "received")
        closed = ("c", "closed")
    status = models.CharField(max_length=2,choices=status.choices,default=status.sent,blank=True,null=True)