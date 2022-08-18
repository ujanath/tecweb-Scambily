from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "portafoglio"

urlpatterns = [
    path("carte", login_required(listacarte.as_view()), name="lista_carte"),
    path("paypal", login_required(listapaypal.as_view()), name="lista_pp"),# lista di prodotti del tuo user

    path("createpp" ,login_required(CreatePaypal.as_view()), name="create_pp" ),
    path("createcarta" ,login_required(CreateCarta.as_view()), name="create_carta" ),

    path('delete/<int:pk>' , login_required(DeleteCarta.as_view()), name = "delete_carta"),
    path('deletepp/<int:pk>' , login_required(DeletePp.as_view()), name = "delete_pp"),

    path('updatecarta/<int:pk>' , login_required(UpdateCarta.as_view()), name = "update_carta"),
    path('updatepp/<int:pk>' , login_required(UpdatePaypal.as_view()), name = "update_pp"),





]
