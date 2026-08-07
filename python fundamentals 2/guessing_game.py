og_ons = 56
while True:
    ans = int(input("enter a number: "))

    if ans == og_ons:
        print("entered number is correct")
        break

    elif ans > og_ons:
        print("entered number is larger than the original number")

    elif ans < og_ons:
        print("entered number is smaller than the original number")