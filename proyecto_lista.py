import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Entry para nueva tarea
        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=10)

        # Botón para añadir tarea
        self.button_add = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.button_add.pack(pady=5)

        # Listbox para mostrar tareas
        self.listbox_tasks = tk.Listbox(root, width=50, height=10)
        self.listbox_tasks.pack(pady=10)

        # Botón para eliminar tarea
        self.button_delete = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.button_delete.pack(pady=5)

        # Botón para marcar tarea como completada
        self.button_complete = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.button_complete.pack(pady=5)

        # Etiqueta para mostrar el estado
        self.label_status = tk.Label(root, text="")
        self.label_status.pack(pady=10)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
            self.update_status()
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def delete_task(self):
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(selected_index)
            self.update_status()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

    def complete_task(self):
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            task = self.listbox_tasks.get(selected_index)
            self.listbox_tasks.delete(selected_index)
            self.listbox_tasks.insert(tk.END, f"{task} (Completada)")
            self.update_status()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def update_status(self):
        tasks_count = self.listbox_tasks.size()
        self.label_status.config(text=f"Tareas pendientes: {tasks_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

