maximum_score = int(input("Maximum Possible Score: "))

actual_score = int(input("Your Score: "))

test_percentage = round(actual_score/maximum_score, 2) * 100

print("You got", test_percentage, "%")
if test_percentage > 89:
    print("You made an A+! Good Job!")
elif test_percentage > 79:
    print("You got a B! Nice!")
elif test_percentage > 69:
    print("C's get degrees!")
elif test_percentage > 59:
    print("You got a D!")
else:
    print("That's an F")