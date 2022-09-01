from django import forms
from django.http import request
from .models import Recensione

class RecensioneForm(forms.ModelForm):
    class Meta:
        model = Recensione
        fields = [ 'ordine',
                   'target',
                   'valutazione',
                   'points'
                   ]


    def __init__(self, *args, **kwargs):
        ordine = kwargs.pop('ordine', None)
        super().__init__(*args, **kwargs)
        self.fields['target'].queryset = self.fields['target'].queryset.filter()
