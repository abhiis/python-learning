def convert_emoji(message):
    words = message.split(' ')
    emojiDictionary = {":)": "😀", ":(": "🤔", ":D": "😁", ":P": "😛"}
    output = ''
    for word in words:
        output += emojiDictionary.get(word, word.capitalize()) + ' '
    return output


message = input("> ")
converted_message = convert_emoji(message)
print(converted_message)