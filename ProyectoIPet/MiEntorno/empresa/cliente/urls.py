from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('carrito', views.carrito, name='carrito'), 
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('registro', views.registro, name='registro'),
    path('restablecercon', views.restablecercon, name='restablecercon'),
    path('usuario', views.usuario, name='usuario'),   
            ]