def cal_cu(a, b, operation):
    if operation == "+":
        return(a + b)

    elif operation == "-":
        return(a-b)

    elif operation == "*":
        return(a * b)

    elif operation == "%":
        return(a % b)

    elif operation == "//":
        return(a // b)

a = int(input("enter a number: "))
b = int(input("enter b number:"))

operation = input("please enter operation +, -, *, //: ")

result = cal_cu(a, b, operation)
print(result)
