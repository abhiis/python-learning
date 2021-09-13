# very easy if you use # * length
line_length = [5, 2, 5, 2, 2]
for length in line_length:
    print("#" * length)

# another way without using # * length

for length in line_length:
    output = ''
    for numbers_of_X in range(length):
        output += 'X'
    print(output)