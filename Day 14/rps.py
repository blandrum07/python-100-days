from getpass import getpass as input

print("Rock, Paper, Scissors!")

print()

print("Select R, P, or S")

player_1_choice = input("Player 1 > ")
print()

player_2_choice = input("Player 2 > ")
print()

if player_1_choice == player_2_choice:
    print("You both picked " + player_1_choice + "! It's a draw!")

elif player_1_choice == "R":
    if player_2_choice == "S":
        print("Rock breaks Scissors! Player 1 Wins!")
    elif player_2_choice == "P":
        print("Paper covers Rock! Player 2 Wins!")
elif player_1_choice == "P":
    if player_2_choice == "R":
        print("Paper covers Rock! Player 1 Wins!")
    elif player_2_choice == "S":
        print("Scissors cuts Paper! Player 2 Wins!")
elif player_1_choice == "S":
    if player_2_choice == "R":
        print("Rock breaks Scissors! Player 2 Wins!")
    elif player_2_choice == "P":
        print("Scissors cuts Paper! Player 1 Wins!")
else:
    print("Someone made a mistake. Try again!")
