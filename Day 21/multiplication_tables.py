print("Math Game!\n\n")
num_multiple = int(input("Choose a number. You will be tested on this number's multiples: "))
num_correct_answers = 0
for i in range(1, 11):
    user_answer = int(input(str(i) + " X " + str(num_multiple) + " = "))
    if user_answer == (i * num_multiple):
        num_correct_answers += 1
        print("You got it.")
    else:
        print("Sorry that's wrong.")

print("You scored", num_correct_answers, "out of 10")



