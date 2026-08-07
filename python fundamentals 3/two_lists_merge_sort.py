l1 = list(map(int,input("enter a list: ").split()))
l2 = list(map(int,input("enter a list: ").split()))

#with predefined functions

ll = l1 + l2

# ll.sort()

# print(ll)

for i in range(len(ll)):
    for j in range(i + 1, len(ll)):
        if ll[i] > ll[j]:
            temp = ll[i]
            ll[i] = ll[j]
            ll[j] = temp

print("sorted list: ", ll)