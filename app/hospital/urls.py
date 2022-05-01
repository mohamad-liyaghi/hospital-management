from django.urls import path
from hospital.views import RegisterHospitalView,ConfirmHospitalListView,HospitalProfileView

app_name = "hospital"

urlpatterns = [
    path("register-hospital/",RegisterHospitalView.as_view(),name="register-hospital"),
    path("hospital-confirm-list/",ConfirmHospitalListView.as_view(),name="hospital-confirm-list"),
    path("profile/<str:id>/",HospitalProfileView.as_view(),name="profile")
]