
while True:
    x = input("Enter the first number: ")
    if x == "exit":
        break
    y = input("Enter the second number: ")
    if y == "exit":
        break
    math_operation = input("Choose the math operation (+, -, *, /, **): ")
    if math_operation == "exit":
        break
    if "." in x:
        x = float(x)
    else:
        x = int(x)
    if "." in y:
        y = float(y)
    else:
        y = int(y)
    if math_operation not in ["+","-","*","/", "**"]:
        print("Error! Choose the math operation please!");
        math_operation = input("Choose the math operation (+, -, *, /, **): ")
    elif math_operation == "+":
        print(x+y);
    elif math_operation == "-":
        print(x-y);
    elif math_operation == "*":
        print(x*y);
    elif math_operation == "/":
        try:
            x/y
        except ZeroDivisionError:
            print("You can't divide by 0")
        else:
            print(x/y);
    elif math_operation == "**":
        print(x**y);