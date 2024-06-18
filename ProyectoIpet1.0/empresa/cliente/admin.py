from django.contrib import admin
from .models import Cliente , Producto, Pedido, Carrito

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Carrito)


# ejercicios agregar los otros modelos
# e ingresar 5 filas para cada uno de ellos