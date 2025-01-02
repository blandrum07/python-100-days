print("Seconds in year calculator")

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minutes = 60

leap_year = input("Is it a leap year? (y/n)")
if leap_year == "y":
    days_in_year += 1


result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minutes

print("There are", result, "seconds in a year.")