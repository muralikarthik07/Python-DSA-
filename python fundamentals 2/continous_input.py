while True:
    n = input("enter a number:")

    if n == "quit":
        print("quiting...")
        break;

    v = int(n)
    if v > 0:
        print("entered number is positive")
    elif v < 0:
        print("entered number is negative")

    else:
        print("quiting....")
        break
     
          