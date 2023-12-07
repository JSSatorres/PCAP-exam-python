
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
        
# my_dog = Dog("pepe","0")        
print(Dog.__dict__)
#   Se puede hacer con la clase para ver lo que hay dentro
#   {'__module__': '__main__', 'counter': 0, '__init__': <function Dog.__init__ at 0x0000014CAA422AC0>, '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}


class House():
    counter = 0
    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1
        
        House.quality = 'low'
        self.quality = 'medium'
        quality = 'high'
        
        print(House.quality, self.quality, quality)
    
    def present(self):
        print('The house at', self.address, 'has an area of', self.area, 'and costs', self.price)

soho_house = House('12 Lexington St, Soho', 130, 540000)
soho_house.present()
print(House.counter)

# aqui qulity solo se puede acceder en el constructor es una variable local

class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        
   
class Vehicle:
    def __init__(self, speed):
        self.speed = speed
             

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count
        
        
first_str = 'hello'
second_str = 'hell'
second_str += 'o'
print(first_str is second_str)  # False
print(first_str == second_str) # True

# no es igual con el operador is por que second tendra dos referencias de memoria
# una "hell" otra "o"
# pero el == compara que hayalo mismo 

