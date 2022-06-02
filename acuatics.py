"""Module to create a class animal"""
from animals import Animals


class Acuatics(Animals):

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def move(self):
        print(f"{self.__name} is swimming")
    
    def show(self):
        if self.species == "Starfish":
            print(f"Here is {self.name}")
            print(f"\t\t──────────────────────████──────────────\n\
                ─────────────────────███████────────────\n\
                ────────────────────██░░░░▓██───────────\n\
                ───────────────────██░░░░░░░██──────────\n\
                ───────────────────██░░░░░░░██──────────\n\
                ────────████───────█░░░▒▒░░░██──────────\n\
                ───────███████────██░░▒▒▒▒░░██──────────\n\
                ──────██░░░░███───██░░▒▒▒▒░░█▀──────────\n\
                ──────██░░░░░░██──██░░▒▒▒▒░██───────────\n\
                ──────██░░▒▒░░░██▄██░▒▒▒▒░░██───────────\n\
                ──────██░░▒▒▒░░░████░░▒▒▒░░██───────────\n\
                ───────██░░▒▒▒░░░███░░░░░░░█────────────\n\
                ────────██░░▒▒▒░░███░░░░░░██───────███──\n\
                ─────────██░░▒▒▒░░██░███████─────██████▄\n\
                ──────────██░░▒░░░░░░█────██────███░░░██\n\
                ───────────██░░░░░░░█──█──██▄▄▄██▓░░░░██\n\
                ──────────▄██░████░░█─███─██████▒░░░░░░█\n\
                ─────▄██████▒██──██░█─███─█░███░░░▒▒▒░░█\n\
                ────███████░░█─█──█░█──█──█░░░░░▒▒▒▒░░░█\n\
                ───██▒░░░░░░█─███──█░█───█░░░░░▒▒▒▒░░░██\n\
                ──██░░░░░░░░█─███──█░░███░░░░░░░░░░░░███\n\
                ─██░░░▒▒▒▒░░█──█───█░░░░░░░░░░░░░░░████▀\n\
                ─█▓░░▒▒▒▒▒░░░█────█░░░░░░░░░░░███████▀──\n\
                ██░░░▒▒▒▒▒░░░░█──█░░░░░░░░░░░██▀────────\n\
                ██░░░▒▒▒▒▒░░░░░██░░░░░░░░░░░░█▄─────────\n\
                ██░░░▒▒▒▒▒░░░█░░░░░░░░░░░░░█░██─────────\n\
                ██░░░░░░░░░░░██░░░░░░░░░░░██░██▄────────\n\
                ▀██░░░░░░░░░░░██░░░░░░░░░██░░░██▄───────\n\
                ─▀█████████▀█░░██░░░░░░░██░░░░░███──────\n\
                ──▀█████▀───▀█░░██░░░░░██░░░░▒░░░██─────\n\
                ─────────────█░░░███████░░░░▒▒▒░░░██────\n\
                ─────────────██░░░█████░░█░░░▒▒▒░░░██───\n\
                ─────────────██░░░████░░███░░░▒▒▒░░██───\n\
                ─────────────█░░░░░██░░█▀▀██░░░▒▒░░██───\n\
                ────────────██░░▒░░░░░█▀───██░░░░░░██───\n\
                ────────────█▒░▒▒▒▒░░██─────▀██░░░███───\n\
                ───────────██░░▒▒▒▒░██▀──────▀██████▀───\n\
                ───────────██░░▒▒▒░░██─────────▀██▀─────\n\
                ───────────██░░░▒░░██───────────────────\n\
                ───────────██░░░░░░██───────────────────\n\
                ───────────███░░░░██────────────────────\n\
                ────────────███░░██─────────────────────\n\
                ─────────────▀███▀──────────────────────\n")
        elif self.species == "Crab":
            print(" /\
                ( /   @ @    ()
                \  __| |__  /
                -/   "   \-
                /-|       |-\
                / /-\     /-\ \
                / /-`---'-\ \
                /         \")
    def sound(self):
        if self.species == "Crab":
            print("TacTacTac")
        elif self.species == "Starfish":
            print("Shuuuu")