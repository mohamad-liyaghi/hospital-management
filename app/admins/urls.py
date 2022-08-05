from django.urls import path
from .views import RegisterAdminView,ConfirmAdminListView,AcceptAdminView,DeclineAdminView
app_name = "admins"

urlpatterns = [
    path("register-admin/",RegisterAdminView.as_view(),name="register-admin"),
    path("confirm-admin-list/",ConfirmAdminListView.as_view(),name="confrim-admin-list"),
    path("accept-admin/<str:email>/",AcceptAdminView.as_view(),name="accept-admin"),
    path("decline-admin/<str:email>/",DeclineAdminView.as_view(),name="decline-admin"),
]