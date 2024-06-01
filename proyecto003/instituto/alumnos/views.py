from django.shortcuts import render
from .models import Alumno
# Create your views here.
def index(request):
    alumnos = Alumno.objects.all() # select * from alumno
    context = {"alumnos":alumnos}
    print(alumnos)
    return render(request, 'index.html', context)

def carrito(request):
    alumnos = Alumno.objects.all() # select * from alumno
    context = {"alumnos":alumnos}
    print(alumnos)
    return render(request, 'carrito.html', context)

def inicioSesion(request):
    alumnos = Alumno.objects.all() # select * from alumno
    context = {"alumnos":alumnos}
    print(alumnos)
    return render(request, 'inicioSesion.html', context)

def registro(request):
    alumnos = Alumno.objects.all() # select * from alumno
    context = {"alumnos":alumnos}
    print(alumnos)
    return render(request, 'registro.html', context)

def restablecercon(request):
    alumnos = Alumno.objects.all() # select * from alumno
    context = {"alumnos":alumnos}
    print(alumnos)
    return render(request, 'restablecercon.html', context)

def usuario(request):
    alumnos = Alumno.objects.all() # select * from alumno
    context = {"alumnos":alumnos}
    print(alumnos)
    return render(request, 'usuario.html', context)

def listarAlumnos(request):
    alumnos = Alumno.objects.all()
    context={'alumnos': alumnos}
    return render (request, 'index.html', context)

def PlantillaBase(request):
    alumnos = Alumno.objects.all()
    context={'alumnos': alumnos}
    return render (request, 'PlantillaBase.html', context)