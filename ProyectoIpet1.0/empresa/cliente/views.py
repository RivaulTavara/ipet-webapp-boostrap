from django.shortcuts import render
from .models import Cliente
# Create your views here.
def index(request):
    cliente = Cliente.objects.all() # select * from cliente
    context = {"cliente":cliente}
    print(cliente)
    return render(request, 'index.html', context)

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


