class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Los atributos de 'titulo' y 'autor' son tuplas porque son inmutables.
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista que guarda los libros prestados al usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro {libro.titulo} no está prestado a este usuario.")

    def listar_libros_prestados(self):
        if self.libros_prestados:
            return [libro.titulo for libro in self.libros_prestados]
        else:
            return "No tiene libros prestados."


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto que asegura que los IDs de usuario sean únicos

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro {libro.titulo} añadido a la biblioteca.")
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
            print(f"Usuario {usuario.nombre} registrado.")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn, None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            usuario.prestar_libro(libro)
            print(f"Libro {libro.titulo} prestado a {usuario.nombre}.")
        else:
            print("No se pudo realizar el préstamo. Verifique los datos.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn, None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            usuario.devolver_libro(libro)
            print(f"Libro {libro.titulo} devuelto por {usuario.nombre}.")
        else:
            print("No se pudo realizar la devolución. Verifique los datos.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            return usuario.listar_libros_prestados()
        else:
            return "Usuario no encontrado."


# Ejemplo:

# Creación de la biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
libro1 = Libro("Python para todos", "Charles Severance", "Programación", "978-0-13-454136-6")
libro2 = Libro("Ciencia de datos con Python", "Jake VanderPlas", "Ciencia de Datos", "978-1-4493-8823-2")

biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Leila MUÑOZ", 1)
usuario2 = Usuario("Valeska Guerrero", 2)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("978-0-13-454136-6", 1)
biblioteca.devolver_libro("978-0-13-454136-6", 1)

# Buscar libros
biblioteca.buscar_libro("titulo", "python")

# Listar libros prestados
print(usuario1.listar_libros_prestados())

# Dar de baja usuario
biblioteca.dar_de_baja_usuario(1)
