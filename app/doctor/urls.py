from django.urls import path
from .views import (RegisterDoctorView,
                    ConfirmDoctorListView,
                    AcceptDoctorView,
                    DeclineDoctorView,
                    SendMessage,
                    UnreadMessageList,
                    MessageDetail,AllMessageList,ReadMessageStatus,CloseMessageStatus)
app_name = "doctor"
urlpatterns = [
    path("register-doctor/",RegisterDoctorView.as_view(),name="register-doctor"),
    path("confirm-doctor-page/",ConfirmDoctorListView.as_view(),name="confirm-doctor-page"),
    path("accept-doctor/<str:email>/",AcceptDoctorView.as_view(),name="accept-doctor"),
    path("decline-doctor/<str:email>/",DeclineDoctorView.as_view(),name="decline-doctor"),
    path("send-message/",SendMessage.as_view(),name='send-message'),
    path("unread-messages-list/",UnreadMessageList.as_view(),name="unread-messages"),
    path("all-message-list/",AllMessageList.as_view(),name="all-messages"),
    path("message-detail/<str:token>/",MessageDetail.as_view(),name="message-detail"),
    path("message-read/<str:token>/",ReadMessageStatus.as_view(),name="read-message"),
    path("message-close/<str:token>/",CloseMessageStatus.as_view(),name="close-message"),

]