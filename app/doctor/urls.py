from django.urls import path
from .views import (RegisterDoctorView,
                    ConfirmDoctorListView,
                    AcceptDoctorView,
                    DeclineDoctorView,
                    SendMessage,
                    MessageList,
                    MessageDetail)
app_name = "doctor"
urlpatterns = [
    path("register-doctor/",RegisterDoctorView.as_view(),name="register-doctor"),
    path("confirm-doctor-page/",ConfirmDoctorListView.as_view(),name="confirm-doctor-page"),
    path("accept-doctor/<str:username>/",AcceptDoctorView.as_view(),name="accept-doctor"),
    path("decline-doctor/<str:username>/",DeclineDoctorView.as_view(),name="decline-doctor"),
    path("send-message/",SendMessage.as_view(),name='send-message'),
    path("message-list/",MessageList.as_view(),name="messages"),
    path("message-detail/<str:token>/",MessageDetail.as_view(),name="message-detail")
]