try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError: 
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Error! Cannont divide by zero.")

else:
    print("Result: ", result)

"""
output:
Enter first number: 10
Enter second number: 0
Error! Cannont divide by zero.
"""