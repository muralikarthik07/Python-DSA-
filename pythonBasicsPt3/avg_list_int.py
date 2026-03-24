
nlen = int(input("enter how many numbers you want to enter: "))
numbers = []


while nlen > 0:
    numbers.append(int(input("enter a positive number: ")))
    nlen = nlen -1


#python method to find the average of a list of integers
def avg_list_py_method(numbers):
    print("the average of the numbers is:", sum(numbers)/len(numbers))

#general method to find the average of a list of integers
def avg_list_int(numbers):
    sum = 0
    for i in numbers:
        sum = i + sum
    return sum / len(numbers)

avg_list_int(numbers)
avg_list_py_method(numbers)
