def print_even_numbers(a,b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)


# calling function
a = int(input("enter number a:"))
b = int(input("enter number b:"))
print_even_numbers(a, b) 