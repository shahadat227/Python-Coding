import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)

"""
output:
Enter password length: 8
Generated Password: j;'L~)e1
"""