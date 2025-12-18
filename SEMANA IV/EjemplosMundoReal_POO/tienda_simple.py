# Ejemplo del mundo real: Tienda simple
# Aplicación de Programación Orientada a Objetos (POO)

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Carrito:
    def __init__(self):
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        producto.stock -= cantidad
        self.total += producto.precio * cantidad
        print(f"Se agregó {cantidad} unidades de {producto.nombre}")


# --- PROGRAMA PRINCIPAL ---
arroz = Producto("Arroz", 49.50, 10)
carrito = Carrito()

print("=== TIENDA SIMPLE ===")

compra_realizada = False

while not compra_realizada:
    print(f"Stock disponible de arroz: {arroz.stock}")
    cantidad = int(input("Ingrese la cantidad de arroz a comprar: "))

    if arroz.stock >= cantidad:
        carrito.agregar_producto(arroz, cantidad)
        print("Compra realizada con éxito.")
        compra_realizada = True
    else:
        print("No hay suficiente stock, intente nuevamente.\n")

print("Total a pagar:", carrito.total)
