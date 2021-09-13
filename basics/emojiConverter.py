message = input("> ")
words = message.split(' ')
emojiDictionary = {":)": "😀", ":(": "🤔", ":D": "😁", ":P": "😛"}
output = ''
for word in words:
    output += emojiDictionary.get(word, word.capitalize()) + ' '
print(output)