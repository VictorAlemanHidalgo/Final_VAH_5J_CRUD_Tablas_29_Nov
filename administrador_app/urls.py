from django.urls import path
from administrador_app import views

urlpatterns = [
    path("administrador", views.inicio_vistaAdministrador, name="administrador"),
    path("registrarAdministrador/",views.registrarAdministrador,name="registrarAdministrador"),
    path("seleccionarAdministrador/<codigo>",views.seleccionarAdministrador,name="seleccionarAdministrador"),
    path("editarAdministrador/",views.editarAdministrador,name="editarAdministrador"),
    path("borrarAdministrador/<codigo>",views.borrarAdministrador,name="borrarAdministrador"),

]