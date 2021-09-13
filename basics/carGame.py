command = ""
is_started = False
is_stopped = False
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
        if not is_started:
            print("Car Started")
            is_started = True
        else:
            print("Already Started!")
    elif command == "stop":
        if not is_stopped and is_started:
            print("Car Stopped")
            is_stopped = True
        else:
            print("Already Stopped!")
    elif command == "quit":
        print("Bye")
        break  #this is loop control
    else:
        print("Sorry, I don't understand...Try Again")
