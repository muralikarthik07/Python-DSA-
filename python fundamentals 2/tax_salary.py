# Write a program that takes as input. Using conditional statements, calculate the based on these rules:
# Q1 salary final tax rate
# • If salary <30,000→5%
# • If salary is 30,000–70,000→15%
# • If salary >70,000→25%

salary = int(input("Please enter your salary: "))

if salary < 30000:
    print("you will be paying 5% tax.")
elif (salary >= 30000 and salary <= 70000):
    print("you will be paying 15% tax.")
else:
    print("you will be paying 25% tax.")