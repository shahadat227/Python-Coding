try:
    with open("D:/Python-Coding/06_File_Handling/data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")

"""
output:
Hello Shahadat
Welcome to Python File Handling
"""