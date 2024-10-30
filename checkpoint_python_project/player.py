# Import random library
import random

class Player:
    def __init__(self, name: str) -> None:
        self.name = name.title()
        self.hp = 100
        self.defense = 0
    # Attack monster method
    def atk(self, Monster:object) -> None:
        dmg = random.randrange(1, 6)
        Monster.hp -= dmg
        
        if (Monster.hp <= 0):
            return None     
        else:
            print(f"\n{self.name} attacks {Monster.name} and takes {dmg} of damage...")
            print(f"The {Monster.name} is {Monster.hp} of hp")
    # Block defense method
    def block(self) -> None:
        defense = random.randint(1, 3)
        self.defense += defense
    # heal player method
    def heal(self) -> None:
        heal_points = random.randint(1, 6)
        total = heal_points + self.hp
        
        if (self.hp == 100):
            print("\nYou are full hp. Stay calm....")
        else:
            if (total > 100):
                self.hp = 100
                print("\nYou are full hp now!")
            else:
                self.hp += heal_points
                print(f"\nYou recover {heal_points} of hp!")