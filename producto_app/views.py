from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.
def inicio_vistaProducto(request):
    losproductos=Producto.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos":losproductos})

def registrarProducto(request):
    id_producto=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["numprecio"]
    stolk=request.POST["numstolk"]
    tipo=request.POST["txttipo"]
    linea=request.POST["datelinea"]
    id_admin=request.POST["numidadmin"]

    linea=Producto.objects.create(
        id_producto=id_producto,nombre=nombre,descripcion=descripcion, precio=precio,stolk=stolk,tipo=tipo,linea=linea,id_admin=id_admin
    ) # GUARDA EL REGISTRO

    return redirect("producto")

def seleccionarProducto(request,codigo):
    producto=Producto.objects.get(id_producto=codigo)
    fecha_fin=producto.linea.strftime('%Y-%m-%d')
    return render(request,"editarproducto.html",{"misproductos":producto, "misproductos":producto,"fecha_fin":fecha_fin})

def editarProducto(request):
    id_producto=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["numprecio"]
    stolk=request.POST["numstolk"]
    tipo=request.POST["txttipo"]
    linea=request.POST["datelinea"]
    id_admin=request.POST["numidadmin"]
    producto=Producto.objects.get(id_producto=id_producto)
    producto.nombre=nombre
    producto.descripcion=descripcion
    producto.precio=precio
    producto.stolk=stolk
    producto.tipo=tipo
    producto.linea=linea
    producto.id_admin=id_admin
    
    producto.save() # guarda registro actualizado
    return redirect("producto")

def borrarProducto(request,codigo):
    producto=Producto.objects.get(id_producto=codigo)
    producto.delete() # borra el registro
    return redirect("producto")