"""Module to create a class animal"""
from animals import Animals


class Terrestrial(Animals):

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def move(self):
        print(f"{self.__name} is running")
    
    def show(self):
        print(f"Here is {self.__name}")

    def sound(self):
        if self.species == "Cat":
            print("MiauMiau")
        elif self.species == "Dog":
            print("WofWof")
