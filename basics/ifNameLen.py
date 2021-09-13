name = input("Enter Name: ")
if (len(name) <= 3):
    print("Name must have more than 3 Characters")
elif len(name) > 50:
    print("Name must be less than 50 characters")
else:
    print("Name looks good!")