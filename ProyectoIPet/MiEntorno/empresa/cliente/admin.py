from django.contrib import admin
from .models import Usuario, Producto, Pedido, ItemPedido

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)


# ejercicios agregar los otros modelos
# e ingresar 5 filas para cada uno de ellos