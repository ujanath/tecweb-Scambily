from django import forms
from django.http import request
from .models import Prodotto



class ProdottoCreateForm(forms.ModelForm):
    class Meta:
        model = Prodotto
        fields = [ 'profilo', 'immagine_copertina', 'prezzo', 'stato_articolo', 'descrizione']


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['profilo'].queryset = self.fields['profilo'].queryset.filter(user=user)
        self.fields['profilo'].label = "conferma il tuo Luogo di residenza"

