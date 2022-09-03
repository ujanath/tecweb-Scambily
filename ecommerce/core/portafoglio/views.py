from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy


class UpdateCarta(UpdateView):
    model = metodo_pagamento_carta
    template_name = 'carta_update.html'
    fields = ('carta_codice', 'carta_CVV', 'carta_scadenza_giorno', 'carta_scadenza_mese')
    success_url = reverse_lazy("profilo:profilo_view")




# Create your views here.
class listacarte(ListView):
    model = metodo_pagamento_carta

    template_name = 'lista_pagamento_carte.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)




class DeleteCarta(DeleteView):
    model = metodo_pagamento_carta
    template_name = 'delete.html'
    success_url = reverse_lazy("profilo:profilo_view")



class CreateCarta(CreateView):
    model = metodo_pagamento_carta
    template_name = 'create_carta.html'
    fields = ('carta_codice', 'carta_CVV', 'carta_scadenza_giorno', 'carta_scadenza_mese')
    success_url = reverse_lazy("portafoglio:lista_carte")

    def form_valid(self, form):
        form.instance.user = self.request.user
        controllo = str(form.instance.carta_codice)
        controllo_cvv = str(form.instance.carta_CVV)
        print(controllo)
        if len(controllo) == 16 and len(controllo_cvv) == 3: #Controllo minimo
            return super().form_valid(form)
        else:
            return HttpResponse("ERROR: il codice di una carta deve essere di 16 cifre e il CVV di 3 !")
        #TODO: controllo se la carta é giá stata inserita per evitare doppioni, ma siccome e una cosa fittizzia
        # verrá fatta se ho tempo
