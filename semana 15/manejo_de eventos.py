import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor ingrese una tarea.")

# Función para marcar tarea como completada
def mark_completed():
    try:
        selected_task = listbox.curselection()  # Obtener tarea seleccionada
        if selected_task:
            task_index = selected_task[0]
            task = listbox.get(task_index)
            listbox.delete(task_index)  # Eliminar la tarea de la lista
            listbox.insert(task_index, task + " (Completada)")  # Añadir "(Completada)" a la tarea
        else:
            messagebox.showwarning("Seleccionar tarea", "Por favor seleccione una tarea para marcar como completada.")
    except Exception as e:
        print(f"Error al marcar como completada: {e}")

# Función para eliminar tarea
def delete_task():
    try:
        selected_task = listbox.curselection()  # Obtener tarea seleccionada
        if selected_task:
            listbox.delete(selected_task)  # Eliminar la tarea de la lista
        else:
            messagebox.showwarning("Seleccionar tarea", "Por favor seleccione una tarea para eliminar.")
    except Exception as e:
        print(f"Error al eliminar tarea: {e}")

# Crear ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Establecer el tamaño de la ventana con el método geometry
root.geometry("400x400")  # Definir el tamaño de la ventana en 400x400 píxeles

# Campo de entrada para escribir nuevas tareas
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir tarea
add_button = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Crear lista de tareas
listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tarea como completada
completed_button = tk.Button(root, text="Marcar como Completada", width=20, command=mark_completed)
completed_button.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tarea
delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Permitir añadir tarea con la tecla Enter
entry.bind("<Return>", lambda event: add_task())

# Iniciar la aplicación
root.mainloop()
