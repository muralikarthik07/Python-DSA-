def divisible_by_two_numbers(num1, num2):
    for i in range(1, 101):
        if i % num1 == 0 and i % num2 == 0:
            print(i)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
divisible_by_two_numbers(num1, num2)