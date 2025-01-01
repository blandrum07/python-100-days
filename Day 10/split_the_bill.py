bill = float(input("How much is the bill? "))
numPeople = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage would you like to tip? (Whole numbers only) "))

billTotal = bill + (tip/100 * bill)

paymentAmount = round(billTotal/numPeople, 2) 

print("Each person owes", paymentAmount)
