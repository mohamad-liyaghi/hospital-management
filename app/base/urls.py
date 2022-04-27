from django.urls import path
from .views import homePage

app_name = "base"

urlpatterns = [
    path("",homePage,name="home")
]