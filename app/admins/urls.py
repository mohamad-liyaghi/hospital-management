from django.urls import path
from .views import RegisterAdminView
app_name = "admins"

urlpatterns = [
    path("register-admin/",RegisterAdminView.as_view(),name="register-admin")
]