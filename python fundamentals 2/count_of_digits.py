def count_of_digits(n):
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count 



n = int(input("Enter the number:"))
print(count_of_digits(n))