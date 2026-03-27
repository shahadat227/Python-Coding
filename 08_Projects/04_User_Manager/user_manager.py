print("1. Add User")
print("2. View Users")

choice = input("Enter choice: ")

if choice == "1":
    name = input("Enter name: ")
    email = input("Enter email: ")

    with open("D:/Python-Coding/08_Projects/04_User_Manager/user_info.txt", "a") as file:
        file.write(name + ", " + email + "\n")
    
    print("User saved!")

elif choice == "2":
    with open("D:/Python-Coding/08_Projects/04_User_Manager/user_info.txt", "r") as file:
        print(file.read())
    
else:
    print("Invalid choice!")

"""
1. Add User
2. View Users
Enter choice: 1
Enter name: Shahadat
Enter email: shahadathossen227@gmail.com
User saved!
"""
