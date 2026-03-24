#check palindrome or not for numbers
def is_palindrome_num(s):
    original = s
    rev = 0

    while original > 0:
        digit = original % 10
        rev = rev * 10 + digit
        original = original // 10

    if s == rev:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
 
#function for words.
def is_palindrome_letters(word):
    if word == word[::-1]:
        print("yes it is palindrome")
    else:
        print("not a palindrome")

num = int(input("enter the num: "))
is_palindrome_num(num)

word = input("enter the word: ")
is_palindrome_letters(word)