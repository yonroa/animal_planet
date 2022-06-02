"""Module to create a class animal"""
from typing import Type


class Animals:
    """Class to create animals"""

    def __init__(self, name="", species="", age=0):
        """Initialize the class animal"""
        self.name = name
        self.species = species
        self.age = age

    @property
    def name(self):
        """Return the name of the animal"""
        return self.__name

    @name.setter
    def name(self, value):
        """Sets the attribute name"""
        if type(value) is not str:
            raise TypeError("Name should be of type string")
        self.__name = value

    @property
    def species(self):
        """Return the species of the animal"""
        return self.__species

    @species.setter
    def species(self, value):
        """Sets the attribute species"""
        if type(value) is not str:
            raise TypeError("Species should be of type string")
        self.__species = value

    @property
    def age(self):
        """Return the age of the animal"""
        return self.__age

    @age.setter
    def age(self, value):
        """Sets the attribute age"""
        if type(value) is not int:
            raise TypeError("Age should be an integer")
        if value < 0:
            raise ValueError("Age should be >= 0")
        self.__age = value

    def __str__(self):
        """Print the name, specie, and age of the animal"""
        return (f"Name: {self.__name}\n" \
                f"Specie: {self.__species}\n" \
                f"Age: {self.__age}\n")
