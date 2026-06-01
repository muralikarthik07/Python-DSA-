a = 10
b = 20

# Swap the values of a and b
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a) 
print("b =", b)
# Alternatively, in Python, you can swap values without using a temporary variable:
a = 10  
b = 20
a, b = b, a
print("After swapping without temp variable:")
print("a =", a)
print("b =", b)