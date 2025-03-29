import tkinter as tk
from tkinter import messagebox


class TareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Lista para almacenar las tareas
        self.tareas = []

        # Crear la interfaz gráfica
        self.create_widgets()

        # Atajos de teclado
        self.root.bind("<Return>", self.add_task)  # Añadir tarea con Enter
        self.root.bind("<C>", self.mark_completed)  # Marcar tarea como completada con C
        self.root.bind("<Delete>", self.delete_task)  # Eliminar tarea con Delete
        self.root.bind("<D>", self.delete_task)  # Eliminar tarea con D
        self.root.bind("<Escape>", self.quit_app)  # Cerrar aplicación con Escape

    def create_widgets(self):
        """Crear los widgets (componentes de la interfaz gráfica)."""
        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.root, text="Añadir tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Botones para otras acciones
        self.complete_button = tk.Button(self.root, text="Marcar como completada", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self, event=None):
        """Añadir tarea a la lista."""
        task = self.entry.get().strip()
        if task:
            self.tareas.append({"task": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def mark_completed(self, event=None):
        """Marcar una tarea como completada."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tareas[task_index]["completed"] = True
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self, event=None):
        """Eliminar tarea de la lista."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tareas[task_index]
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

    def update_task_list(self):
        """Actualizar la visualización de las tareas en la lista."""
        self.task_listbox.delete(0, tk.END)
        for tarea in self.tareas:
            display_text = f"[{'✓' if tarea['completed'] else ' '}] {tarea['task']}"
            color = "light green" if tarea['completed'] else "white"
            self.task_listbox.insert(tk.END, display_text)
            self.task_listbox.itemconfig(tk.END, {'bg': color})

    def quit_app(self, event=None):
        """Cerrar la aplicación."""
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = TareasApp(root)
    root.mainloop()
