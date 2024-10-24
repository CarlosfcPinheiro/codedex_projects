# Import library
import random

class Monster:
    species = ["Dragon", "Gnome", "Hunter", "Thief", "Ghost"]

    def __init__(self, name:str):
        self.name = name.title()
        self.specie = Monster.setSpecie()
        self.hp = 20

    def atk(self, player:object) -> None:
        damage = random.randint(1, 30)
        player.hp -= (damage-player.defense)
        print(f"\nYou recived {damage} of damage.")

    @classmethod
    def setSpecie(cls) -> str:
        return random.choice(cls.species)