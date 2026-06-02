def calculator(a, b, operation):
    if operation == "+":
        add = a + b
        return add
    
    elif operation == "-":
        sub = a - b
        return sub
    
    elif operation == "*":
        mul = a * b
        return mul
    
    elif operation == "/":
        div = a // b
        return div
    

a = float(input("enter the a number:"))
b = float(input("enter the b number:"))
operation = input("enter the operation +,-,*,/:")

print(calculator(a, b, operation))