from django import forms
from django.http import request
from .models import Prodotto



class ProdottoCreateForm(forms.ModelForm):
    class Meta:
        model = Prodotto
        fields = [ 'nome',
                   'profilo',
                   'immagine_copertina',
                   'prezzo',
                   'stato_articolo',
                   'descrizione',
                   'categoria'
                   ]


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['profilo'].queryset = self.fields['profilo'].queryset.filter(user=user)
        self.fields['profilo'].label =\
            "conferma il tuo Luogo di residenza , se non vedi nulla é perche non hai creato il uo profilo"



#$class OrdinaProdotto(forms.ModelForm):
