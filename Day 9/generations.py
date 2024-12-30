birthYear = int(input("What year were you born? "))

if  1901 <= birthYear <= 1927:
    print("You're part of the Greatest Generation!")

elif 1928 <= birthYear <= 1947:
    print("You're part of the Silent Generation!")

elif 1946 <= birthYear <= 1965:
    print("You're a Baby Boomer!")

elif 1965 <= birthYear <= 1980:
    print("You're part of Generation X!")

elif 1981 <= birthYear <= 1996:
    print("You're a Millenial!")

elif 1997 <= birthYear <= 2010:
    print("You're a Zoomer!")

elif 2011 <= birthYear <= 2024:
    print("You're part of Generation Alpha!")

elif 2025 <= birthYear <= 2039:
    print("You're part of Generation Beta!")

else:
    print("I'm not sure what generation you are part of (or how you're alive)")