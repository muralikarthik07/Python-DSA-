#Python method
tp = (1,2,3,4,5,6,7,8,9,10)

even_tuple = tuple(i for i in tp if i % 2 == 0)
odd_tuple = tuple(i for i in tp if i % 2 != 0)

print("Even tuple: ", even_tuple)
print("Odd tuple: ", odd_tuple)

#General method
tp2 = (1,2,3,4,5,6,7,8,9,10)

even = []
odd = []

for i in tp2:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

eventp = tuple(even)
oddtp = tuple(odd)

print("even tuple", eventp)
print("odd tuple", oddtp)


