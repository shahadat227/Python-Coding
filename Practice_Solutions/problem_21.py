class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

cr = Car("Toyota", 2000000)

print("Brand: ",cr.brand)
print("Price: ",cr.price)
