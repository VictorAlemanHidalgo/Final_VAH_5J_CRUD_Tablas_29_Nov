from django.db import models

# Create your models here.
class Administrador(models.Model):
    id_admin=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    telefono=models.PositiveIntegerField()
    direccion=models.CharField(max_length=100)
    cargo=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre