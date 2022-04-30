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
    path("login/",loginPage.as_view(),name="login"),
    path("register/",registerPage.as_view(),name="register"),
    path("logout/",logoutView,name="logout"),
    path("profile/<str:username>/",ProfileView.as_view(),name="profile"),


]