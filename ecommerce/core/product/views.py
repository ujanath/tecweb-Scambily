from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Prodotto
from django.urls import reverse_lazy
from .forms import ProdottoCreateForm


# Create your views here.


class ProdottoUpdate(UpdateView):
    model = Prodotto
    template_name = 'prodotto_update.html'
    fields = ('profilo', 'immagine_copertina', 'nome', 'prezzo', 'stato_articolo', 'descrizione')
    success_url = reverse_lazy("prodotto:prodotto_view")


class listaprodotto(ListView):
    model = Prodotto
    template_name = 'prodotto_view.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class listaprodottoall(ListView):
    model = Prodotto
    template_name = 'prodotto_view.html'

    def get_queryset(self):
        return self.model.objects.all()


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