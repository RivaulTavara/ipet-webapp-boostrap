from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from .models import Carrito, UserAuth, Producto, listaDeseos
from .carrito import Carrito
from .listaDeseos import listaDeseos
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout






# Create your views here.
def index(request):
    # Obtiene todos los productos
    productos = Producto.objects.all()

    # Obtiene 5 productos al azar
    randomprod = Producto.objects.order_by('?')[:5]

    lista_deseos = request.session.get('listaDeseos', {})

    # Para cada producto, verifica si su ID está en la lista de deseos
    for producto in productos:
        producto.en_lista_deseos = str(producto.id) in lista_deseos


    for producto in productos:
        if producto.precio_Oferta:
            descuento = (producto.precio - producto.precio_Oferta) / producto.precio * 100
            producto.descuento = round(descuento)

    # Pasa ambos conjuntos de productos a la plantilla
    return render(request, 'index.html', {'productos': productos, 'randomprod': randomprod})


@login_required
def modoAdmin(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    admins = User.objects.filter(is_staff=True)  # Obtiene todos los usuarios que son administradores
    context = {"admins": admins}
    print(admins)
    return render(request, 'modoAdmin.html', context)

def producto_detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'producto_Detalle.html', {'producto': producto})

@login_required
def listadeseos(request):
    lista = listaDeseos(request)
    productos = Producto.objects.all()
    return render(request, 'listaDeseos.html', {'productos': productos, 'lista': lista})

@login_required
def agregarAListaDeseos(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    lista = listaDeseos(request)
    imagen_url = str(producto.imagen.url)
    if imagen_url.startswith('/'):
        imagen_url = imagen_url[1:]
    lista.agregar(producto=producto, imagen_url=imagen_url)
    return redirect('index')

@login_required
def eliminarDeListaDeseosIndex(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    lista = listaDeseos(request)
    lista.eliminar(producto=producto)
    lista.guardar_listaDeseos()
    return redirect('index')

def eliminarDeListaDeseos(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    lista = listaDeseos(request)
    lista.eliminar(producto=producto)
    lista.guardar_listaDeseos()
    return redirect('listadeseos')

def limpiarListaDeseos(request):
    lista = listaDeseos(request)
    lista.limpiar_listaDeseos()
    return redirect('listadeseos')

@login_required
def carrito(request):
    carrito = Carrito(request)
    productos = Producto.objects.all()
    total = sum(int(producto['precio_unitario']) * producto['cantidad'] for producto in carrito.carrito.values())
    tot_cant=sum(int(producto['cantidad']) for producto in carrito.carrito.values())
    return render(request, 'carrito.html', {'productos': productos, 'carrito': carrito, 'total': total, 'tot_cant': tot_cant})

@login_required
def agregarMultiplesAlCarrito(request, producto_id):
    cantidad = request.GET.get('cantidad', 1)  # obtiene la cantidad de los parámetros de la URL, por defecto es 1 si no se proporciona
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    imagen_url = str(producto.imagen.url)
    if imagen_url.startswith('/'):
        imagen_url = imagen_url[1:]
    for _ in range(int(cantidad)):
        carrito.agregar(producto=producto, imagen_url=imagen_url)
    return redirect('carrito')

@login_required
def agregarAlCarrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    imagen_url = str(producto.imagen.url)
    if imagen_url.startswith('/'):
        imagen_url = imagen_url[1:]
    carrito.agregar(producto=producto, imagen_url=imagen_url)
    return redirect('index')

@login_required
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

@login_required
def restablecercon(request):
    cliente = UserAuth.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'restablecercon.html', context)



def inicioSesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:  # Verifica si el usuario es un administrador
                return redirect('modoAdmin')  # Redirige al usuario a la página de administración
            else:
                return redirect('index')  # Redirige al usuario a la página 'home'
        else:
            # Si la autenticación falla, vuelve a renderizar la página de inicio de sesión con un mensaje de error
            context = {"error": "Correo y/o contraseña incorrectos"}
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html')

def exit(request):
    logout(request)
    return redirect('login')


def registro(request):
    cliente = UserAuth.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'registro.html', context)


@login_required
def registroProducto(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    clientes = User.objects.all()  # Obtiene todos los usuarios
    context = {"clientes": clientes}
    print(clientes)
    return render(request, 'registroProducto.html', context)

@login_required
def listarProducto(request):
    listado = Producto.objects.all()
    context = {'listado': listado}
    return render(request, 'listarProducto.html', context)


@login_required
def registroUsuario(request):
    clientes = UserAuth.objects.all()  # Obtiene todos los usuarios
    context = {'clientes': clientes}
    print(clientes)
    return render(request, 'registroUsuario.html', context)

@login_required
def listarUsuario(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    listado = User.objects.all()  # Obtiene todos los usuarios
    context = {'listado': listado}
    return render(request, 'listarUsuario.html', context)


def generar_numero_aleatorio():
    rango = range(1000000, 9999999)  # Cambiado a 7 dígitos
    while True:
        numero_aleatorio = random.choice(rango)
        if not Producto.objects.filter(modelo=numero_aleatorio).exists():
            return numero_aleatorio

@login_required
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
        categoria = request.POST['txtCategoria']

        # Si txtPrecioOferta es una cadena vacía, establece precio_Oferta en None
        if precio_Oferta == '':
            precio_Oferta = None

        if 'btnGuardar' in request.POST:
            if id== '0':
                modelo = generar_numero_aleatorio()
                Producto.objects.create(imagen=imagen, nombre=nombre, marca=marca, descripcion=descripcion, precio=precio, precioOferta=precio_Oferta, stock=stock, creado_en=fecha, modelo=modelo, categoria=categoria)        
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
                item.categoria = categoria
                item.save()
                context['exito'] = "Los datos fueron actualizados"

    return render(request, 'registroProducto.html', context)

@login_required
def buscarProducto(request, pk):
    context = {}
    try:
        item = Producto.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'registroProducto.html', context)

@login_required
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






def guardarUsuario(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    context = {}
    if request.method == 'POST':
        rut = request.POST['txtRut']
        email = request.POST['txtCorreo']
        contrasena = request.POST['txtContrasena']
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        direccion = request.POST['txtDireccion']
        fecha_de_nacimiento = request.POST['txtFecha']
        telefono = request.POST['txtTelefono']
        region = request.POST['txtRegion']
        nivel_educacional = request.POST['txtNivel_Educacional']
        es_admin = 'chkEsAdmin' in request.POST  # Verifica si el checkbox 'chkAdmin' está marcado

        if 'btnGuardar' in request.POST:
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                user.email = email
                user.rut = rut
                user.set_password(contrasena)
                user.first_name = nombre
                user.last_name = apellido
                user.direccion = direccion
                user.fecha_de_nacimiento = fecha_de_nacimiento
                user.telefono = telefono
                user.region = region
                user.nivel_educacional = nivel_educacional
                user.last_login = timezone.now()  # Actualiza el último inicio de sesión del usuario
                user.is_staff = es_admin  # Actualiza el estado de administrador del usuario
                user.save()
                context['exito'] = "Los datos fueron actualizados"
            else:
                user = User.objects.create_user(email=email, rut=rut, password=contrasena, first_name=nombre, last_name=apellido, direccion=direccion, fecha_de_nacimiento=fecha_de_nacimiento, telefono=telefono, region=region, nivel_educacional=nivel_educacional, last_login=timezone.now(), is_staff=es_admin)
                context['exito'] = "Los datos fueron guardados"

    return render(request, 'registroUsuario.html', context)

def buscarUsuario(request, pk):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    context = {}
    try:
        item = User.objects.get(pk=pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'registroUsuario.html', context)

def eliminarUsuario(request, pk):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    context = {}
    try:
        item = User.objects.get(pk=pk)
        item.delete()
        context['exito'] = "El usuario fue eliminado"
    except:
        context['error'] = "El usuario NO fue eliminado"

    return redirect('listarUsuario')