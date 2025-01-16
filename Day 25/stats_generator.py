import random

def roll_dice(sides):
    return random.randint(1, sides)

def generate_health():
    health = roll_dice(6) * roll_dice(8)
    return health

make_new_character = True
print("Character Stats Generator")

while make_new_character:
    character_name = input("Name your warrior: ")
    health = generate_health()

    print(character_name + "'s health is", health, "hp")
    print()
    make_new_character = True if ((input("Do you want to make another character? (y/n) ").lower() == "y")) else False