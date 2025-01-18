import random
import os
import time

def roll_dice(sides):
    return random.randint(1, sides)

def roll_health():
    return int(((roll_dice(6) * roll_dice(12)) / 2) + 10)

def roll_strength():
    return int(((roll_dice(6) * roll_dice(12)) / 2) + 10)

def print_dots():
    print("Rolling stats")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
        
    print()
    print("Done!")
    print()

def create_character():
    character_races = ["human", "orc", "elf", "dwarf"]
    character_name = input("Name your Hero: ")
    print()
    race = input("Choose your race (Human, Orc, Elf, Dwarf):").lower()
    print()
    print_dots()
    time.sleep(1)
    os.system("cls")
    print(character_name)
    print("Race: " + race.capitalize())
    print("Health: ", roll_health())
    print("Strength: ", roll_strength())


print("Character Builder")
print()
keep_building = "y"
while keep_building == "y":

    create_character()
    print()

    keep_building = input("Build another character? (y/n) ").lower()
    print()

    if keep_building == "y":
        continue
    elif keep_building == "n":
        break
    else:
        print("Invalid answer. Exiting.")
        break