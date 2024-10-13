# How to create init function:
# class MyClass:
#     def __init__(self, parameter1, parameter2):
#         # Initialization code goes here
#         self.attribute1 = parameter1
#         self.attribute2 = parameter2
#
# # Creating an instance of MyClass
# my_object = MyClass(parameter1_value, parameter2_value)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")


# creating an instance of the Dog class
my_dog = Dog(name="Buddy", age=3)


# Accessing attributes and calling method
print(my_dog.name)
print(my_dog.age)
my_dog.bark()
