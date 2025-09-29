import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Funciones principales
# ------------------------------
def añadir_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea antes de añadirla.")

def marcar_completada():
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        texto = lista_tareas.get(index)
        # Si ya está marcada, la desmarca
        if texto.startswith("✅ "):
            lista_tareas.delete(index)
            lista_tareas.insert(index, texto[2:])
        else:
            lista_tareas.delete(index)
            lista_tareas.insert(index, "✅ " + texto)
    else:
        messagebox.showinfo("Selección requerida", "Selecciona una tarea para marcarla.")

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        lista_tareas.delete(index)
    else:
        messagebox.showinfo("Selección requerida", "Selecciona una tarea para eliminarla.")

def doble_click(event):
    marcar_completada()

# ------------------------------
# Configuración de la ventana principal
# ------------------------------
ventana = tk.Tk()
ventana.title("📝 Lista de Tareas")
ventana.geometry("400x400")
ventana.resizable(False, False)

# ------------------------------
# Widgets de la interfaz
# ------------------------------
# Campo de entrada
entrada_tarea = tk.Entry(ventana, font=("Arial", 14))
entrada_tarea.pack(pady=10, padx=10, fill=tk.X)
entrada_tarea.bind("<Return>", añadir_tarea)  # Presionar Enter para añadir tarea

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_añadir = tk.Button(frame_botones, text="➕ Añadir Tarea", width=15, command=añadir_tarea)
btn_añadir.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="✅ Marcar Completada", width=18, command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar Tarea", width=15, command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, font=("Arial", 12), height=15)
lista_tareas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
lista_tareas.bind("<Double-Button-1>", doble_click)  # Doble clic para marcar completada

# ------------------------------
# Iniciar la aplicación
# ------------------------------
ventana.mainloop()
