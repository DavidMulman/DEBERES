import tkinter as tk
from tkinter import messagebox

# ==============================
# Aplicación GUI con Tkinter
# ==============================
class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI - Lista de Datos")
        self.root.geometry("400x300")
        self.root.resizable(False, False)  # Fijar tamaño de ventana

        # ======== LABEL ========
        self.label = tk.Label(root, text="Ingrese un dato:", font=("Arial", 14))
        self.label.pack(pady=5)

        # ======== ENTRY (campo de texto) ========
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # ======== BOTONES ========
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)

        self.btn_agregar = tk.Button(self.btn_frame, text="Agregar", command=self.agregar_dato)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_limpiar = tk.Button(self.btn_frame, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.grid(row=0, column=1, padx=5)

        # ======== LISTBOX ========
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=10)

    # Función para agregar dato a la lista
    def agregar_dato(self):
        dato = self.entry.get().strip()
        if dato:
            self.listbox.insert(tk.END, dato)
            self.entry.delete(0, tk.END)  # limpiar el campo de texto
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un dato antes de agregar.")

    # Función para limpiar campo y lista
    def limpiar(self):
        self.entry.delete(0, tk.END)
        self.listbox.delete(0, tk.END)


# ==============================
# Ejecución principal
# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
