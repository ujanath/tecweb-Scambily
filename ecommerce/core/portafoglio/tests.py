import unittest
from django.contrib.auth.models import User

from django.test import TestCase
from .models import metodo_pagamento_carta

# Create your tests here.

class Test_metodo_pagamento_carta(unittest.TestCase):

    def setUp(self):

        user = User.objects.create(username='testuser')
        user.set_password('12345678')
        user.save()

        self.pagamento1 = metodo_pagamento_carta.objects.create(
            user = user ,
            carta_codice= '01234567890123456789',
            carta_CVV='123',
            carta_scadenza_mese='12',
            carta_scadenza_giorno='10',

        )


    def test_codice_carta(self):
        test = 'finisce per *789'
        self.assertEqual(self.pagamento1.ultime_tre_cifre(), test)

