class Producto:
    def __init__(self, nombre, precio):
        """Inicializa un producto con un nombre y un precio."""
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        """Representación en cadena del producto."""
        return f"{self.nombre} - ${self.precio:.2f}"


class CarritoDeCompras:
    def __init__(self):
        """Inicializa el carrito de compras vacío."""
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto al carrito."""
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def calcular_total(self):
        """Calcula el total de los productos en el carrito."""
        total = sum(producto.precio for producto in self.productos)
        return total

    def mostrar_carrito(self):
        """Muestra los productos en el carrito y el total."""
        print("\nCarrito de Compras:")
        for producto in self.productos:
            print(producto)
        print(f"Total: ${self.calcular_total():.2f}")


# Crear productos
producto1 = Producto("leche", 1.9)
producto2 = Producto("huevos", 4.5)
producto3 = Producto("Pan", 1.5)
producto4 = Producto("mantequilla", 3.75)

# Crear el carrito de compras
carrito = CarritoDeCompras()

# Agregar productos al carrito
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

# Mostrar el carrito y el total
carrito.mostrar_carrito()