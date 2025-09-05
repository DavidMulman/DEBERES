# =======================================
# Sistema de Gestión de Biblioteca Digital con Menú
# =======================================

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}            # Diccionario {ISBN: Libro}
        self.usuarios = {}          # Diccionario {ID: Usuario}
        self.ids_usuarios = set()   # Conjunto para IDs únicos

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("⚠️ El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"✅ Libro agregado: {libro}")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"❌ Libro eliminado: {eliminado}")
        else:
            print("⚠️ No se encontró el libro con ese ISBN.")

    def registrar_usuario(self, usuario):
        if usuario.user_id in self.ids_usuarios:
            print("⚠️ El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"✅ Usuario registrado: {usuario}")

    def baja_usuario(self, user_id):
        if user_id in self.usuarios:
            eliminado = self.usuarios.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"❌ Usuario dado de baja: {eliminado}")
        else:
            print("⚠️ No se encontró el usuario con ese ID.")

    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("⚠️ Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"📚 Libro prestado: {libro} a {usuario.nombre}")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return

        usuario = self.usuarios[user_id]
        libro_devuelto = None

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_devuelto = libro
                break

        if libro_devuelto:
            usuario.libros_prestados.remove(libro_devuelto)
            self.libros[isbn] = libro_devuelto
            print(f"🔄 Libro devuelto: {libro_devuelto}")
        else:
            print("⚠️ El usuario no tenía este libro en préstamo.")

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"📌 Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f"   - {libro}")
            else:
                print(f"📌 {usuario.nombre} no tiene libros prestados.")
        else:
            print("⚠️ Usuario no registrado.")

    def listar_libros_por_categoria(self):
        if not self.libros:
            print("⚠️ No hay libros en la biblioteca.")
            return

        categorias = {}
        for libro in self.libros.values():
            categorias.setdefault(libro.categoria, []).append(libro)

        print("📂 Lista de libros por categoría:")
        for categoria, libros in categorias.items():
            print(f"\n📌 {categoria}:")
            for libro in libros:
                print(f"   - {libro}")


# =======================================
# PROGRAMA PRINCIPAL CON MENÚ
# =======================================
if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        print("\n===== 📚 MENÚ BIBLIOTECA DIGITAL =====")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro por título")
        print("8. Buscar libro por autor")
        print("9. Buscar libro por categoría")
        print("10. Listar libros prestados de un usuario")
        print("11. Listar todos los libros por categoría")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID único del usuario: ")
            usuario = Usuario(nombre, user_id)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            user_id = input("Ingrese ID del usuario a dar de baja: ")
            biblioteca.baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            titulo = input("Ingrese el título a buscar: ")
            resultados = biblioteca.buscar_por_titulo(titulo)
            if resultados:
                print("✅ Libros encontrados:")
                for libro in resultados:
                    print(f"   - {libro}")
            else:
                print("⚠️ No se encontraron libros con ese título.")

        elif opcion == "8":
            autor = input("Ingrese el autor a buscar: ")
            resultados = biblioteca.buscar_por_autor(autor)
            if resultados:
                print("✅ Libros encontrados:")
                for libro in resultados:
                    print(f"   - {libro}")
            else:
                print("⚠️ No se encontraron libros de ese autor.")

        elif opcion == "9":
            categoria = input("Ingrese la categoría a buscar: ")
            resultados = biblioteca.buscar_por_categoria(categoria)
            if resultados:
                print("✅ Libros encontrados:")
                for libro in resultados:
                    print(f"   - {libro}")
            else:
                print("⚠️ No se encontraron libros en esa categoría.")

        elif opcion == "10":
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(user_id)

        elif opcion == "11":
            biblioteca.listar_libros_por_categoria()

        elif opcion == "0":
            print("👋 Saliendo del sistema de biblioteca digital...")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.")
