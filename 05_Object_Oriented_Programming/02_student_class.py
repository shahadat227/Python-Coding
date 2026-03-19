class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Shahadat", 26)
s2 = Student("Rakib", 25)

s1.show_info()
s2.show_info()

"""
output:
Name: Shahadat
Age: 26
Name: Rakib
Age: 25
"""