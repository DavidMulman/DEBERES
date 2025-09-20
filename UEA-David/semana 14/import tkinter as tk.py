import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Librería extra para el DatePicker

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # ================== FRAME PRINCIPAL (LISTA DE EVENTOS) ==================
        frame_lista = ttk.Frame(self.root)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # TreeView para mostrar los eventos
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # ================== FRAME DE ENTRADA ==================
        frame_entrada = ttk.Frame(self.root)
        frame_entrada.pack(fill=tk.X, padx=10, pady=5)

        # Etiquetas y campos de entrada
        ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background="darkblue",
                                     foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = ttk.Entry(frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(frame_entrada, width=30)
        self.descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

        # ================== FRAME DE BOTONES ==================
        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(fill=tk.X, padx=10, pady=10)

        btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side=tk.LEFT, padx=5)

        btn_eliminar = ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        btn_salir = ttk.Button(frame_botones, text="Salir", command=self.root.quit)
        btn_salir.pack(side=tk.RIGHT, padx=5)

    # ================== FUNCIONES ==================
    def agregar_evento(self):
        """Agrega un nuevo evento al TreeView"""
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Debe llenar todos los campos antes de agregar un evento.")
            return

        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiar entradas
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado del TreeView con confirmación"""
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selección vacía", "Debe seleccionar un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmacion:
            for item in seleccionado:
                self.tree.delete(item)


# ================== EJECUCIÓN PRINCIPAL ==================
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
