from django.db import models

# Create your models here.
class Servicio(models.Model):
    id_servicio=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    tipo=models.CharField(max_length=50)
    horario=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=100)
    id_admin=models.PositiveIntegerField()
    

    def __str__(self):
        return self.nombre