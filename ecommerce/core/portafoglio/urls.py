from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "portafoglio"

urlpatterns = [
    path("carte", login_required(listacarte.as_view()), name="lista_carte"),
    path("paypal", login_required(listapaypal.as_view()), name="lista_pp"), # lista di prodotti del tuo user



]
