# Ask the user for a temperature in Celsius(string input).Convert it to float,then calculate and print temperature in Fahrenheit.
#     Q7 float Conversion formula :Fahrenheit Temp=(CelsiusTemp∗(9/5))+32

temp = input("please enter your temperature:")
celsiustemp = float(temp)

fahrenheit_temp = celsiustemp * (9/5) + 32
print(fahrenheit_temp)