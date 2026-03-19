student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["department"] = input("Enter department: ")

print("\nStudent Profile")
for key, value in student.items():
    print(key, ":", value)

"""
output: 
Enter name: Shahadat
Enter age: 26
Enter department: CSE

Student Profile
name : Shahadat
age : 26
department : CSE
"""