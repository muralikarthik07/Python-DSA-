lists = list(map(int,input("enter a strnig: ")))

sum = 0
for i in lists:
    sum = i + sum

avg = sum / len(lists)
print(avg)