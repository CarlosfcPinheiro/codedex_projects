# Import library
from time import sleep

# Import classes
from player import Player
from monster import Monster
from npc import Npc

#Setting entities instances
player = Player("Albert")
npc = Npc("Jorge")
monster = Monster("Koby")

# Main game function
def main():
    print("="*20+"RPG TERMINAL"+"="*20)
    # Start of the game
    print(f"You are a brave warrior named of {player.name}!\n")
    sleep(1)
    print(f"Because of your great strength, you are invited to save the Vastin village from {monster.name} the {monster.specie}...\n")
    sleep(2)
    print("After a long journey, you arrived on Vastin village...\n")
    sleep(1)
    print("You came across a city dweller.\n")
    sleep(1)

    # Npc dialog
    print("You greet him and give him a smile... :)\n")
    sleep(2)
    print(f"{npc.name}: {npc.talk()}\n")

main()