from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.urls import reverse_lazy
# Create your views here.


class ProfiloUpdate(UpdateView):
    model = Profilo
    template_name = 'profilo_update.html'
    fields = ( 'immagine_profilo' ,'nome' , 'cognome', 'regione','cap' , 'citta', 'indirizzo','bio'  )
    success_url = reverse_lazy("profilo:profilo_view")


class listaprofilo(ListView):
    model = Profilo
    template_name = 'profilo_view.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ProfiloCreate(CreateView):
    model = Profilo
    fields = ( 'immagine_profilo' ,'nome' , 'cognome', 'regione','cap' , 'citta', 'indirizzo','bio'  )
    template_name = 'profilo_create.html'
    success_url = reverse_lazy("profilo:profilo_view")

    # hack per perfezionisti con una deadline
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

