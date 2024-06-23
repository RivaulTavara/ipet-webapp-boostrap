from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('logout/', views.exit, name='logout'),
    path('login/', views.inicioSesion, name='login'),
    path('index', views.index, name='index'),
    path('modoAdmin', views.modoAdmin, name='modoAdmin'), 
    path('carrito', views.carrito, name='carrito'), 
    path('restablecercon', views.restablecercon, name='restablecercon'),
    path('registro', views.registro, name='registro'),
    path('producto_detalle/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),    
    path('listaDeseos', views.listadeseos, name='listadeseos'),
    path('agregarAListaDeseos/<int:producto_id>', views.agregarAListaDeseos, name='agregarAListaDeseos'),
    path('eliminarDeListaDeseos/<int:producto_id>', views.eliminarDeListaDeseos, name='eliminarDeListaDeseos'),
    path('eliminarDeListaDeseosIndex/<int:producto_id>', views.eliminarDeListaDeseosIndex, name='eliminarDeListaDeseosIndex'),
    path('limpiarListaDeseos', views.limpiarListaDeseos, name='limpiarListaDeseos'),
    path('registroProducto', views.registroProducto, name='registroProducto'),
    path('registroUsuario', views.registroUsuario, name='registroUsuario'),
    path('guardarProducto', views.guardarProducto, name='guardarProducto'),
    path('guardarUsuario', views.guardarUsuario, name='guardarUsuario'),
    path('listarProducto', views.listarProducto, name='listarProducto'),
    path('listarUsuario', views.listarUsuario, name='listarUsuario'),
    path('buscarProducto/<str:pk>', views.buscarProducto, name='buscarProducto'),
    path('buscarUsuario/<str:pk>', views.buscarUsuario, name='buscarUsuario'), 
    path('eliminarProducto/<str:pk>', views.eliminarProducto, name='eliminarProducto'),
    path('eliminarUsuario/<str:pk>', views.eliminarUsuario, name='eliminarUsuario'),
    path('agregarAlCarrito/<int:producto_id>', views.agregarAlCarrito, name='agregarAlCarrito'),    
    path('agregarAlCarritoYRedirigir/<int:producto_id>', views.agregarAlCarritoYRedirigir, name='agregarAlCarritoYRedirigir'),
    path('agregarMultiplesAlCarrito/<int:producto_id>', views.agregarMultiplesAlCarrito, name='agregarMultiplesAlCarrito'),
    path('agregarProductoCarrito/<int:producto_id>', views.agregarProductoCarrito, name='agregarProductoCarrito'),
    path('eliminarProductoCarrito/<int:producto_id>', views.eliminarProductoCarrito, name='eliminarProductoCarrito'),
    path('restarProductoCarrito/<int:producto_id>', views.restarProductoCarrito, name='restarProductoCarrito'),
    path('limpiarCarrito', views.limpiarCarrito, name='limpiarCarrito')
            ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
