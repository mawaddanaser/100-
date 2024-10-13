# Function as return value
def multiplier(factor):
    def multiply(x):
       return x * factor
    return multiply


double = multiplier(2)
triple = multiplier(3)

print(f"Double of 5: {double(5)}")
print(f"Triple of 4: {triple(4)}")