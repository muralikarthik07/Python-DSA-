# Ask the user for : Principal(P), Rate(R), Time(T). Convert all to float and compute simple interest:
#     Q9 float SI = ( P ∗ R ∗ T)/100

P = int(input("please enter the principal amount: "))
R = int(input("please enter the rate: "))
T = int(input("please enter the time: "))

SI = (float(P * R * T))/ 100
print(SI)