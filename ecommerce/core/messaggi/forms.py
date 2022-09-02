from django import forms
from django.http import request
from .models import *


class  MessaggioCreateForm(forms.ModelForm):
    class Meta:
        model = Messaggi

        fields = [ 'message' , 'img' ]


    #TODO implementare la lista prodotti quando crei un messaggio

    def __init__(self, *args, **kwargs):
        #   ricevi = kwargs.pop('pk', None)
            super().__init__(*args, **kwargs)
        # self.fields['prodotto'].queryset = self.fields['prodotto'].queryset.filter(user=ricevi)



