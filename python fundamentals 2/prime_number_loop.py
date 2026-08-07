def is_prime(n):
    if n <= 1:
        print("entered number is not a prime number")
    else:
        i = 2

        while i < n:
            if n % i == 0:
                print("entered number is not a prime number.")
                break;
            i+1

        else:
            print("entered number is a prime number")
                


n = int(input("enter a number:"))
is_prime(n)