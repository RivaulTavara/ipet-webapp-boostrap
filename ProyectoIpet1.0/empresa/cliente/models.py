from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=9, unique=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    nivel_educacional = models.CharField(max_length=255, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    ultimo_login = models.DateTimeField(blank=True, null=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    creado_en = models.DateField()
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Pedido ' + str(self.id) + ' - ' + str(self.Cliente)

class Carrito(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return 'Item ' + str(self.id) + ' - ' + str(self.producto)
