numbers = []
while True:
    command = input("Enter list items. Press '/' when finished: ")
    if command == '/':
        break
    numbers.append(int(command))
print(numbers)
numbers.sort()
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)