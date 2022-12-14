"""axce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path , re_path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *
from .forms import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^$|^\/$|^home\/$", home_page ,name="home"),

    path("register/", UserCreateView.as_view(), name="register"),
    # path("registerstaff/", login_required(StaffCreateView.as_view()), name="register_staff"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("product/" , include("product.urls")),
    path("profilo/" , include("profilo.urls")),
    path("portafoglio/" , include("portafoglio.urls")),
    path("messaggi/" , include("messaggi.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
