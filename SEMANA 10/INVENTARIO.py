import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Cargar los productos desde el archivo de texto al iniciar."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as file:
                    for line in file:
                        datos = line.strip().split(",")
                        if len(datos) == 4:
                            producto = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))
                            self.productos.append(producto)
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al leer el archivo: {e}")
            except Exception as e:
                print(f"Se produjo un error inesperado al cargar el inventario: {e}")
        else:
            print("El archivo no existe, se creará uno nuevo.")

    def guardar_inventario(self):
        """Guardar el inventario en el archivo de texto."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(str(producto) + "\n")
            print("Inventario guardado correctamente.")
        except (PermissionError, IOError) as e:
            print(f"Error al guardar el archivo: {e}")

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        """Añadir un nuevo producto al inventario."""
        producto = Producto(codigo, nombre, cantidad, precio)
        self.productos.append(producto)
        self.guardar_inventario()

    def actualizar_producto(self, codigo, cantidad, precio):
        """Actualizar la cantidad o el precio de un producto."""
        encontrado = False
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.cantidad = cantidad
                producto.precio = precio
                encontrado = True
                break
        if encontrado:
            self.guardar_inventario()
            print(f"Producto {codigo} actualizado correctamente.")
        else:
            print(f"Producto {codigo} no encontrado.")

    def eliminar_producto(self, codigo):
        """Eliminar un producto del inventario."""
        self.productos = [producto for producto in self.productos if producto.codigo != codigo]
        self.guardar_inventario()

    def mostrar_inventario(self):
        """Mostrar todos los productos del inventario."""
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(f"Codigo: {producto.codigo}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

# Funciones del programa
def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def ejecutar_programa():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.agregar_producto(codigo, nombre, cantidad, precio)
        elif opcion == "3":
            codigo = input("Ingrese el código del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar_producto(codigo, cantidad, precio)
        elif opcion == "4":
            codigo = input("Ingrese el código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_programa()