target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total_even_number = 0
for number in range(2, target+1, 2):
  total_even_number += number
print(total_even_number)
  