from django.urls import path
from .views import RegisterDoctorView,ConfirmDoctorListView
urlpatterns = [
    path("register-doctor/",RegisterDoctorView.as_view(),name="register-doctor"),
    path("confirm-doctor-page/",ConfirmDoctorListView.as_view(),name="confirm-doctor-page"),
]