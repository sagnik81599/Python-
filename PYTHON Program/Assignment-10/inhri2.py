class Animal:
    def __init__(self, animal_type):
        self.type = animal_type
    
    def eat(self):
        print("The animal is eating.")

class Bird(Animal):
    def __init__(self, animal_type, name):
        super().__init__(animal_type)
        self.name = name
    
    def eat(self):
        print(f"The bird {self.name} is eating.")

class Cat(Animal):
    def __init__(self, animal_type, color):
        super().__init__(animal_type)
        self.color = color
    
    def eat(self):
        print(f"The cat with {self.color} fur is eating.")

# Creating objects of the Bird and Cat classes
bird = Bird("Bird", "Sparrow")
cat = Cat("Cat", "Black")

# Calling the eat method on the objects
bird.eat()
cat.eat()
