import random

num = random.randint(0, 1000000)

print("Number Guessing Game")
print("A random number between 0 and 1,000,000 has been generated. Try to guess it.")

attempts = 0

while True:
    guess = int(input("Guess a number: "))
    attempts += 1
    if guess < num:
        print("Too low.")
    elif guess > num:
        print("Too high.")
    else:
        break

print("You got it!")
print("It took you", attempts, "guesses!")