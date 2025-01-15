import random

def roll_dice(sides):
    print("You rolled ", random.randint(1, sides))

print("Infinity Dice 🎲")
sides = int(input("How many sides? "))
roll_again = True
while roll_again:
    roll_dice(sides)

    roll_again = True if (input("Roll again? (y/n) ").lower() == "y") else False