class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

calc = Calculator()

print("Addition: ", calc.add(10, 5))
print("Subtract: ", calc.subtract(10, 5))

"""
output:
Addition:  15
Subtract:  5
"""