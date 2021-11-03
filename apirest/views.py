from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProveedorSerializer
from .models import Proveedor

class ProveedorViewSet (viewsets.ModelViewSet):
    queryset=Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# Create your views here.
