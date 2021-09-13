print("\n\nProgram to convert weight in different units\n")
wt = float(input("\nEnter Weight: "))
unit = input("(K)gs or (L)bs? Press K or k for Kgs, L or l for Lbs: ")
if unit.upper() == "K":
    wtLbs = wt / 0.45
    print(f"Weight in Lbs = {wtLbs}")
elif unit.upper() == "L":
    wtKgs = wt * 0.45
    print(f"Weight in Kgs = {wtKgs}")
else:
    print("\nError. Please enter correct unit")
