from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('index', views.index, name='index'),
    path('modoAdmin', views.modoAdmin, name='modoAdmin'), 
    path('carrito', views.carrito, name='carrito'), 
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('restablecercon', views.restablecercon, name='restablecercon'),
    path('registro', views.registro, name='registro'),
    path('usuario', views.usuario, name='usuario'),   
    path('registroProducto', views.registroProducto, name='registroProducto'),
    path('registroCliente', views.registroCliente, name='registroCliente'),
    path('guardarProducto', views.guardarProducto, name='guardarProducto'),
    path('guardarCliente', views.guardarCliente, name='guardarCliente'),
    path('listarProducto', views.listarProducto, name='listarProducto'),
    path('listarCliente', views.listarCliente, name='listarCliente'),
    path('buscarProducto/<str:pk>', views.buscarProducto, name='buscarProducto'),
    path('buscarCliente/<str:pk>', views.buscarCliente, name='buscarCliente'), 
    path('eliminarProducto/<str:pk>', views.eliminarProducto, name='eliminarProducto'),
    path('eliminarCliente/<str:pk>', views.eliminarCliente, name='eliminarCliente'),
    path('agregarAlCarrito/<int:producto_id>', views.agregarAlCarrito, name='agregarAlCarrito'),    
    path('agregarAlCarritoYRedirigir/<int:producto_id>', views.agregarAlCarritoYRedirigir, name='agregarAlCarritoYRedirigir'),
    path('agregarProductoCarrito/<int:producto_id>', views.agregarProductoCarrito, name='agregarProductoCarrito'),
    path('eliminarProductoCarrito/<int:producto_id>', views.eliminarProductoCarrito, name='eliminarProductoCarrito'),
    path('restarProductoCarrito/<int:producto_id>', views.restarProductoCarrito, name='restarProductoCarrito'),
    path('limpiarCarrito', views.limpiarCarrito, name='limpiarCarrito')
            ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
