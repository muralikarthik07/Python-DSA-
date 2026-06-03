#using string
str = input("Enter a string: ")

reverse = ""
for ch in str:
    reverse = ch + reverse

if str == reverse:
    print("palindrome")
else:
    print("not a palindrome")

#using python method

if str == str[::-1]:
    print("palindrome number")
else:
    print("not a palindrome")