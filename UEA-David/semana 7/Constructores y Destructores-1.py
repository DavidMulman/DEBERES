class Archivo:
    """
    Clase que simula la apertura y cierre de un archivo.
    Demuestra el uso de constructor y destructor en Python.
    """

    def __init__(self, nombre):
        """
        Constructor: se ejecuta cuando se crea una instancia de la clase.
        Inicializa el nombre del archivo y simula abrirlo.
        """
        self.nombre = nombre
        self.abierto = True
        print(f"Constructor: Se ha abierto el archivo '{self.nombre}'.")

    def escribir(self, contenido):
        """
        Método para escribir contenido en el archivo (simulado).
        """
        if self.abierto:
            print(f"Escribiendo en '{self.nombre}': {contenido}")
        else:
            print("No se puede escribir, el archivo está cerrado.")

    def cerrar(self):
        """
        Método para cerrar el archivo manualmente.
        """
        if self.abierto:
            self.abierto = False
            print(f"Archivo '{self.nombre}' cerrado manualmente.")
        else:
            print("El archivo ya estaba cerrado.")

    def __del__(self):
        """
        Destructor: se ejecuta cuando el objeto es eliminado o recolectado por el garbage collector.
        Se usa para realizar tareas de limpieza, como cerrar recursos abiertos.
        """
        if self.abierto:
            print(f"Destructor: Cerrando automáticamente el archivo '{self.nombre}'.")
            self.abierto = False
        else:
            print(f"Destructor: El archivo '{self.nombre}' ya estaba cerrado.")

# Uso del programa
def main():
    print("Inicio del programa")

    archivo1 = Archivo("datos.txt")
    archivo1.escribir("Línea 1")
    
    # Cerrar archivo manualmente
    archivo1.cerrar()

    print("Saliendo del bloque principal")

# Ejecutar solo si se corre este archivo directamente
if __name__ == "__main__":
    main()
    print("Fin del programa")
