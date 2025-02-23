import pickle


# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener atributos
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Métodos para establecer atributos
    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        # Usamos un diccionario para almacenar los productos, donde la clave es el ID
        self.productos = {}

    def agregar_producto(self, producto):
        # Agrega un nuevo producto al inventario
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        # Elimina un producto por ID
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza cantidad o precio de un producto
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        # Busca productos por nombre
        productos_encontrados = [producto for producto in self.productos.values() if
                                 nombre.lower() in producto.obtener_nombre().lower()]
        return productos_encontrados

    def mostrar_productos(self):
        # Muestra todos los productos del inventario
        if not self.productos:
            print("El inventario está vacío.")
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        # Guarda el inventario en un archivo usando pickle
        with open(archivo, 'wb') as file:
            pickle.dump(self.productos, file)

    def cargar_inventario(self, archivo):
        # Carga el inventario desde un archivo usando pickle
        try:
            with open(archivo, 'rb') as file:
                self.productos = pickle.load(file)
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará un nuevo inventario.")


# Función para mostrar el menú
def mostrar_menu():
    print("\n---- TANIA GUERRERO MORA ----")
    print("\n---- Menú de Gestión de Inventario ----")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Guardar Inventario")
    print("7. Cargar Inventario")
    print("8. Salir")


# Función principal
def main():
    inventario = Inventario()
    archivo_inventario = "inventario.pkl"

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Agregar Producto
            id_producto = input("ID del Producto: ")
            nombre = input("Nombre del Producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado.")

        elif opcion == '2':
            # Eliminar Producto
            id_producto = input("ID del Producto a Eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            # Actualizar Producto
            id_producto = input("ID del Producto a Actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")
            precio = input("Nuevo precio (deja vacío para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            # Buscar Producto
            nombre = input("Nombre del Producto a Buscar: ")
            productos_encontrados = inventario.buscar_producto_por_nombre(nombre)
            if productos_encontrados:
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            # Mostrar Productos
            inventario.mostrar_productos()

        elif opcion == '6':
            # Guardar Inventario
            inventario.guardar_inventario(archivo_inventario)
            print("Inventario guardado.")

        elif opcion == '7':
            # Cargar Inventario
            inventario.cargar_inventario(archivo_inventario)
            print("Inventario cargado.")

        elif opcion == '8':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


# Iniciar el programa
if __name__ == "__main__":
    main()
