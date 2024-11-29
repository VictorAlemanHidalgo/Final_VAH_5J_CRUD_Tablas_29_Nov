from django.shortcuts import render,redirect
from .models import Administrador

# Create your views here.
def inicio_vistaAdministrador(request):
    losadministradores=Administrador.objects.all()
    return render(request, "gestionarAdministrador.html", {"misadministradores":losadministradores})

def registrarAdministrador(request):
    id_admin=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    cargo=request.POST["txtCargo"]

    guardarAdministrador=Administrador.objects.create(
        id_admin=id_admin,nombre=nombre,apellidos=apellidos, email=email,telefono=telefono,direccion=direccion,cargo=cargo
    ) # GUARDA EL REGISTRO

    return redirect("administrador")

def seleccionarAdministrador(request,codigo):
    administrador=Administrador.objects.get(id_admin=codigo)
    return render(request,"editaradministrador.html",{"misadministradores":administrador})

def editarAdministrador(request):
    id_admin=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    cargo=request.POST["txtCargo"]
    administrador=Administrador.objects.get(id_admin=id_admin)
    administrador.id_admin=id_admin
    administrador.nombre=nombre
    administrador.apellidos=apellidos
    administrador.email=email
    administrador.telefono=telefono
    administrador.direccion=direccion
    administrador.cargo=cargo
    
    administrador.save() # guarda registro actualizado
    return redirect("administrador")

def borrarAdministrador(request,codigo):
    administrador=Administrador.objects.get(id_admin=codigo)
    administrador.delete() # borra el registro
    return redirect("administrador")