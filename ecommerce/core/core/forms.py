from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class CreaUtenteVenditore(UserCreationForm):
    #Facciamo un override del metodo save per assicurarci di assegnare il gruppo specificato
    #all'utente appena registrato. I gruppi possono essere creati in via programmatica, ma in questo
    #caso li abbiamo creati dal pannello admin nell'interfaccia grafica web.
    
    def save(self, commit=True):
        user = super().save(commit) #ottengo un riferimento all'utente
        g = Group.objects.get(name="Registrato") #cerco il gruppo che mi interessa
        g.user_set.add(user) #aggiungo l'utente al gruppo
        return user #restituisco quello che il metodo padre di questo metodo avrebbe restituito.


# class CreaUtenteStaff(UserCreationForm):
#     # Facciamo un override del metodo save per assicurarci di assegnare il gruppo specificato
#     # all'utente appena registrato. I gruppi possono essere creati in via programmatica, ma in questo
#     # caso li abbiamo creati dal pannello admin nell'interfaccia grafica web.
#
#     def save(self, commit=True):
#         user = super().save(commit)  # ottengo un riferimento all'utente
#         g = Group.objects.get(name="Staff")  # cerco il gruppo che mi interessa
#         g.user_set.add(user)  # aggiungo l'utente al gruppo
#
#         return user  # restituisco quello che il metodo padre di questo metodo avrebbe restituito.
