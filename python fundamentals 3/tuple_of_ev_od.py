tp = tuple(map(int,input("enter a tuple:").split()))

even_tp = ()

odd_tp = ()

for i in tp:
    if i % 2 == 0:
        even_tp = even_tp + (i,)
    else:
        odd_tp = odd_tp + (i,)

print(even_tp)
print(odd_tp)
