from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "messaggi"

urlpatterns = [
    path("mine", login_required(vedi_messaggio.as_view()), name="messaggi_user"),
    path("crea/<int:pk>",login_required(create_messaggio.as_view()), name="crea_msg"),
    path("crearec/<int:pk>",login_required(create_recensione.as_view()), name="crea_rec"),



]
