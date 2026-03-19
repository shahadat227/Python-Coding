class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def show(self):
        print("Brand: ", self.brand )
        print("Price: ", self.price)
        

cr = Car("Toyota", 2000000)
cr.show()

"""
output:
Brand:  Toyota
Price:  2000000
"""

