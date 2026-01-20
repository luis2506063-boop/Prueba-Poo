class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def mostrar_producto(self):
        print(self.nombre, self.cantidad, self.precio)

