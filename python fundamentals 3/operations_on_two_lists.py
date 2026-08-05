lst1 = list(map(int, input("Enter the first list of numbers: ").split()))

lst2 = list(map(int, input("Enter the second list of numbers: ").split()))

final_list = lst1 + lst2

final_list.sort()
print("Final sorted list:", final_list)