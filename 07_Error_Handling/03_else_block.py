try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)

"""
output 1:
Enter number: abc
Invalid input

output2:
nter number: 10
You entered: 10
"""