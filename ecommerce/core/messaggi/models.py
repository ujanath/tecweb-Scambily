from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
from product.models import Prodotto, Prodotto_ordine


#Model.get_FOO_display()

scelta_valutazione = (
    ('1', 'pessimo'),
    ('2', 'discreto'),
    ('3', 'buono'),
    ('4', 'molto buono'),
    ('5', 'perfetto')
)

class recensione(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordine = models.OneToOneField(Prodotto_ordine, on_delete=models.CASCADE)

    dop = models.DateTimeField(default=timezone.now)
    voto = models.DecimalField(max_digits=3, decimal_places=1, choices=scelta_valutazione)
    descrizione = models.CharField(max_length=1000, null=False)



class segnalazione(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    dop = models.DateTimeField(default=timezone.now)
    ordine = models.OneToOneField(Prodotto_ordine, on_delete=models.CASCADE)
    descrizione = models.CharField(max_length=1000, null=False)
    prova_immagine_1 = models.ImageField(upload_to='segnalazioni/', null=True, blank=False)
    prova_immagine_2 = models.ImageField(upload_to='segnalazioni/', null=True, blank=True)
    prova_immagine_3 = models.ImageField(upload_to='segnalazioni/', null=True, blank=True)



class Messaggi(models.Model):
    user_invio = models.ForeignKey(User, on_delete=models.CASCADE , related_name="user_invio")
    user_ricevi = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ricevi")
    message = models.CharField(max_length=5000)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE , null=True , blank=True)
    img = models.ImageField(upload_to='chat/', blank=True)
    dop = models.DateTimeField(default=timezone.now)
