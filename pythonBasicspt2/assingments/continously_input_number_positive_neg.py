while True:
    user_input = input("enter a number: ")
    if user_input == "quit":
        break

    num = int(user_input)
    if num % 2 == 0:
        print("even")
    elif num % 2 != 0:
        print("odd")
    