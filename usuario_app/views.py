from django.shortcuts import render,redirect
from .models import Usuario

# Create your views here.
def inicio_vistaUsuario(request):
    losusuarios=Usuario.objects.all()
    return render(request, "gestionarUsuario.html", {"misusuarios":losusuarios})

def registrarUsuario(request):
    Id_user=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    fecha_registro=request.POST["dateregistro"]
    tipo_usuario=request.POST["txtTipo"]
    id_admin=request.POST["numidadmin"]

    guardarusuario=Usuario.objects.create(
        Id_user=Id_user,nombre=nombre,apellidos=apellidos, email=email,telefono=telefono,direccion=direccion,fecha_registro=fecha_registro,tipo_usuario=tipo_usuario,id_admin=id_admin
    ) # GUARDA EL REGISTRO

    return redirect("usuario")

def seleccionarUsuario(request,codigo):
    usuario=Usuario.objects.get(Id_user=codigo)
    fecha_fin=usuario.fecha_registro.strftime('%Y-%m-%d')
    return render(request,"editarusuario.html",{"misusuarios":usuario, "misusuarios" : usuario, "fecha_fin" : fecha_fin})

def editarUsuario(request):
    Id_user=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    email=request.POST["txtemail"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    fecha_registro=request.POST["dateregistro"]
    tipo_usuario=request.POST["txtTipo"]
    id_admin=request.POST["numidadmin"]
    usuario=Usuario.objects.get(Id_user=Id_user)
    usuario.nombre=nombre
    usuario.apellidos=apellidos
    usuario.email=email
    usuario.telefono=telefono
    usuario.direccion=direccion
    usuario.fecha_registro=fecha_registro
    usuario.tipo_usuario=tipo_usuario
    usuario.id_admin=id_admin
    
    usuario.save() # guarda registro actualizado
    return redirect("usuario")

def borrarUsuario(request,codigo):
    usuario=Usuario.objects.get(Id_user=codigo)
    usuario.delete() # borra el registro
    return redirect("usuario")