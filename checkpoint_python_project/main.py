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

# Variables
base_time = 3

def fight(monsterInst:object) -> int:
    while(monster.hp > 0 or player.hp > 0):
        # Set turn status
        player.defense = 0
        # Logic
        option = int(input(f"""\n
        {monsterInst.name}'s HP: {monsterInst.hp}
        {player.name}'s HP: {player.hp}
        ACTIONS ====
        [1] Attack
        [2] Defense
        [3] Heal
        
        SELECT OPTION: """))

        match(option):
            case 1:
                player.atk(monster)
                if (monster.hp <= 0):
                    print(f"\nYou defeat the monster {monster.name}: The {monster.specie}!!!")
                    win = 1
                    break
            case 2:
                player.block()
            case 3:
                player.heal()
            case _:
                print("This option isn't avaliable...")
                break

        # Monster attacks the player
        monster.atk(player)
        # Conditionals win or loose
        if (player.hp <= 0):
            print("\nYou died. Try the game again :(")
            win = 0
            break
    return win
        
def final(win:int) -> None:
    if (win):
        print("\nNow, all the residents of the village are grateful for you! Get ready for the party! :D")
    else:
        print(f"\nThe village was destroyed by {monster.name}: The {monster.specie}...")

# Main game function
def main() -> None:
    print("="*20+"RPG TERMINAL"+"="*20)
    # Start of the game
    print(f"You are a brave warrior named of {player.name}!\n")
    sleep(base_time)
    print(f"Because of your great strength, you are invited to save the Vastin village from {monster.name} the {monster.specie}...\n")
    sleep(base_time)
    print("After a long journey, you arrived on Vastin village...\n")
    sleep(base_time)
    print("You came across a city dweller, named Jorge.\n")
    sleep(base_time)

    # Npc dialog
    print("You greet him and give him a smile... :)\n")
    sleep(base_time)
    print(f"{npc.name}: {npc.talk()}\n")
    sleep(base_time)
    print("You greet him again and goes towards the city center.\n")
    sleep(base_time)
    print("In the distance, you start to hear some screams coming from there...\n")
    sleep(base_time)
    print(f"Arriving on the city center, you find the monster {monster.name}: The {monster.specie}!\n")

    print(20*"="+"COMBAT"+"="*20)
    # Fight logic
    win = fight(monster)

    # Final game
    final(win)

main()