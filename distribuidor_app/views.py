from django.shortcuts import render,redirect
from .models import Distribuidor

# Create your views here.
def inicio_vistaDistribuidor(request):
    losdistribuidores=Distribuidor.objects.all()
    return render(request, "gestionarDistribuidor.html", {"misdistribuidores":losdistribuidores})

def registrarDistribuidor(request):
    id_distribuidor=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    id_producto=request.POST["txtcodigoproducto"]
    descuento=request.POST["txtdescuento"]
    ciudad_estado=request.POST["txtciudad_estado"]
    direccion=request.POST["txtdireccion"]
    activo='chkactivo' in request.POST
    telefono=request.POST["numtelefono"]
    
    guardarDistribuidor=Distribuidor.objects.create(
        id_distribuidor=id_distribuidor,nombre=nombre,id_producto=id_producto, descuento=descuento,ciudad_estado=ciudad_estado, direccion=direccion, activo=activo, telefono=telefono 
        ) # GUARDA EL REGISTRO


    return redirect("distribuidor")



def seleccionarDistribuidor(request,codigo):
    distribuidor=Distribuidor.objects.get(id_distribuidor=codigo)
    return render(request,"editardistribuidor.html",{"misdistribuidores":distribuidor})

def editarDistribuidor(request):
    id_distribuidor=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    id_producto=request.POST["txtcodigoproducto"]
    descuento=request.POST["txtdescuento"]
    ciudad_estado=request.POST["txtciudad_estado"]
    direccion=request.POST["txtdireccion"]
    activo='chkactivo' in request.POST
    telefono=request.POST["numtelefono"]
    distribuidor=Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    distribuidor.nombre=nombre
    distribuidor.id_producto=id_producto
    distribuidor.descuento=descuento
    distribuidor.ciudad_estado=ciudad_estado
    distribuidor.direccion=direccion
    distribuidor.activo=activo
    distribuidor.telefono=telefono
    
    distribuidor.save() # guarda registro actualizado
    return redirect("distribuidor")

def borrarDistribuidor(request,codigo):
    distribuidor=Distribuidor.objects.get(id_distribuidor=codigo)
    distribuidor.delete() # borra el registro
    return redirect("distribuidor")