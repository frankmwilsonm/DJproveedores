from rest_framework import serializers
from .models import Proveedor

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Proveedor
        fields = ('id', 'nombres', 'apellidos', 'razonsocial','direccion', 'ruc', 'celular')
