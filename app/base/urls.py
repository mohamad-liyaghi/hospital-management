from django.urls import path
from .views import homePage,loginPage,logoutView,registerPage

app_name = "base"

urlpatterns = [
    path("",homePage,name="home"),
    path("login/",loginPage.as_view(),name="login"),
    path("register/",registerPage.as_view(),name="register"),
    path("logout/",logoutView,name="logout")
]