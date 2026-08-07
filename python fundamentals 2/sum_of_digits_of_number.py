n = int(input("Enter a number: "))

sum = 0
while n > 0:
    v = n % 10
    sum = sum + v
    n = n // 10

print(sum) 

