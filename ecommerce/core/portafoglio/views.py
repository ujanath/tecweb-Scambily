from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy


class UpdateCarta(UpdateView):
    model = metodo_pagamento_carta
    template_name = 'carta_update.html'
    fields = ('carta_codice', 'carta_CVV', 'carta_scadenza_giorno', 'carta_scadenza_mese')
    success_url = reverse_lazy("profilo:profilo_view")


class UpdatePaypal(UpdateView):
    model = metodo_pagamento_paypal
    template_name = 'paypal_update.html'
    fields = ('paypal_email', 'paypal_password')
    success_url = reverse_lazy("profilo:profilo_view")


# Create your views here.
class listacarte(ListView):
    model = metodo_pagamento_carta

    template_name = 'lista_pagamento_carte.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class listapaypal(ListView):
    model = metodo_pagamento_paypal

    template_name = 'lista_pagamento_paypal.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class DeleteCarta(DeleteView):
    model = metodo_pagamento_carta
    template_name = 'delete.html'
    success_url = reverse_lazy("profilo:profilo_view")


class DeletePp(DeleteView):
    model = metodo_pagamento_paypal
    template_name = 'delete.html'
    success_url = reverse_lazy("profilo:profilo_view")


class CreateCarta(CreateView):
    model = metodo_pagamento_carta
    template_name = 'create_carta.html'
    fields = ('carta_codice', 'carta_CVV', 'carta_scadenza_giorno', 'carta_scadenza_mese')
    success_url = reverse_lazy("portafoglio:lista_carte")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreatePaypal(CreateView):
    model = metodo_pagamento_paypal
    template_name = 'create_paypal.html'
    fields = ('paypal_email', 'paypal_password')
    success_url = reverse_lazy("profilo:profilo_view")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
