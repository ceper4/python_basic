x = (input("Enter the first number: "))
try:
    x = int(x)
except: x = float(x)
y = (input("Enter the second number: "))
try:
    y = int(y)
except: y = float(y)
math_operation = input("Choose the math operation: *,-,/,+, ** :  ")
result = 0

if math_operation == "+":
    result = (x + y)

elif math_operation == "/":
    result = (x / y)

elif math_operation == "*":
    result = (x * y)

elif math_operation == "-":
    result = (x - y)

elif math_operation == "**":
    result = (x ** y)

else:
    print("Error! Please, use numbers and math operations as : x,-,/, ** or + next time!")
print (f"Result is: {result}")