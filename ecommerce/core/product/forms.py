from django import forms
from django.http import request
from .models import Prodotto , Prodotto_ordine , Prdotto_Tag



class ProdottoCreateForm(forms.ModelForm):
    class Meta:
        model = Prodotto
        fields = [ 'nome',
                   'immagine_copertina',
                   'prezzo',
                   'stato_articolo',
                   'descrizione',
                   'categoria'
                   ]


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)





class  OrdineCreateForm(forms.ModelForm):
    class Meta:
        model = Prodotto_ordine

        fields = [ 'carta'  , 'indirizzo' ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['carta'].queryset = self.fields['carta'].queryset.filter(user=user)

class  TagCreateForm(forms.ModelForm):
    class Meta:
        model = Prdotto_Tag

        fields = [ 'tag' ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    

class SearchForm(forms.Form):

    CHOICE_LIST = [("nome" , "Nome del Prodotto"),
                   ("descrizione","descrizione del prodotto"),
                   ("tag" , "vuoi cercare con un tag speciale")]

    search_string = forms.CharField(label="cosa devo cercare" , max_length= 100, min_length= 3 , required=True)
    search_where = forms.ChoiceField(label="cercare dove ? " , required=True , choices=CHOICE_LIST)
