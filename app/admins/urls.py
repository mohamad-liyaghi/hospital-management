from django.urls import path
from .views import RegisterAdminView,ConfirmAdminListView
app_name = "admins"

urlpatterns = [
    path("register-admin/",RegisterAdminView.as_view(),name="register-admin"),
    path("confirm-admin-list/",ConfirmAdminListView.as_view(),name="confrim-admin-list")
]