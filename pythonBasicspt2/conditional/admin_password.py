admin = "admin"
password = "admin123"

user = input("enter the username: ")
user_password = input("enter the password: ")

if(user == admin and user_password == password):
    print("correct credentials")
else:
    print("incorrect credentials")