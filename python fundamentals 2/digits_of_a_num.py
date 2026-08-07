# Write a function that prints the digits of a number.
# For example,
# there are 3 digits in 312, and we need to print them. n = 312
# The rightmost digit of a number N is N % 10. 
# Hint: And to remove the rightmost digit from a number, we can do N = N // 10.]

#solution1

num = int(input("enter a number: "))

# while num > 0:
#     rd = num % 10
#     print(rd)
#     num = num // 10



for i in str(num):
    print(i)