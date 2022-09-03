import unittest
from django.test import Client
from django.test import TestCase
from .models import *
# Create your tests here.

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import *
class Test_modello_prodotto(unittest.TestCase):

    def setUp(self):
        try:
            User.objects.get(username='testuser').delete() and User.objects.get(username='compratore').delete()
        except Exception:
            pass  # pericoloso ma necessario per usare unittest

        self.reset()

    def test_user(self):
        self.assertEqual(self.user.username , 'testuser')

    def test_user_prodotto_disponibilita(self):
     self.assertTrue(self.prodotto1.disponibilita)

    def test_user_prodotto_viene_comprato(self):
        self.prodotto1.sono_stato_comprato()
        self.assertFalse(self.prodotto1.disponibilita)

    def test_crea_ordine(self):
        c = Client()
        logged_in = c.login(username='compratore', passwrod= 'spadaccino')
        self.assertTrue(logged_in)
    #TODO capire come fare il test delle view

    def reset(self):
        self.user = User.objects.create_user(username='testuser', password='spadaccino')
        self.compratore = User.objects.create_user(username='compratore')
        self.compratore.set_password('spadaccino')


        self.profilo_dummy = Profilo.objects.create(
            user=self.user,
            nome='nome_dummy',
            cognome='cognome_dummy',
            regione='regione_dummy',
            cap='12345',
            citta='citta_dummy',
            indirizzo='indirizzo_dummy',

            bio='bio_dummy_leggermente_lungo'

        )

        self.prodotto1 = Prodotto.objects.create(
            user=self.user,
            profilo=self.profilo_dummy,

            immagine_copertina=SimpleUploadedFile(name='test_image.jpg',
                                                  content=open('static/images/home.jpg', 'rb').read(),
                                                  content_type='image/jpeg'),

            nome='prodotto_dummy',
            prezzo='123',
            stato_articolo='ricondizionato',
            descrizione='descrizione dummy',
            categoria='categoria_dummy'
        )
        self.pagamento1 = metodo_pagamento_carta.objects.create(
            user=self.compratore,
            carta_codice='01234567890123456789',
            carta_CVV='123',
            carta_scadenza_mese='12',
            carta_scadenza_giorno='10',

        )

        self.prodotto2 = Prodotto.objects.create(
            user=self.user,
            profilo=self.profilo_dummy,

            immagine_copertina=SimpleUploadedFile(name='test_image.jpg',
                                                  content=open('static/images/home.jpg', 'rb').read(),
                                                  content_type='image/jpeg'),

            nome='prodotto_dummy',
            prezzo='123',
            stato_articolo='ricondizionato',
            descrizione='descrizione dummy',
            categoria='categoria_dummy'
        )

