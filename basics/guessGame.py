secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the Number: "))
    guess_count += 1
    if guess == secret_number:
        print("Yay!. You Won")
        break
    # elif guess_count == guess_limit:
    #     print("You ran out maximum number of guesses")
#while also has an else block, just like if. while..else gets executed when while loop finishes
else:
    print("You ran out maximum number of guesses")
