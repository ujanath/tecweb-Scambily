from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import *


class create_messaggio(CreateView):
    model = Messaggi
    form_class = MessaggioCreateForm
    template_name = 'create_temp.html'
    success_url = reverse_lazy("profilo:profilo_view")

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)

        return kwargs

    def form_valid(self, form):
        form.instance.user_invio = self.request.user

        ricevi = User.objects.get(pk=self.kwargs['pk'])

        self.object = form.save(commit=False)
        self.object.user_ricevi = ricevi
        self.object.save()
        return super().form_valid(form)


class vedi_messaggio(ListView):
    model = Messaggi

    template_name = 'msg_view.html'

    def get_queryset(self):
        return self.model.objects.filter(user_ricevi=self.request.user)
