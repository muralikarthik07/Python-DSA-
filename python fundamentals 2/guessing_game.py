fixed = 59
while True:
    num = int(input("enter the number:"))

    if num == fixed:
        print("Guessed the correct number")
        break
    elif num < fixed:
        print("entered number is too small")
    elif num > fixed:
        print("entered number is too big")


    