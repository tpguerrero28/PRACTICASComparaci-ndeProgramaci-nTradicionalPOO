import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar


# Funciones de la aplicación
def agregar_evento():
    fecha = calendario.get_date()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha and hora and descripcion:
        eventos_tree.insert('', 'end', values=(fecha, hora, descripcion))
        entrada_hora.delete(0, 'end')
        entrada_descripcion.delete(0, 'end')
    else:
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos")


def eliminar_evento():
    selected_item = eventos_tree.selection()
    if not selected_item:
        messagebox.showwarning("No seleccionado", "Por favor seleccione un evento para eliminar")
        return

    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este evento?")
    if respuesta:
        eventos_tree.delete(selected_item)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# Crear el Frame principal
frame_principal = tk.Frame(ventana)
frame_principal.pack(pady=20)

# Frame para el calendario y los campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiqueta y calendario
etiqueta_fecha = tk.Label(frame_entrada, text="Selecciona la fecha:")
etiqueta_fecha.grid(row=0, column=0, padx=10, pady=5)

calendario = Calendar(frame_entrada, selectmode="day", date_pattern="yyyy-mm-dd")
calendario.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y campos de entrada (hora y descripción)
etiqueta_hora = tk.Label(frame_entrada, text="Hora:")
etiqueta_hora.grid(row=1, column=0, padx=10, pady=5)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=10, pady=5)

etiqueta_descripcion = tk.Label(frame_entrada, text="Descripción:")
etiqueta_descripcion.grid(row=2, column=0, padx=10, pady=5)
entrada_descripcion = tk.Entry(frame_entrada)
entrada_descripcion.grid(row=2, column=1, padx=10, pady=5)

# Botones
boton_agregar = tk.Button(frame_entrada, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=3, column=0, columnspan=2, pady=10)

# Frame para la lista de eventos
frame_eventos = tk.Frame(ventana)
frame_eventos.pack(pady=10)

# Treeview para mostrar los eventos
eventos_tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_tree.heading("Fecha", text="Fecha")
eventos_tree.heading("Hora", text="Hora")
eventos_tree.heading("Descripción", text="Descripción")
eventos_tree.pack()

# Botón para eliminar evento
boton_eliminar = tk.Button(ventana, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(pady=10)

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
