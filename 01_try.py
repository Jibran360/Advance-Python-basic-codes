while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break

# try….. except blocks are used in python to handle errors and exceptions. 
# The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

    try:
        print("Trying...")
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:                                  # If any error occurs in try except block executes
        print(f"Your input resulted in an error {e}")

print("Thanks for playing this game")