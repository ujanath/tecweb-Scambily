from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = "prodotto"

urlpatterns = [
    path("", login_required(listaprodotto.as_view()), name="prodotto_view"),  # lista di prodotti del tuo user
    path("create", login_required(ProdottoCreate.as_view()), name="prodotto_create"),
    path("<int:pk>", login_required(ProdottoUpdate.as_view()), name="prodotto_update"),
    path("all", login_required(listaprodottoall.as_view()), name="prodotto_view_all"),
    path("delete/<int:pk>", login_required(DeleteProdotto.as_view()), name="prodotto_delete"),
    path("buy/<int:pk>", login_required(OrdineCreate.as_view()) , name ="ordine_create")


]
