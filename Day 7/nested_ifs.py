print("Choose Your Own Adventure!")

print("You find yourself lost in the woods. You stumble upon a path. Do you go left or right? (left/right)")

pathChoice = input("> ")

if pathChoice == "left":
    print("You turn to the left and start walking. You eventually notice a shack just off to the side of the path. Do you continue walking or go inside the shack? (walk/shack)")
    shackChoice = input("> ")
    if shackChoice == "walk":
        print("You ignore the shack and continue walking at a brisk pace. The path eventually dead-ends and when you turn around there's a hungry bear. Whoops.")
    elif shackChoice == "shack":
        print("You walk inside the shack and find a nice old man who tells you how to get back to town.")
    else:
        print("Invalid choice. You wander off the path and get lost again.")

elif pathChoice == "right":
    print("You turn right and start walking. Almost immediately you hear something in the bushes behind you. What do you do? (investigate/run)")
    runChoice = input("> ")
    if runChoice == "investigate":
        print("Why would you do that? You die.")
    elif runChoice == "run":
        print("It's faster than you. You die.")
    else:
        print("Invalid choice. You stand there unsure what to do and then you die.")

else:
    print("Invalid choice. You ponder your decision forever.")