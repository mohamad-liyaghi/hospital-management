from django.urls import path
from hospital.views import (RegisterHospitalView, ConfirmHospitalListView,
                            HospitalProfileView, AcceptHospitalView, DeclineHospitalView,)

app_name = "hospital"

urlpatterns = [
    path("register-hospital/",RegisterHospitalView.as_view(),name="register-hospital"),
    path("hospital-confirm-list/",ConfirmHospitalListView.as_view(),name="hospital-confirm-list"),
    path("profile/<str:id>/",HospitalProfileView.as_view(),name="profile"),
    path("accept-hospital/<int:id>/<int:hospital_id>/",AcceptHospitalView.as_view(),name="accept-hospital"),
    path("decline-hospital/<int:id>/<int:hospital_id>/",DeclineHospitalView.as_view(),name="decline-hospital"),

]