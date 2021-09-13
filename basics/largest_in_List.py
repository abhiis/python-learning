max = 0
numbers = list(int(input("Enter List>")))
# while True:
#     command = input("Enter list items. Press '/' when finished: ")
#     if command == '/':
#         break
#     numbers.append(int(command))
print(numbers)
for number in numbers:
    if number > max:
        max = number
print(f"Max in list is {max}")