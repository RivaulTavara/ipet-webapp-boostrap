from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('carrito', views.carrito, name='carrito'), 
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('registro', views.registro, name='registro'),
    path('registroProducto', views.registroProducto, name='registroProducto'),
    path('guardarProducto', views.guardarProducto, name='guardarProducto'),
    path('listarProducto', views.listarProducto, name='listarProducto'),
    path('restablecercon', views.restablecercon, name='restablecercon'),
    path('buscarProducto/<str:pk>', views.buscarProducto, name='buscarProducto'), 
    path('eliminarProducto/<str:pk>', views.eliminarProducto, name='eliminarProducto'),
    path('modoAdmin', views.modoAdmin, name='modoAdmin'), 
    path('usuario', views.usuario, name='usuario'),   
            ]