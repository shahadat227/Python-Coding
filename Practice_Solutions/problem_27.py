try: 
    num = int(input("Enter number: "))
    print("Number is: ", num)

except ValueError:
    print("Invalid input! Please enter a valid number.")

"""
output:
Enter number: abc
Invalid input! Please enter a valid number.
"""