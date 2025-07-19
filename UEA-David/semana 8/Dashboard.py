import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    
    opciones = {
        '1': ("Promedio del clima (Tradicional)", "# Programa que calcula el promedio semanal del clima, tradicional.py"),
        '2': ("Promedio del clima (POO)", "# Programa que calcula el promedio semanal del clima, POO.py"),
        '3': ("Cálculo de áreas (Versión 1)", "# Programa para calcular el área.py"),
        '4': ("Cálculo de áreas (Versión 2)", "# Programa para calcular el área de un r.py"),
        '5': ("Ejemplo de Herencia y Polimorfismo", "# Clase base.py"),
        '6': ("Uso de Constructor y Destructor", "Untitled-1.py"),
        # Puedes seguir agregando más scripts aquí si lo deseas
    }

    while True:
        print("\n========= DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS =========")
        for key, (titulo, _) in opciones.items():
            print(f"{key}. {titulo}")
        print("0. Salir")

        eleccion = input("Selecciona una opción para ver el código: ")

        if eleccion == '0':
            print("Saliendo del dashboard.")
            break
        elif eleccion in opciones:
            _, ruta_archivo = opciones[eleccion]
            ruta_script = os.path.join(ruta_base, ruta_archivo)
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
