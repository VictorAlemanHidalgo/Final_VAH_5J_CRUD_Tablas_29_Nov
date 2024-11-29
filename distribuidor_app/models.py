from django.db import models

# Create your models here.
class Distribuidor(models.Model):
    id_distribuidor=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    id_producto=models.PositiveIntegerField()
    descuento=models.CharField(max_length=30)
    ciudad_estado=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    activo=models.BooleanField()
    telefono=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre