file = open("D:/Python-Coding/06_File_Handling/data.txt", "a")
file.write("\nThis is appended line")
file = open("D:/Python-Coding/06_File_Handling/data.txt", "r")
content = file.read()
print(content)

"""
output:
This is new content
This is appended line
"""