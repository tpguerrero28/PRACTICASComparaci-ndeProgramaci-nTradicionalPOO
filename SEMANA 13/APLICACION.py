#import tkinter as tk
from tkinter import messagebox


# Función para agregar información a la lista
def agregar():
    # Obtener el valor del campo de texto
    dato = entry.get()

    # Verificar que el campo no esté vacío
    if dato:
        # Agregar el dato a la lista
        listbox.insert(tk.END, dato)
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        # Mostrar un mensaje si no hay texto
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato.")


# Función para limpiar la lista y el campo de texto
def limpiar():
    entry.delete(0, tk.END)  # Limpiar el campo de texto
    listbox.delete(0, tk.END)  # Limpiar la lista


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Información")

# Crear la etiqueta
label = tk.Label(ventana, text="Ingresa un dato:")
label.pack(pady=10)

# Crear el campo de texto (Entry)
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Crear el botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# Crear el botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Crear la lista (Listbox) para mostrar los datos
listbox = tk.Listbox(ventana, width=40, height=10)
listbox.pack(pady=10)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
