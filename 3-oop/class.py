
#  class began with capital leter

class Car():
    def __init__(self, model, colour, initial_speed = 0):
        self.model = model
        self.colour = colour
        if initial_speed < 0:
            self.__speed = 0
        else:
            self.__speed = initial_speed
    
    def speed_up(self):
        self.__speed += 5
        
    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5
        
    def show_speed(self):
        print('Current speed:', self.__speed)
        
my_car = Car("seat","rojo")

my_car.colour = "blue"

# __dict__ son todas las propiedades de la calse
print(my_car.__dict__)
# {'model': 'seat', 'colour': 'blue', '_Car__speed': 0}

del my_car.model

print(my_car.__dict__)
# {'colour': 'blue', '_Car__speed': 0}

# __name hacemos que sea privada
class Dog():
    __counter = 0
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.__counter += 1
        
my_dog = Dog("pepe","0")
        
print(my_dog.__dict__)
#{'_Dog__name': 'pepe', 'age': '0'}  
#   Se ve la privada _Nombreclase__nombrepropiedad

#  counter es una variable de la clase no una variable de la instancia
#  name es una variable de la instancia
class Dog():
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1
