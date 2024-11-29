from django.shortcuts import render,redirect
from .models import Venta

# Create your views here.
def inicio_vistaVenta(request):
    lasventas=Venta.objects.all()
    return render(request, "gestionarVenta.html", {"misventas":lasventas})

def registrarVenta(request):
    id_venta=request.POST["txtcodigo"]
    id_usuario=request.POST["numiduser"]
    id_producto=request.POST["numidproducto"]
    id_servicio=request.POST["numidservicio"]
    precio=request.POST["numprecio"]
    estado=request.POST["txtestado"]
    entrega=request.POST["txtentrega"]
    metodo_pago=request.POST["txtmetodopago"]
    direccion_envio=request.POST["txtdireccionenvio"]


    guardarVenta=Venta.objects.create(
        id_venta=id_venta,id_usuario=id_usuario,id_producto=id_producto,id_servicio=id_servicio,precio=precio,estado=estado,entrega=entrega, metodo_pago=metodo_pago,direccion_envio=direccion_envio
    ) # GUARDA EL REGISTRO

    return redirect("venta")

def seleccionarVenta(request,codigo):
    venta=Venta.objects.get(id_venta=codigo)
    return render(request,"editarventa.html",{"misventas":venta})

def editarVenta(request):
    id_venta=request.POST["txtcodigo"]
    id_usuario=request.POST["numiduser"]
    id_producto=request.POST["numidproducto"]
    id_servicio=request.POST["numidservicio"]
    precio=request.POST["numprecio"]
    estado=request.POST["txtestado"]
    entrega=request.POST["txtentrega"]
    metodo_pago=request.POST["txtmetodopago"]
    direccion_envio=request.POST["txtdireccionenvio"]
    venta=Venta.objects.get(id_venta=id_venta)
    venta.id_usuario=id_usuario
    venta.id_producto=id_producto
    venta.id_servicio=id_servicio
    venta.precio=precio
    venta.estado=estado
    venta.entrega=entrega
    venta.metodo_pago=metodo_pago
    venta.direccion_envio=direccion_envio
    
    venta.save() # guarda registro actualizado
    return redirect("venta")

def borrarVenta(request,codigo):
    venta=Venta.objects.get(id_venta=codigo)
    venta.delete() # borra el registro
    return redirect("venta")