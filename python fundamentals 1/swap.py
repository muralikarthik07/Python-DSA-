a = int(input("enter a number:"))
b = int(input("enter b number:"))

temp = a
a = b
b = temp

print(a , b)

#without using 3rd variable

a,b = b,a