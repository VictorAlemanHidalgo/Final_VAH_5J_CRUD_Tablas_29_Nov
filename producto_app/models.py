from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    stolk=models.PositiveIntegerField()
    tipo=models.CharField(max_length=50)
    linea=models.DateField()
    id_admin=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre