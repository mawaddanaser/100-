# List Comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)
#################

new_list = [n*2 for n in range(1,5)]
print(new_list)
######################

names = ["Alex", "Bath", "Caroline", "Dave", "Eleanor", "Ferddie"]
capital_names = [name.upper() for name in names if len(name) > 5]
print(capital_names)
