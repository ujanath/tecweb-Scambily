from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# TODO aggiungere piú stati dei articoli
from portafoglio.models import metodo_pagamento_carta
from profilo.models import Profilo

scelta_stato = (
    ('nu', "nuovo"),
    ('pr', "come nuovo"),
    ('us', "usato"),
    ('re', 'ricondizionato')

)

# TODO aggiungere piú categorie
scelta_categorie = (
    ('info', 'informatica'),
    ('phone', 'telefonia'),
    ('games', 'console e giochi'),
    ('book', 'Libri'),
    ('model', 'modellini')

)

scelta_valutazione = (
    ('1', 'pessimo'),
    ('2', 'discreto'),
    ('3', 'buono'),
    ('4', 'molto buono'),
    ('5', 'perfetto')
)


class Prodotto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilo = models.ForeignKey(Profilo, on_delete=models.CASCADE)  # il profilo fa da nucleo ai dati del

    immagine_copertina = models.ImageField(upload_to='products/', null=True, blank=True)
    nome = models.CharField(max_length=50)
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    stato_articolo = stato_articolo = models.CharField(max_length=2, choices=scelta_stato)
    descrizione = models.CharField(max_length=1000)
    disponibilita = models.BooleanField(default='True')
    categoria = models.CharField(max_length=5, choices=scelta_categorie)

    def sono_stato_comprato(self):
        self.disponibilita = False
        self.save()

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

    class Meta:
        verbose_name_plural = "Prodotti"


class Prdotto_Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, null=False)


class Prodotto_ordine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carta = models.ForeignKey(metodo_pagamento_carta, on_delete=models.CASCADE)
    prodotto = models.OneToOneField(Prodotto, on_delete=models.CASCADE)
    dop = models.DateTimeField(default=timezone.now)
    indirizzo = models.CharField(max_length=100)
    stato = models.IntegerField(default=1)

    def eleva_spedizione(self):
        if self.stato == 1:
            self.stato = 2
        elif self.stato == 2:
            self.stato = 3

    def controlla_stato(self):
        if self.stato == 1:
            return 'in sviluppo'
        elif self.stato == 2:
            return 'spedito'
        elif self.stato == 3:
            return 'consegnato'
        elif self.stato == 4:
            return 'reclamo'
        elif self.stato == 5:
            return 'rimborso effettuato'

    def ottieni_username(self):
        return self.user.username


