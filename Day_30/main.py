# Exeption Handling

# FileNOtFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} don't exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")

# ##############

# raise
# Bmi Example
height = float(input("Height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human height shouldn't be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
