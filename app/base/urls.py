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
    path("profile/<str:username>/",ProfileView.as_view(),name="profile"),


]