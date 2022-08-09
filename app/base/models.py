from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from hospital.models import Hospital
import random
# Create your models here.

class UserManager(BaseUserManager):
    '''
        Manager for creating user
    '''
    def create_user(self, email, first_name, last_name, picture, birthday, user_id, description, user_status, password):
        '''
            Create a user
        '''
        if not email:
            raise ValueError("Email is required")

        user = self.model(email= email,
                          first_name= first_name, last_name= last_name, picture=picture,
                          birthday= birthday, user_id=user_id, description=description,
                          token= random.randint(1, 99999999999999), user_status= "admin"
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, user_id, password):
        # create new superuser
        user = self.model(email=email,
                          user_status="su",
                          first_name=first_name, last_name=last_name,
                          user_id=user_id, description="This user is root",
                          token=random.randint(1, 99999999999999)
                          )

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class BaseUser(AbstractUser):
    # base info
    class status(models.TextChoices):
        patient = ("pa","patient")
        superuser = ("su","superuser")
        admin = ("ad","admin")
        doctor = ("do","doctor")

    picture = models.ImageField(blank=True,null=True, upload_to="user-profiles/")
    email = models.EmailField(unique=True)
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField(blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    user_id = models.PositiveIntegerField(unique=True,blank=True,null=True)
    token = models.CharField(max_length=15,null=True,blank=True,unique=True)
    user_status = models.CharField(max_length=2,choices=status.choices, default=status.patient,blank=True,null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "user_id"]

    def __str__(self):
        return self.email
