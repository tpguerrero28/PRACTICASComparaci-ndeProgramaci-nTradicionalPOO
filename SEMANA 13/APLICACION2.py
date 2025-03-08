import tkinter as tk
from tkinter import messagebox


# Función para agregar la información
def agregar():
    # Obtener los valores de los campos de texto
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    direccion = entry_direccion.get()

    # Verificar que todos los campos estén completos
    if nombre and edad and correo and direccion:
        # Agregar la información a la lista
        datos = f"Nombre: {nombre}, Edad: {edad}, Correo: {correo}, Dirección: {direccion}"
        listbox.insert(tk.END, datos)

        # Limpiar los campos de texto
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
    else:
        # Mostrar un mensaje si algún campo está vacío
        messagebox.showwarning("Advertencia", "Por favor, ingresa todos los datos.")



# Función para limpiar los campos y la lista
def limpiar():
    # Limpiar los campos de texto
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

    # Limpiar la lista
    listbox.delete(0, tk.END)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Información")

# Crear la etiqueta de título
label_titulo = tk.Label(ventana, text="Formulario de Registro", font=("times new roman", 18))
label_titulo.pack(pady=10)

# Crear la etiqueta y el campo para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack(pady=5)

# Crear la etiqueta y el campo para la edad
label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack(pady=5)
entry_edad = tk.Entry(ventana, width=40)
entry_edad.pack(pady=5)

# Crear la etiqueta y el campo para el correo
label_correo = tk.Label(ventana, text="Correo Electrónico:")
label_correo.pack(pady=5)
entry_correo = tk.Entry(ventana, width=40)
entry_correo.pack(pady=5)

# Crear la etiqueta y el campo para la dirección
label_direccion = tk.Label(ventana, text="Dirección:")
label_direccion.pack(pady=5)
entry_direccion = tk.Entry(ventana, width=40)
entry_direccion.pack(pady=5)

# Crear el botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=10)

# Crear el botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Crear la lista (Listbox) para mostrar los datos
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()


