from django.db import OperationalError
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import ProdottoCreateForm, OrdineCreateForm , TagCreateForm
from django.shortcuts import get_object_or_404


# Create your views here.


class ProdottoUpdate(UpdateView):
    model = Prodotto
    form_class = ProdottoCreateForm
    template_name = 'prodotto_create.html'
    success_url = reverse_lazy("prodotto:prodotto_view")


class listaprodotto(ListView):
    model = Prodotto
    template_name = 'prodotto_view.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class listaordine(ListView):
    model = Prodotto_ordine
    template_name = 'ordine_view.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ProdottoCreate(CreateView):
    model = Prodotto
    form_class = ProdottoCreateForm
    template_name = 'prodotto_create.html'
    success_url = reverse_lazy("prodotto:prodotto_view")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrdineCreate(CreateView):
    model = Prodotto_ordine
    form_class = OrdineCreateForm
    template_name = 'prodotto_create.html'
    success_url = reverse_lazy("prodotto:prodotto_view")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        prodotto = Prodotto.objects.get(pk=self.kwargs['pk'])


        self.object = form.save(commit=False)
        self.object.prodotto = prodotto
        self.object.prodotto.sono_stato_comprato()
        self.object.save()
        return super().form_valid(form)


class DeleteProdotto(DeleteView):
    model = Prodotto
    template_name = 'delete.html'
    success_url = reverse_lazy("prodotto:prodotto_view")


class listaprodottoall(ListView):
    model = Prodotto
    template_name = 'prodotto_view_all.html'

    def get_queryset(self):

        try:

            return self.model.objects.all()

        except OperationalError:
                return HttpResponse("ERROR")


# TODO info prodotto ordinato
class infoprodotto(ListView):
    model = Prodotto
    template_name = 'prodotto_info.html'

    def get_queryset(self):
        # controllo se esiste un ordine fatto da questo user per il prodotto che controllo
        check = Prodotto_ordine.objects.filter(user_id=self.request.user, prodotto_id=self.kwargs['pk'])
        if check:
            return self.model.objects.filter(pk=self.kwargs['pk'])

        if get_object_or_404(Prodotto, id=self.kwargs['pk']).user.username == self.request.user.username :
            return self.model.objects.filter(pk=self.kwargs['pk'])

class gestione_ordini(ListView):
    model = Prodotto_ordine
    template_name = 'gestione_ordini.html'

    def get_queryset(self):
        lista_prod = Prodotto.objects.filter(user_id=self.request.user, disponibilita=False)
        lista = lista_prod.values_list('id', flat=True)

        return self.model.objects.filter(prodotto_id__in=lista)


class aggiorna_ordine(ListView):
    model = Prodotto_ordine
    template_name = 'ordine_view.html'

    def get_queryset(self):


        update = get_object_or_404(Prodotto_ordine ,id=self.kwargs['pk'])

        # posso cambiare se solo se sono quello che ha comprato e se stato spedito
        if self.request.user == update.user and update.stato == 2:

            update.eleva_spedizione()
            update.save()

            return self.model.objects.filter(user=self.request.user)

        if self.request.user == update.prodotto.user and update.stato == 1:
            update.eleva_spedizione()
            update.save()

            lista_prod = Prodotto.objects.filter(user_id=self.request.user, disponibilita=False)
            lista = lista_prod.values_list('id', flat=True)

            return self.model.objects.filter(prodotto_id__in=lista)


class tag_create(CreateView):
    model = Prdotto_Tag
    form_class = TagCreateForm
    template_name = 'prodotto_create.html'
    success_url = reverse_lazy("prodotto:prodotto_view")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        prodotto = Prodotto.objects.get(pk=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.prodotto = prodotto
        self.object.save()
        return super().form_valid(form)


class tag_list(ListView):
    model = Prdotto_Tag
    template_name = 'P_tag_info.html'

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs['pk'])

