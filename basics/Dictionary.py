#just like JS objects, having key value pairs
#patient = {
# "name": "John",
# "age": 28,
# "new": True
# }
numberInWords = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ''
number = input("Enter Number: ")
for num in number:
    output += numberInWords[num] + ' '
print(output)