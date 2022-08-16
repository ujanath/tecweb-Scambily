from django.contrib import admin
from django.urls import path , re_path , include
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.conf.urls.static import static 

app_name= "profilo"

urlpatterns = [
    path("" , login_required(listaprofilo.as_view()) , name = "profilo_view" ),  # lista di prodotti del tuo user
    path("create" , login_required(ProfiloCreate.as_view()), name = "profilo_create"),
     path("<int:pk>" , login_required(ProfiloUpdate.as_view()), name = "profilo_update")
]
