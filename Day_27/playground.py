def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
##########

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
#note: not give errors because i have a class and use get