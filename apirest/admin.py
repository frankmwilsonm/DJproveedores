from django.contrib import admin

from .models import Proveedor

admin.site.register(Proveedor, ProveedorAdmin) #Quita ProductoAdmin si no funciona

# Register your models here.
