from django.urls import path
from distribuidor_app import views

urlpatterns = [
    path("distribuidor", views.inicio_vistaDistribuidor, name="distribuidor"),
    path("registrarDistribuidor/",views.registrarDistribuidor,name="registrarDistribuidor"),
    path("seleccionarDistribuidor/<codigo>",views.seleccionarDistribuidor,name="seleccionarDistribuidor"),
    path("editarDistribuidor/",views.editarDistribuidor,name="editarDistribuidor"),
    path("borrarDistribuidor/<codigo>",views.borrarDistribuidor,name="borrarDistribuidor"),

]