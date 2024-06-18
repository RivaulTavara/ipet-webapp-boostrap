class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            self.carrito = self.session['carrito'] = {}
        else:
            self.carrito = carrito

    def agregar(self, producto, imagen_url=None):
        id = str(producto.id)
        if imagen_url is None:
            imagen_url = producto.imagen.url
        if id not in self.carrito.keys():
            self.carrito[id] = {
                'imagen': imagen_url,
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio_unitario': producto.precio,  # Guarda el precio unitario
                'cantidad': 1,
            }
        else:
            self.carrito[id]['cantidad'] += 1
        self.guardar_carrito()
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
    

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            if self.carrito[id]['cantidad'] < 1:
                self.eliminar(producto)
            else:
                self.carrito[id]['precio'] = self.carrito[id]['precio_unitario'] * self.carrito[id]['cantidad']
            self.guardar_carrito()
            
    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True