from django.db import models
from django.contrib.auth.models import User
from profilo.models import Profilo

# Create your models here.


scelta_stato = (
    ('nu', "nuovo"),
    ('pr', "come nuovo"),
    ('us', "usato"),
    ('re', 'ricondizionato')

)


class Prodotto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilo = models.ForeignKey(Profilo, on_delete=models.CASCADE)  # il profilo fa da nucleo ai dati del


    immagine_copertina = models.ImageField(upload_to='products/', null=True, blank=True)
    nome = models.CharField(max_length=50)
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    stato_articolo = models.CharField(max_length=2, choices=scelta_stato)
    descrizione = models.CharField(max_length=1000)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

    class Meta:
        verbose_name_plural = "Prodotti"
