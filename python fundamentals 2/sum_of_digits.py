def sum_of_digits(n):
    inti = 0
    sum = 0

    while n != 0:
        a = n % 10
        n = n // 10
        sum = sum + a

    return sum 
     







n = int(input("enter the number: "))
print(sum_of_digits(n))