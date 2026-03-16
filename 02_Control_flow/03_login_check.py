username = input("Enter username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("User not found")


"""
output:
Enter username: admin
Enter your password: 1234
Login Successful

"""