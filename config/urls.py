"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('superuser/', admin.site.urls),
    path("accounts/", include("allauth.urls")),

    path("",include("app.base.urls")),
    path("hospital/",include("app.hospital.urls")),
    path("doctor/",include("app.doctor.urls")),
    path("admin/",include("app.admins.urls")),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


handler404 = 'app.base.views.page_not_found'
handler500 = 'app.base.views.server_error'