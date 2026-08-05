# The user enters a string containing a number 
# (e.g.,).Convert it to :

# Q4"45"
# •an integer
# •a float
# •a string again
# Print all three value swith their types

num = input("please enter a number: ")

og = print(num)
print(type(og))

float_num = float(num)
print(type(float_num))

str_num = str(num)
print(type(str_num))