from django.shortcuts import render,redirect
from .models import Servicio

# Create your views here.
def inicio_vistaServicio(request):
    losservicios=Servicio.objects.all()
    return render(request, "gestionarServicio.html", {"misservicios":losservicios})

def registrarServicio(request):
    id_servicio=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["numprecio"]
    tipo=request.POST["txttipo"]
    horario=request.POST["txthorario"]
    ubicacion=request.POST["txtubicacion"]
    id_admin=request.POST["numidadmin"]

    guardarServicio=Servicio.objects.create(
        id_servicio=id_servicio,nombre=nombre,descripcion=descripcion, precio=precio,tipo=tipo,horario=horario,ubicacion=ubicacion,id_admin=id_admin
    ) # GUARDA EL REGISTRO

    return redirect("servicio")

def seleccionarServicio(request,codigo):
    servicio=Servicio.objects.get(id_servicio=codigo)
    return render(request,"editarservicio.html",{"misservicios":servicio})

def editarServicio(request):
    id_servicio=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["numprecio"]
    tipo=request.POST["txttipo"]
    horario=request.POST["txthorario"]
    ubicacion=request.POST["txtubicacion"]
    id_admin=request.POST["numidadmin"]
    servicio=Servicio.objects.get(id_servicio=id_servicio)
    servicio.nombre=nombre
    servicio.descripcion=descripcion
    servicio.precio=precio
    servicio.tipo=tipo
    servicio.horario=horario
    servicio.ubicacion=ubicacion
    servicio.id_admin=id_admin
    
    servicio.save() # guarda registro actualizado
    return redirect("servicio")

def borrarServicio(request,codigo):
    servicio=Servicio.objects.get(id_servicio=codigo)
    servicio.delete() # borra el registro
    return redirect("servicio")