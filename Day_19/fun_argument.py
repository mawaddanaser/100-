# Higher order functions
# Function as argument

def square(x):
    return x * x


def cube(x):
    return x * x * x


def apply_operation(fun, value):
    return fun(value)


square_result = apply_operation(square, 5)
cube_result = apply_operation(cube, 3)

print(f"square: {square_result}")
print(f"cube: {cube_result}")
