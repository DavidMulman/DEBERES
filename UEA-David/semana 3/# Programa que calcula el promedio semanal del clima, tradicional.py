# Programa que calcula el promedio semanal de temperaturas usando programación tradicional

def ingresar_temperaturas():
    """Solicita al usuario las temperaturas diarias durante 7 días y las retorna en una lista."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de las temperaturas recibidas."""
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Lógica principal
def main():
    print("PROMEDIO SEMANAL DEL CLIMA - TRADICIONAL")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
