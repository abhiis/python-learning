#String
message = "this is my first string program"
#String Methods
print(message.capitalize())
print(message.upper())
print(message.lower())
print(message.find('m'))
print(message.replace('my', 'your'))
print("TITLE: " + message.title())
#These methods do not change original string. Strings are immutable. They return a new string as we can message is not changed
print(message)

#IN operator
#returns boolean for checking a substr in str
print('first' in message)