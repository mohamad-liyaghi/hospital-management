from django.urls import path
from hospital.views import RegisterHospitalView

app_name = "hospital"

urlpatterns = [
    path("register-hospital/",RegisterHospitalView.as_view(),name="register-hospital")
]