from django.urls import path
from hospital.views import RegisterHospitalView,ConfirmHospitalListView

app_name = "hospital"

urlpatterns = [
    path("register-hospital/",RegisterHospitalView.as_view(),name="register-hospital"),
    path("hospital-confirm-list/",ConfirmHospitalListView.as_view(),name="hospital-confirm-list")
]