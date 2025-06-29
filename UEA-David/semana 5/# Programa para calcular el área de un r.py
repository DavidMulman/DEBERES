# Programa para calcular el área de un rectángulo y un círculo
# Utiliza diferentes tipos de datos (int, float, string, boolean)
# Autor: [Tu Nombre]
# Fecha: [Fecha de entrega]

import math

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dado su base y altura."""
    area = base * altura
    return area

def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * radio ** 2
    return area

# Entradas del usuario (string que luego convertimos a float)
nombre_usuario = input("Ingresa tu nombre: ")
print(f"Hola, {nombre_usuario}! Vamos a calcular áreas.")

# Datos para rectángulo
base_rectangulo = float(input("Ingresa la base del rectángulo (cm): "))
altura_rectangulo = float(input("Ingresa la altura del rectángulo (cm): "))

# Datos para círculo
radio_circulo = float(input("Ingresa el radio del círculo (cm): "))

# Cálculos
area_rect = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
area_circ = calcular_area_circulo(radio_circulo)

# Resultados
print("\n--- Resultados ---")
print(f"Área del rectángulo: {area_rect:.2f} cm²")
print(f"Área del círculo: {area_circ:.2f} cm²")

# Uso de tipo booleano para verificar si el área del rectángulo es mayor
es_mayor_area_rectangulo = area_rect > area_circ
print(f"¿El área del rectángulo es mayor que la del círculo?: {es_mayor_area_rectangulo}")
