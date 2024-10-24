# Import library
import random

class Monster:
    species = ["Dragon", "Gnome", "Hunter", "Thief", "Ghost"]

    def __init__(self, name:str):
        self.name = name.title()
        self.specie = Monster.setSpecie()

    @classmethod
    def setSpecie(cls) -> str:
        return random.choice(cls.species)