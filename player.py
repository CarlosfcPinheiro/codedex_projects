# Import random library
import random

class Player:
    def __init__(self, name: str):
        self.name = name.title()
        self.hp = 100
    
    def atk(self, Monster:object):
        dmg = random.randrange(1, 6)
        Monster.hp -= dmg
        
        if (Monster.hp <= 0):
            print("You defeat the monster, congrats!")     
        else:
            print(f"{self.name} attacks {Monster.name} and takes {dmg} of damage...")
            print(f"The {Monster.name} is {Monster.hp} of hp")
    
    def block(self, monsterDamage):
        defense = random.randint(1, 6)
        dmgRecived = monsterDamage-defense
        
        while(dmgRecived<0):
            defense = random.randrange(1, 6)
            dmgRecived = monsterDamage-defense
        
        if (dmgRecived == 0):
            print("Wow, you defense all damage!")
        else:
            print(f"You taked {dmgRecived} of damage...")
            self.hp -= (dmgRecived)
            print(f"Actual hp: {self.hp}")
            
    def heal(self):
        heal_points = random.randint(1, 6)
        total = heal_points + self.hp
        
        while (total > 100):
            heal_points = random.randint(1, 6)
            total = heal_points + self.hp
        
        self.hp += heal_points
        if (self.hp == 100):
            print("You are full hp now!")
        else:
            print(f"You recover {heal_points} of hp...")
            print(f"Actual hp: {self.hp}")