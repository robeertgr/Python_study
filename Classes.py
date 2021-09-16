"""
Ao criar uma classe, devemos usar o def __init__ que é um construtor. É uma função especial
que informa ao Python que você está criando uma nova classe
O parâmetro self se refere à instancia recém criada da classe
Os parâmetros radius e color podem ser usados no corpo do construtor para acessar os valores
passados para o construtor da classe quando a classe é construída
Podemos definir o valor dos atributos de dados de raio e cor para os valores passados para o
método no construtor, no caso "self.radius e self.color"
Todos os atributos devem ser inicializados
"""


# Um objeto é a instanciação de uma classe


class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r


class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color


# Criando um objeto da classe

RedCircle = Circle(10, "red")
RedCircle.color = "blue"
RedCircle.radius = 10
RedCircle.add_radius(8)


# ---------------------------------------------------------------


class Car(object):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.owner_number = 0

    def car_info(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Color: ", self.color)
        print("Number of owners: ", self.owner_number)

    def sell(self):
        self.owner_number = self.owner_number + 1


make = "BMW"
model = "M3"
color = "gray"

my_car = Car(make, model, color)
my_car.car_info()

for i in range(5):
    my_car.sell()

my_car.car_info()
