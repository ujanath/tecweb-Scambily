from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class metodo_pagamento_carta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    carta_codice = models.DecimalField(max_digits=20 , decimal_places=0)
    carta_CVV = models.DecimalField(max_digits=20 , decimal_places=0)
    carta_scadenza_giorno = models.DecimalField(max_digits=4 , decimal_places=0)
    carta_scadenza_mese   = models.DecimalField(max_digits=2 , decimal_places=0)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)




class metodo_pagamento_paypal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    paypal_email    = models.CharField(max_length=50)
    paypal_password = models.CharField(max_length=50)


    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)




