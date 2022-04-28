from django.urls import path
from .views import RegisterDoctorView
urlpatterns = [
    path("register-doctor/",RegisterDoctorView.as_view(),name="register-doctor"),
]