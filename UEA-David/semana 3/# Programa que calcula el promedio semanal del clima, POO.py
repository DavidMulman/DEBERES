# Programa que calcula el promedio semanal de temperaturas usando Programación Orientada a Objetos (POO)

class ClimaSemanal:
    """Clase que representa el clima de una semana."""

    def __init__(self):
        self._temperaturas = []  # Encapsulamiento: atributo privado

    def ingresar_temperaturas(self):
        """Solicita al usuario las temperaturas diarias durante 7 días."""
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        """Calcula el promedio de las temperaturas almacenadas."""
        if not self._temperaturas:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_promedio(self):
        """Muestra el promedio calculado."""
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

# Lógica principal
def main():
    print("PROMEDIO SEMANAL DEL CLIMA - POO")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()

if __name__ == "__main__":
    main()
