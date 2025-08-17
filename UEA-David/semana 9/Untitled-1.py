# ==============================
# Sistema de Gestión de Inventarios
# ==============================

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


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado correctamente.")
                return
        print("⚠️ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("✅ Producto actualizado correctamente.")
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
