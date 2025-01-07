print("Fill in the blank lyrics!")
print("Type in the blank lyrics and see if you are as cool as me.)")

attempts = 0
while True:
    guess = input("Never gonna ____ you up.\n")
    attempts += 1
    if guess == "give":
        break
    else:
        print("Nope. Try again.\n")

print()
print("Well done! It only took you", attempts, "attempt(s).")