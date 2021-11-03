from django.contrib import admin
from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'razonsocial', 'ruc', 'celular', 'web')

admin.site.register(Proveedor, ProveedorAdmin) #Quita ProductoAdmin si no funciona

# Register your models here.
