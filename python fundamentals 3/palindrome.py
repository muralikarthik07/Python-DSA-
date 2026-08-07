s = input("enter a string: ")

# if s[::] == s[::-1]:
#     print("entered string is a palindrome")
# else:
#     print("entered number is not a palindrome.")

n = ""

for i in s:
    n = i + n



if s == n:
    print("it is palindrome")
else:
    print("it is not a palindrome.")