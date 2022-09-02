from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.



class Profilo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    immagine_profilo = models.ImageField(upload_to='images/', null=True, blank=True)
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    regione = models.CharField(max_length=50)
    cap = models.CharField(max_length=50)
    citta = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=100)

    bio = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.regione + " " + self.citta + " " + self.indirizzo)

    class Meta:
        verbose_name_plural = "Profili"


