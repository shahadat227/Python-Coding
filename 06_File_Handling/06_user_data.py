name = input("Enter your name: ")
age = input("Enter your age: ")

with open("D:/Python-Coding/06_File_Handling/users.txt", "a") as file:
    file.write(name + ", "+ age + "\n")

print("Data saved!")

"""
output:
Enter your name: Shahadat
Enter your age: 26
Data saved!
"""