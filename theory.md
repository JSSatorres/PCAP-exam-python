# Resumen de Conceptos de Programación Orientada a Objetos en Python

## Encapsulación

La encapsulación implica ocultar detalles internos de una clase y restringir el acceso a ciertos componentes. En Python, esto se logra mediante el uso de atributos y métodos privados.

```python
class MiClase:
    def __init__(self):
        self.__atributo_privado = 10

    def obtener_atributo_privado(self):
        return self.__atributo_privado

objeto = MiClase()
print(objeto.obtener_atributo_privado())  # Acceso controlado al atributo privado
```

## Polimorfismo

El polimorfismo permite tratar objetos de diferentes clases de manera uniforme. En Python, se puede lograr mediante funciones con el mismo nombre pero comportamientos diferentes según la clase.

```python
class Perro:
    def sonido(self):
        return "Woof!"

class Gato:
    def sonido(self):
        return "Meow!"

def hacer_sonar(animal):
    print(animal.sonido())

perro = Perro()
gato = Gato()

hacer_sonar(perro)  # Salida: Woof!
hacer_sonar(gato)   # Salida: Meow!
```

## Abstracción

La abstracción simplifica un problema al ocultar detalles innecesarios. En Python, se logra con clases abstractas y métodos abstractos.

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

cuadrado = Cuadrado(5)
print(cuadrado.area())  # Salida: 25
```

## Herencia

La herencia permite que una clase herede atributos y métodos de otra clase. En Python, se usa la sintaxis `class NuevaClase(ClaseBase)`.


```python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def describir(self):
        return f"{super().describir()}, color: {self.color}"

coche = Coche("Toyota", "Camry", "Rojo")
print(coche.describir())  # Salida: Toyota Camry, color: Rojo
```


