import random

num = random.randint(1, 100)
guess = 0
print("-----Number Guessing Game-----")
print("A number between 1 and 100 (Inclusive) has been generated. Try to guess it.")

while guess != num:
    guess = int(input("Guess a number\n"))
    if guess > num:
        print("Too high\n")
    if guess < num:
        print("Too low\n")

print("You Win!")
    