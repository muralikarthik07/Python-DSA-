def number_of_count(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

num = int(input("enter a number: "))
print(number_of_count(num))