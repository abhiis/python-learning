print("**************** Basic Calculator Program ****************\n")
option = input("\nPress 1 to add\nPress 2 to subtract\n")
if int(option) == 1:
    num1 = input("\nFirst Number: ")
    num2 = input("\nSecond Number: ")
    sum_ = float(num1) + float(num2)
    print("\nSum of " + str(num1) + " and " + str(num2) + " is " + str(sum_))
elif int(option) == 2:
    num1 = input("\nFirst Number: ")
    num2 = input("\nSecond Number: ")
    diff = float(num1) - float(num2)
    print("\nDifference of " + str(num1) + " and " + str(num2) + " is " +
          str(diff))

#We can also use float on input funcions as well