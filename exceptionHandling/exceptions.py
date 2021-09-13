#exception handling isn done using try .. except
try:
    age = int(
        input("Enter age: ")
    )  #an error can be generated if user enters other than int values
    income = float(input("Enter income: "))
    risk = income / age  #an error can be generated if age=0
    print(age)
except ZeroDivisionError:
    print("Age can not be 0.")
except ValueError:
    print("Invalid Value")
