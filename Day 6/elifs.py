import random

num = random.randint(1, 100)
guess = 0
keep_playing = True

print("-----Number Guessing Game-----")
print("A number between 1 and 100 (Inclusive) has been generated. Try to guess it.")

while keep_playing:
    guess = int(input("Guess a number\n"))
    if guess > num:
        print("Too high\n")
    elif guess < num:
        print("Too low\n")
    else:
        print("You Win!\n\n")
        user_input = input("Play Again? (y/n)")
        if user_input == 'n':
            keep_playing = False
print("Thanks for playing!")
