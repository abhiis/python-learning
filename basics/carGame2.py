command = ""
is_started = False
help = '''
start: To start the car
stop: To stop the car
quit: To exit game
'''
print("Welcome to Car Game")
print("Type help to read instructions\n")
while True:  #command != "quit":   if we write this condition, last else block always gets executed
    command = input("> ").lower()
    if command == "help":
        print(help)
    elif command == "start":
        if is_started:
            print("Already Started!")
        else:
            print("Car Started")
            is_started = True
    elif command == "stop":
        if not is_started:
            print("Already Stopped!")
        else:
            print("Car Stopped")
            is_started = False

    elif command == "quit":
        print("Bye")
        break  #this is loop control
else:
    print("Sorry, I don't understand...Try Again")
