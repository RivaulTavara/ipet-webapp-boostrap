from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Carrito, Cliente,Producto, listaDeseos
from .carrito import Carrito
from .listaDeseos import listaDeseos


# Create your views here.
def index(request):
    # Obtiene todos los productos
    productos = Producto.objects.all()

    # Obtiene 5 productos al azar
    randomprod = Producto.objects.order_by('?')[:5]

    for producto in productos:
        if producto.precio_Oferta:
            descuento = (producto.precio - producto.precio_Oferta) / producto.precio * 100
            producto.descuento = round(descuento)

    # Pasa ambos conjuntos de productos a la plantilla
    return render(request, 'index.html', {'productos': productos, 'randomprod': randomprod})

def modoAdmin(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'modoAdmin.html', context)

def listadeseos(request):
    lista = listaDeseos(request)
    productos = Producto.objects.all()
    return render(request, 'listaDeseos.html', {'productos': productos, 'lista': lista})

def agregarAListaDeseos(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    lista = listaDeseos(request)
    imagen_url = str(producto.imagen.url)
    if imagen_url.startswith('/'):
        imagen_url = imagen_url[1:]
    lista.agregar(producto=producto, imagen_url=imagen_url)
    return redirect('index')

def eliminarDeListaDeseos(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    lista = listaDeseos(request)
    lista.eliminar(producto=producto)
    lista.guardar_listaDeseos()
    return redirect('listaDeseos')

def limpiarListaDeseos(request):
    lista = listaDeseos(request)
    lista.limpiar_listaDeseos()
    return redirect('listaDeseos')


def carrito(request):
    carrito = Carrito(request)
    productos = Producto.objects.all()
    total = sum(int(producto['precio_unitario']) * producto['cantidad'] for producto in carrito.carrito.values())
    tot_cant=sum(int(producto['cantidad']) for producto in carrito.carrito.values())
    return render(request, 'carrito.html', {'productos': productos, 'carrito': carrito, 'total': total, 'tot_cant': tot_cant})

def agregarAlCarrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    imagen_url = str(producto.imagen.url)
    if imagen_url.startswith('/'):
        imagen_url = imagen_url[1:]
    carrito.agregar(producto=producto, imagen_url=imagen_url)
    return redirect('index')

def agregarAlCarritoYRedirigir(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    imagen_url = str(producto.imagen.url)
    if imagen_url.startswith('/'):
        imagen_url = imagen_url[1:]
    carrito.agregar(producto=producto, imagen_url=imagen_url)
    return redirect('carrito')

def agregarProductoCarrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    carrito.agregar(producto=producto)
    return redirect('carrito')

def eliminarProductoCarrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    carrito.eliminar(producto=producto)
    return redirect('carrito')

def restarProductoCarrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    carrito.restar(producto=producto)
    return redirect('carrito')

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect('carrito')


def inicioSesion(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'inicioSesion.html', context)

def restablecercon(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'restablecercon.html', context)

def usuario(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'usuario.html', context)

def registro(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'registro.html', context)

def registroProducto(request):
    cliente = Cliente.objects.all()
    context = {"cliente": cliente}
    print(cliente)
    return render(request, 'registroProducto.html', context)

def listarProducto(request):
    listado = Producto.objects.all()
    context = {'listado': listado}
    return render(request, 'listarProducto.html', context)

def registroCliente(request):
    cliente = Cliente.objects.all()
    context = {'cliente': cliente}
    print(cliente)
    return render(request, 'registroCliente.html', context)

def listarCliente(request):
    listado = Cliente.objects.all()
    context = {'listado': listado}
    return render(request, 'listarCliente.html', context)

def guardarProducto(request):
    context = {}
    if request.method == 'POST':
        id = request.POST.get('txtId')
        nombre = request.POST['txtNombre']
        marca = request.POST['txtMarca']
        descripcion = request.POST['txtDescripcion']
        precio = request.POST['txtPrecio']
        precio_Oferta = request.POST['txtPrecioOferta']
        stock = request.POST['txtStock']
        fecha = request.POST['txtCreado_en']
        imagen = request.FILES['txtImagen'] if 'txtImagen' in request.FILES else None

        # Si txtPrecioOferta es una cadena vacía, establece precio_Oferta en None
        if precio_Oferta == '':
            precio_Oferta = None

        if 'btnGuardar' in request.POST:
            if id== '0':
                Producto.objects.create(imagen=imagen, nombre=nombre, marca=marca, descripcion=descripcion, precio=precio, precioOferta=precio_Oferta, stock=stock, creado_en=fecha)        
                context['exito'] = "Los datos fueron guardados"
            else:
                item = Producto.objects.get(pk=id)
                if imagen:
                    item.imagen = imagen
                item.nombre = nombre
                item.marca = marca
                item.descripcion = descripcion
                item.precio = precio
                item.precio_Oferta = precio_Oferta
                item.stock = stock
                item.creado_en = fecha
                item.save()
                context['exito'] = "Los datos fueron actualizados"

    return render(request, 'registroProducto.html', context)

def buscarProducto(request, pk):
    context = {}
    try:
        item = Producto.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'registroProducto.html', context)

def eliminarProducto(request, pk):
    context = {}
    try:
        item = Producto.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Producto.objects.all()
    return render(request, 'listarProducto.html', context)




def guardarCliente(request):
    context = {}
    if request.method == 'POST':
        rut = request.POST['txtRut']
        correo = request.POST['txtCorreo']
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        contrasena = request.POST['txtContrasena']
        direccion = request.POST['txtDireccion']
        fecha_de_nacimiento = request.POST['txtFecha']
        telefono = request.POST['txtTelefono']
        region = request.POST['txtRegion']
        nivel_educacional = request.POST['txtNivel_Educacional']
        creado_en = timezone.now()
        ultimo_login =  timezone.now()

        if 'btnGuardar' in request.POST:
            if Cliente.objects.filter(rut=rut).exists():
                item = Cliente.objects.get(rut=rut)
                item.correo = correo
                item.nombre = nombre
                item.apellido = apellido
                item.contrasena = contrasena
                item.direccion = direccion
                item.fecha_de_nacimiento = fecha_de_nacimiento
                item.region = region
                item.nivel_educacional = nivel_educacional
                item.creado_en = creado_en
                item.ultimo_login = ultimo_login
                item.save()
                context['exito'] = "Los datos fueron actualizados"
            else:
                Cliente.objects.create(rut=rut, correo=correo, nombre=nombre, apellido=apellido, contrasena=contrasena, direccion=direccion, fecha_de_nacimiento=fecha_de_nacimiento, telefono=telefono, region=region, nivel_educacional=nivel_educacional, creado_en=creado_en, ultimo_login=ultimo_login)
                context['exito'] = "Los datos fueron guardados"

    return render(request, 'registroCliente.html', context)

def buscarCliente(request, pk):
    context = {}
    try:
        item = Cliente.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'registroCliente.html', context)

def eliminarCliente(request, pk):
    context = {}
    try:
        item = Cliente.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Cliente.objects.all()
    return redirect('listarCliente')

