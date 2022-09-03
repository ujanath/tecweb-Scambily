from django.urls import path


from .views import *
from django.contrib.auth.decorators import login_required


app_name = "prodotto"

urlpatterns = [
    path("", login_required(listaprodotto.as_view()), name="prodotto_view"),  # lista di prodotti del tuo user
    path("create", login_required(ProdottoCreate.as_view()), name="prodotto_create"),
    path("<int:pk>", login_required(ProdottoUpdate.as_view()), name="prodotto_update"),
    path("all", listaprodottoall.as_view(), name="prodotto_view_all"),
    path("delete/<int:pk>", login_required(DeleteProdotto.as_view()), name="prodotto_delete"),
    path("buy/<int:pk>", login_required(OrdineCreate.as_view()) , name ="ordine_create"),
    path("ordini", login_required(listaordine.as_view()), name="ordine_view"),
    path("ordini_update/<int:pk>", login_required(aggiorna_ordine.as_view()), name="aggiorna_ordine"),
    path("gestione", login_required(gestione_ordini.as_view()), name="gestione_ordini"),
    path("info/<int:pk>", login_required(infoprodotto.as_view()), name="info_prodotto"),

    path('tag_create/<int:pk>' , login_required(tag_create.as_view()), name="tag_create"),
    path('tag_list/<int:pk>' , login_required(tag_list.as_view()), name="tag_list"),
    path("deletetag/<int:pk>", login_required(tag_eliminate.as_view()), name="tag_eliminate"),
    path("search/", search, name="search"),
    path("searchresults/<str:sstring>/<str:where>", SearchResultList.as_view(), name = "searchresult"),
    path("raccomandati", login_required(raccomanda.as_view()), name = "raccomanda"),


]
