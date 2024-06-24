import random
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Carrito, UserAuth, Producto, listaDeseos, Categoria, Marca 
from .carrito import Carrito
from .listaDeseos import listaDeseos
from .utils import validar_rut


#VISTA GENERAL 

def generar_numero_aleatorio():
    rango = range(1000000, 9999999)  # Cambiado a 7 dígitos
    while True:
        numero_aleatorio = random.choice(rango)
        if not Producto.objects.filter(codigo=numero_aleatorio).exists():
            return numero_aleatorio

@login_required
def modoAdmin(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    admins = User.objects.filter(is_staff=True)  # Obtiene todos los usuarios que son administradores
    context = {"admins": admins}
    print(admins)
    return render(request, 'modoAdmin.html', context)

@login_required
def registroProducto(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    clientes = User.objects.all()  # Obtiene todos los usuarios
    context = {"clientes": clientes}
    print(clientes)
    return render(request, 'registroProducto.html', {'marcas': marcas, 'categorias': categorias})
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

def index(request):
    # Obtiene todos los productos
    productos = Producto.objects.all()

    # Obtiene 5 productos al azar
    randomprod = Producto.objects.order_by('?')[:5]

    lista_deseos = request.session.get('listaDeseos', {})

    # Para cada producto, verifica si su ID está en la lista de deseos
    for producto in productos:
        producto.en_lista_deseos = str(producto.id) in lista_deseos
        if producto.precio_Oferta:
            descuento = (producto.precio - producto.precio_Oferta) / producto.precio * 100
            producto.descuento = round(descuento)

    # Pasa ambos conjuntos de productos a la plantilla
    return render(request, 'index.html', {'productos': productos, 'randomprod': randomprod})

def producto_detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'producto_Detalle.html', {'producto': producto})


@login_required
def listadeseos(request):
    lista = listaDeseos(request)
    productos = Producto.objects.all()
    return render(request, 'listaDeseos.html', {'productos': productos, 'lista': lista})

@login_required
def carrito(request):
    carrito = Carrito(request)
    productos = Producto.objects.all()
    total = sum(int(producto['precio_unitario']) * producto['cantidad'] for producto in carrito.carrito.values())
    tot_cant=sum(int(producto['cantidad']) for producto in carrito.carrito.values())
    return render(request, 'carrito.html', {'productos': productos, 'carrito': carrito, 'total': total, 'tot_cant': tot_cant})


def restablecercon(request):
    cliente = UserAuth.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'restablecercon.html', context)

def registro(request):
    cliente = UserAuth.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'registro.html', context)

@login_required
def registroCategoria(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    clientes = User.objects.all()  # Obtiene todos los usuarios
    context = {"clientes": clientes}
    return render(request, 'registroCategoria.html', context)

@login_required
def listarCategoria(request):
    listado = Categoria.objects.all()
    context = {'listado': listado}
    return render(request, 'listarCategoria.html', context)

@login_required
def registroMarca(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    clientes = User.objects.all()  # Obtiene todos los usuarios
    context = {"clientes": clientes}
    return render(request, 'registroMarca.html', context)

@login_required
def listarMarca(request):
    listado = Marca.objects.all()
    context = {'listado': listado}
    return render(request, 'listarMarca.html', context)



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











#VISTA USUARIO

@login_required
def gestionarListaDeseos(request, accion, producto_id=None, redirigir=None):
    lista = listaDeseos(request)
    producto = None
    if producto_id is not None:
        producto = Producto.objects.get(id=producto_id)
        imagen_url = str(producto.imagen.url)
        if imagen_url.startswith('/'):
            imagen_url = imagen_url[1:]

    if accion == 'agregar':
        lista.agregar(producto=producto, imagen_url=imagen_url)
    elif accion == 'eliminar':
        lista.eliminar(producto=producto)
        lista.guardar_listaDeseos()
    elif accion == 'limpiar':
        lista.limpiar_listaDeseos()

    if redirigir == 'index':
        return redirect('index')
    elif redirigir == 'listadeseos':
        return redirect('listadeseos')
    else:
        return redirect('index')
    


@login_required
def gestionarCarrito(request, accion, producto_id=None, redirigir=None):
    carrito = Carrito(request)
    producto = None
    if producto_id is not None:
        producto = Producto.objects.get(id=producto_id)
        imagen_url = str(producto.imagen.url)
        if imagen_url.startswith('/'):
            imagen_url = imagen_url[1:]

    cantidad = request.GET.get('cantidad', 1)  # obtiene la cantidad de los parámetros de la URL, por defecto es 1 si no se proporciona

    if accion == 'agregar':
        for _ in range(int(cantidad)):
            carrito.agregar(producto=producto, imagen_url=imagen_url)
    elif accion == 'eliminar':
        carrito.eliminar(producto=producto)
    elif accion == 'restar':
        carrito.restar(producto=producto)
    elif accion == 'limpiar':
        carrito.limpiar_carrito()

    if redirigir == 'index':
        return redirect('index')
    elif redirigir == 'carrito':
        return redirect('carrito')
    else:
        return redirect('carrito')











#VISTA ADMINISTRADOR


@login_required
def guardarProducto(request):
    context = {}
    context['marcas'] = Marca.objects.all()
    context['categorias'] = Categoria.objects.all()
    if request.method == 'POST':
        id = request.POST.get('txtId')
        nombre = request.POST['txtNombre']
        marca_id = request.POST['txtMarca']
        descripcion = request.POST['txtDescripcion']
        precio_Costo = request.POST['txtPrecioCosto']
        precio = request.POST['txtPrecio']
        precio_Oferta = request.POST['txtPrecioOferta']
        stock = request.POST['txtStock']
        fecha = request.POST['txtCreado_en']
        imagen = request.FILES['txtImagen'] if 'txtImagen' in request.FILES else None
        categoria_id = request.POST['txtCategoria']

        marca = Marca.objects.get(pk=marca_id)
        categoria = Categoria.objects.get(pk=categoria_id)

        # Si txtPrecioOferta es una cadena vacía, establece precio_Oferta en None
        if precio_Oferta == '':
            precio_Oferta = None

        if 'btnGuardar' in request.POST:
            if id== '0':
                codigo = generar_numero_aleatorio()
                Producto.objects.create(imagen=imagen, nombre=nombre, marca=marca, descripcion=descripcion, precio_Costo=precio_Costo , precio=precio, precio_Oferta=precio_Oferta, stock=stock, creado_en=fecha, codigo=codigo, categoria=categoria)
                context['exito'] = "Los datos fueron guardados"
            else:
                item = Producto.objects.get(pk=id)
                if imagen:
                    item.imagen = imagen
                item.nombre = nombre
                item.marca = marca
                item.descripcion = descripcion
                item.precio_Costo = precio_Costo
                item.precio = precio
                item.precio_Oferta = precio_Oferta
                item.stock = stock
                item.creado_en = fecha
                item.categoria = categoria
                item.save()
                context['exito'] = "Los datos fueron actualizados"

    return render(request, 'registroProducto.html', context)

@login_required
def gestionarProducto(request, pk, accion):
    context = {}
    try:
        item = Producto.objects.get(pk=pk)
        if accion == 'eliminar':
            item.delete()
            context['exito'] = "El producto fue eliminado"
            return redirect('listarProducto')
        else:  # asumimos que cualquier otra acción es 'buscar'
            context['item'] = item
            return render(request, 'registroProducto.html', context)
    except:
        context['error'] = "Error al buscar el registro"
        return render(request, 'registroProducto.html', context)
@login_required
def guardarUsuario(request):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    context = {}
    if request.method == 'POST':
        rut = request.POST['txtRut']
        if not validar_rut(rut):
            context['error'] = 'El RUT ingresado no es válido.'
            return render(request, 'registroUsuario.html', context)
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

@login_required
def gestionarUsuario(request, pk, accion):
    User = get_user_model()  # Obtiene el modelo de usuario actual (UserAuth)
    context = {}
    try:
        item = User.objects.get(pk=pk)
        if accion == 'eliminar':
            item.delete()
            context['exito'] = "El usuario fue eliminado"
            return redirect('listarUsuario')
        else:  # asumimos que cualquier otra acción es 'buscar'
            context['item'] = item
            return render(request, 'registroUsuario.html', context)
    except:
        context['error'] = "Error al buscar el registro"
        return render(request, 'registroUsuario.html', context)
    

@login_required
def guardarCategoria(request):
    context = {}
    if request.method == 'POST':
        id = request.POST.get('txtId')
        nombre = request.POST['txtNombre']
        is_active = request.POST['txtIsActive'] == 'True'

        if 'btnGuardar' in request.POST:
            if id == '0':
                Categoria.objects.create(nombre=nombre, is_active=is_active)
                context['exito'] = "Los datos fueron guardados"
            else:
                item = Categoria.objects.get(pk=id)
                item.nombre = nombre
                item.is_active = is_active
                item.save()
                context['exito'] = "Los datos fueron actualizados"

    return render(request, 'registroCategoria.html', context)

@login_required
def gestionarCategoria(request, pk, accion):
    context = {}
    try:
        item = Categoria.objects.get(pk=pk)
        if accion == 'eliminar':
            item.delete()
            context['exito'] = "La categoría fue eliminada"
            return redirect('listarCategoria')
        else:  # asumimos que cualquier otra acción es 'buscar'
            context['item'] = item
            return render(request, 'registroCategoria.html', context)
    except:
        context['error'] = "Error al buscar el registro"
        return render(request, 'registroCategoria.html', context)

@login_required
def guardarMarca(request):
    context = {}
    if request.method == 'POST':
        id = request.POST.get('txtId')
        nombre = request.POST['txtNombre']
        is_active = request.POST['txtIsActive'] == 'True'

        if 'btnGuardar' in request.POST:
            if id == '0':
                Marca.objects.create(nombre=nombre, is_active=is_active)
                context['exito'] = "Los datos fueron guardados"
            else:
                item = Marca.objects.get(pk=id)
                item.nombre = nombre
                item.is_active = is_active
                item.save()
                context['exito'] = "Los datos fueron actualizados"

    return render(request, 'registroMarca.html', context)

@login_required
def gestionarMarca(request, pk, accion):
    context = {}
    try:
        item = Marca.objects.get(pk=pk)
        if accion == 'eliminar':
            item.delete()
            context['exito'] = "La categoría fue eliminada"
            return redirect('listarMarca')
        else:  # asumimos que cualquier otra acción es 'buscar'
            context['item'] = item
            return render(request, 'registroMarca.html', context)
    except:
        context['error'] = "Error al buscar el registro"
        return render(request, 'registroMarca.html', context)