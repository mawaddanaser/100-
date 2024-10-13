with open("file1.txt") as data_file:
  file1 = data_file.readlines()
with open("file2.txt") as data_file:
  file2 = data_file.readlines()
#converting to list of numbers
file1_list = [int(x) for x in file1]
file2_list = [int(x) for x in file2]

result = [num for num in file1_list if num in file2_list]


# Write your code above 👆
print(result)