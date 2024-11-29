from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta=models.PositiveIntegerField(primary_key=True)
    id_usuario=models.PositiveIntegerField()
    id_producto=models.PositiveIntegerField()
    id_servicio=models.PositiveIntegerField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.CharField(max_length=50)
    entrega=models.CharField(max_length=50)
    metodo_pago=models.CharField(max_length=50)
    direccion_envio=models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre