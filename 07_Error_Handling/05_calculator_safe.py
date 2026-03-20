try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Invalid number input!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else: 
    print("Result: ", result)

finally:
    print("Program finished!")