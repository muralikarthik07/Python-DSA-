num = int(input("enter a number: "))

def print_digits(num):
    if num == 0:
        print(0)
        return
    digits = []

    while num > 0:
        digit = num % 10
        digits.append(digit)
        num = num // 10

    for digit in reversed(digits):
        print(digit)

print_digits(num)
    