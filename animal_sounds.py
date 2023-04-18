# animal_sounds.py

import random

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Moo")

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Baa")

class Pig(Animal):
    def __init__(self, name):
        super().__init__(name, "Oink")

animals = [Dog("Buddy"), Cat("Fluffy"), Cow("Bessie"), Sheep("Shaun"), Pig("Porky")]

for i in range(10):
    animal = random.choice(animals)
    animal.make_sound()
