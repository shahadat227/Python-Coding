try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Enter a valid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

"""
output 1: 
Enter number: abc
Enter a valid number!

output 2:

"""