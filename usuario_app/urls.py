from django.urls import path
from usuario_app import views

urlpatterns = [
    path("usuario", views.inicio_vistaUsuario, name="usuario"),
    path("registrarUsuario/",views.registrarUsuario,name="registrarUsuario"),
    path("seleccionarUsuario/<codigo>",views.seleccionarUsuario,name="seleccionarUsuario"),
    path("editarUsuario/",views.editarUsuario,name="editarUsuario"),
    path("borrarUsuario/<codigo>",views.borrarUsuario,name="borrarUsuario"),

]