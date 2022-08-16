from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *

def home_page(request):
    return render(request, template_name="home.html")


class UserCreateView(CreateView):
    #form_class = UserCreationForm
    form_class = CreaUtenteVenditore
    template_name = "user_create.html"
    success_url = reverse_lazy("home")

