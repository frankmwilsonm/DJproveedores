from django.db import models

class Proveedor(models.Model):
        ##Atributos
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    razonsocial=models.CharField(max_length=50)
    direccion=models.CharField(max_length=250)
    ruc=models.CharField(max_length=50)
    celular=models.CharField(max_length=15)
    web=models.CharField(max_length=15, default="")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = ("Proveedor")
        verbose_name_plural = ("Proveedores")

    def __str__(self):
        return self.nombres #name Cambia segun Atributo queramos regresar


# Create your models here.
