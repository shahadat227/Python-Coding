try: 
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")
    
except ValueError as e:
    print("Error:", e)

"""
output:
Enter age: -1
Error: Age cannot be negative
"""