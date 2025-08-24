# ==============================
# Sistema de Gestión de Inventarios con Archivos
# ==============================

import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    def to_line(self):
        """Convierte el producto en una línea de texto para guardar en archivo"""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_line(line):
        """Convierte una línea del archivo en un objeto Producto"""
        try:
            id_producto, nombre, cantidad, precio = line.strip().split(",")
            return Producto(int(id_producto), nombre, int(cantidad), float(precio))
        except ValueError:
            return None


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(p.to_line())
        except PermissionError:
            print("⚠️ Error: No tienes permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        """Carga productos desde el archivo, si existe"""
        if not os.path.exists(self.archivo):
            try:
                open(self.archivo, "w").close()  # crea archivo vacío si no existe
                return
            except PermissionError:
                print("⚠️ Error: No tienes permisos para crear el archivo.")
                return

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for line in f:
                    producto = Producto.from_line(line)
                    if producto:
                        self.productos.append(producto)
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado, se creará uno nuevo.")
        except PermissionError:
            print("⚠️ Error: No tienes permisos para leer el archivo.")

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto añadido correctamente y guardado en archivo.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("✅ Producto eliminado correctamente del inventario y archivo.")
                return
        print("⚠️ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("✅ Producto actualizado correctamente en archivo.")
                return
        print("⚠️ Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("🔎 Resultados de búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("⚠️ No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("📋 Lista de productos en inventario:")
            for p in self.productos:
                print(p)


# ==============================
# Interfaz de Usuario (Consola)
# ==============================

def menu():
    inventario = Inventario()

    while True:
        print("\n===== MENÚ DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo)
            except ValueError:
                print("⚠️ Entrada inválida. Intente de nuevo.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                nueva_cantidad = input("Ingrese nueva cantidad (deje vacío si no desea cambiar): ")
                nuevo_precio = input("Ingrese nuevo precio (deje vacío si no desea cambiar): ")

                cantidad = int(nueva_cantidad) if nueva_cantidad else None
                precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("⚠️ Entrada inválida.")

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema de inventario...")
            break

        else:
            print("⚠️ Opción no válida. Intente de nuevo.")


# ==============================
# Programa Principal
# ==============================
if __name__ == "__main__":
    menu()
