from django.urls import path
from .views import (homePage,
                    loginPage,
                    logoutView,
                    registerPage,
                    ProfileView,

                    )

app_name = "base"

urlpatterns = [
    path("",homePage,name="home"),
    path("profile/<int:id>/<str:email>/",ProfileView.as_view(),name="profile"),


]