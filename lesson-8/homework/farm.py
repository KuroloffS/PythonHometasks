class Animal:
    def __init__(self, name, age, race):
        self.name = name 
        self.age = age
        self.race = race    
        type_of_obj = type(self)
        name_of_obj = type_of_obj.__name__    
    def eat(self):
        type_of_obj = type(self)
        name_of_obj = type_of_obj.__name__
        print(f"{name_of_obj} {self.name} is eating")

    def walk(self):
        type_of_obj = type(self)
        name_of_obj = type_of_obj.__name__
        print(f"{name_of_obj} {self.name} is walking")

    def sleep(self):
        type_of_obj = type(self)
        name_of_obj = type_of_obj.__name__
        print(f"{name_of_obj} {self.name} is sleeping")    

    def __str__(self):
        return f"Animal(name={self.name}, age={self.age}, race = {self.race})"  

class Cow(Animal):

    def __init__(self, name, age, race, milk):
        super().__init__(name, age, race)
        self.milk = milk

    def eat(self):
          super().eat()

    def walk(self):
        super().walk()

    def sleep(self):
        super().sleep() 

    def give_milk(self):
        print('Cow is giving a milk')

    def __str__(self):
        return f"Cow(name={self.name}, age={self.age}, race={self.race}, gives a {self.milk}L milk)"  

class Hen(Animal):

    def __init__(self, name, age, race, egg):
        super().__init__(name, age, race)
        self.egg = egg

    def eat(self):
          super().eat()

    def walk(self):
        super().walk()

    def sleep(self):
        super().sleep()

    def give_egg(self):
        print('Heg is giving a egg')

    def __str__(self):
        return f"Hane(name={self.name}, age={self.age}, race={self.race}, gives a {self.egg} egss)" 

class Sheep(Animal):

    def __init__(self, name, age, race, wool):
        super().__init__(name, age, race)
        self.wool = wool

    def eat(self):
          super().eat()

    def walk(self):
        super().walk()

    def sleep(self):
        super().sleep()

    def give_wool(self):
        print('Sheep is giving a wool')

    def __str__(self):
        return f"Sheep(name={self.name}, age={self.age}, race={self.race}, gives a {self.wool}kg wool)" 

cow1 = Cow("Masha", 4, "Golland", 20)
chicken1 = Hen("Alex", 1, "Arman", 2)
sheep1 = Sheep("obama", 3, "shew", 5)
print(sheep1)
print(cow1)
print(chicken1)
cow1.eat()
sheep1.sleep()
chicken1.walk()
cow1.give_milk()
sheep1.give_wool()
chicken1.give_egg()