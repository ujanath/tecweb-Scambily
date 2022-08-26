from django.db import models
from django.contrib.auth.models import User
from profilo.models import *
from portafoglio.models import *
from django.utils import timezone

# Create your models here.

# TODO aggiungere piú stati dei articoli
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
scelta_stato_spedizione = (
    ('1', 'in sviluppo'),
    ('2', 'spedito'),
    ('3', 'consegnato')
)

class Prodotto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilo = models.ForeignKey(Profilo, on_delete=models.CASCADE)  # il profilo fa da nucleo ai dati del


    immagine_copertina = models.ImageField(upload_to='products/', null=True, blank=True)
    nome = models.CharField(max_length=50)
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    stato_articolo =stato_articolo = models.CharField(max_length=2, choices=scelta_stato)
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
    tag = models.CharField(max_length=100 , null= False)


class Prodotto_ordine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carta = models.ForeignKey(metodo_pagamento_carta, on_delete=models.CASCADE)
    prodotto = models.OneToOneField(Prodotto, on_delete=models.CASCADE)
    dop = models.DateTimeField(default=timezone.now)
    indirizzo = models.CharField(max_length=100)

