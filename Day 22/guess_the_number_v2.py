import random

num = random.randint(1, 1000000)

print("Number Guessing Game")
print("A random number between 0 and 1,000,000 has been generated. Try to guess it.")

attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 1,000,000: "))
    attempts += 1
    if guess < num:
        print("Too low.")
    elif guess > num:
        print("Too high.")
    elif guess == num:
        print("You got it!")
        print("It took you", attempts, "guesse(s)!")
        break
    else:
        print("That is not a number I recognize.")

print("Thanks for playing!")
