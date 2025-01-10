apr = 0.05
loan = 1000
for year in range(10):
    loan += loan * apr
    print("Year", year + 1, "is", round(loan,2))