n = int(input("enter the number:"))

if n <= 1:
    print("Not applicable")
else:

    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime number")
    else:
        print("not a prime number")


    
