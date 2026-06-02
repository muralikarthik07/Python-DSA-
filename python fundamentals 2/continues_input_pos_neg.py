while True:
    user_input = input("enter the number or enter quit: ")

    if user_input == "quit":
        print("program terminated")
        break

    try:
        num = float(user_input)

        if num > 0:
            print("Given number is positive")
        elif num < 0:
            print("given number is negative")
        else:
            print("Zero")

    except ValueError:
        print("Please enter a valid number")

