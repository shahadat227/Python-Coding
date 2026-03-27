print("Simple Calculator")

try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, - , *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result: ", num1 + num2)
    elif op == "-":
        print("Result: ", num1 - num2)
    elif op == "*":
        print("Result: ", num1 * num2)
    elif op == "/":
        print("Result: ", num1 / num2)
    else:
        print("Invalid Operator!")

except:
    print("Error! Invalid Input.")

"""
output:
Simple Calculator
Enter first number: 10
Enter operator (+, - , *, /): +
Enter second number: 20
Result:  30.0
"""
        
        
