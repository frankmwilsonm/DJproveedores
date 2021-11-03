from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from apirest.models import Proveedor

class ProveedorListView(ListView):
    model = Proveedor #Cliente
    #template_name = ".html"

# Create your views here.
