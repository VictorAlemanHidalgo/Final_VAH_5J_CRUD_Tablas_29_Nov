from django.urls import path
from servicio_app import views

urlpatterns = [
    path("servicio", views.inicio_vistaServicio, name="servicio"),
    path("registrarServicio/",views.registrarServicio,name="registrarServicio"),
    path("seleccionarServicio/<codigo>",views.seleccionarServicio,name="seleccionarServicio"),
    path("editarServicio/",views.editarServicio,name="editarServicio"),
    path("borrarServicio/<codigo>",views.borrarServicio,name="borrarServicio"),

]