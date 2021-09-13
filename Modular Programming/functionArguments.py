#two types of Arguments
#1. Positional Arguments 2. Keyword Argumeents


def greet_user(fname, lname):
    print(f"Hi {fname} {lname}")
    print("Welcome onboard")


greet_user(
    "Abhishek", "Srivastava"
)  #positional arguments, defined by position in argument list, abhishek is fname, srivastva is lname

greet_user("Srivastava", "Abhishek")

greet_user(
    lname="Srivastava", fname="Abhishek"
)  #Keyword arguments, when dealing with numerical arguments, should be used, else use positional
