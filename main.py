from acuatics import Acuatics
from terrestres import Terrestrial


Animals = __import__('animals').Animals

A = Terrestrial("Toby", "Dog", 3)
B = Terrestrial("Michi", "Cat", 6)

C = Acuatics("Patricio", "Starfish", 30)
D = Acuatics("Mr.Crab", "Crab", 58)

C.show()
