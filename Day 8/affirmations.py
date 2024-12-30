print("Welcome to your daily affirmation generator!")

name = input("What is your name? ")

day = input("What is the day of the week? ").lower()

days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
while day not in days_of_week:
    day = input("Make sure to enter a valid day. ")

if day == days_of_week[0]:
    print("You got this " + name + ". Today will be a great " + days_of_week[0])
elif day == days_of_week[1]:
    print("You're hard work is going to pay off, " + name + "!")
elif day == days_of_week[2]:
    print("It's going to be a great " + day + ", " + name + ". Keep up the good work")
elif day == days_of_week[3]:
    print("You're over the hump, " + name + "!")
elif day == days_of_week[4]:
    print("TGIF. You're gonna do great, " + name + "!")
else:
    print("It's the weekend! Enjoy yourself. You deserve it.")
