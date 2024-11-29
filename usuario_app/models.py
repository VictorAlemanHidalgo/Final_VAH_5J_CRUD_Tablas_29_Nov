from django.db import models

# Create your models here.
class Usuario(models.Model):
    Id_user=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    telefono=models.PositiveIntegerField()
    direccion=models.CharField(max_length=100)
    fecha_registro=models.DateField(null=False,blank=False)
    tipo_usuario=models.CharField(max_length=20)
    id_admin=models.PositiveIntegerField()

    
    def __str__(self):
        return self.nombre