# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido (encapsulación)
        self._edad = edad

    def hacer_sonido(self):
        return "Este animal hace un sonido genérico."

    def descripcion(self):
        return f"{self._nombre} tiene {self._edad} años."

# Clase derivada (herencia)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self._raza = raza

    # Polimorfismo: sobrescritura de método
    def hacer_sonido(self):
        return "¡Guau, guau!"

    def descripcion(self):
        return f"{self._nombre} es un perro de raza {self._raza} y tiene {self._edad} años."

# Otra clase derivada (herencia)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color

    # Polimorfismo: sobrescritura de método
    def hacer_sonido(self):
        return "¡Miau!"

    def descripcion(self):
        return f"{self._nombre} es un gato de color {self._color} y tiene {self._edad} años."

# Función que demuestra polimorfismo
def mostrar_sonido(animal):
    print(animal.hacer_sonido())

# Programa principal
if __name__ == "__main__":
    perro1 = Perro("Max", 5, "Labrador")
    gato1 = Gato("Luna", 3, "Blanco")

    # Mostrar descripciones
    print(perro1.descripcion())
    print(gato1.descripcion())

    # Mostrar sonidos (polimorfismo)
    mostrar_sonido(perro1)
    mostrar_sonido(gato1)
