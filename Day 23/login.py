def login():
    while True:
        username = input("What is your username? ")
        password = input("What is your password? ")
        if username != my_username:
            print("Username not recognized.")
        elif password != my_password:
            print("Password is incorrec!")
        else:
            print("You have successfully logged in.")
            break

print("Landrum Login System")
my_username = input("Set a username: ")
my_password = input("Set a password: ")

login()