from django.shortcuts import render
from .models import Cliente,Producto
from datetime import datetime

# Create your views here.
def index(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'index.html', context)

def modoAdmin(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'modoAdmin.html', context)

def carrito(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'carrito.html', context)

def inicioSesion(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'inicioSesion.html', context)

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

def guardarProducto(request):
    context = {}
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        marca = request.POST['txtMarca']
        descripcion = request.POST['txtDescripcion']
        precio = request.POST['txtPrecio']
        stock = request.POST['txtStock']
        fecha = request.POST['txtCreado_en']

        if 'btnGuardar' in request.POST:
            Producto.objects.create(nombre=nombre, marca=marca, descripcion=descripcion, precio=precio, stock=stock, creado_en=fecha)        
            context['exito'] = "Los datos fueron guardados"

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
