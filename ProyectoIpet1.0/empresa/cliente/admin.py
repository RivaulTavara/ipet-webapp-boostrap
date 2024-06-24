from django.contrib import admin
from .models import  UserAuth , Producto, Pedido, Carrito, listaDeseos, Categoria, Marca, FormaDePago

# Register your models here.
admin.site.register(UserAuth)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(listaDeseos)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(FormaDePago)


# ejercicios agregar los otros modelos
# e ingresar 5 filas para cada uno de ellos