# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_height = 0
for h in student_heights:
  total_height += h
  number_of_student = n + 1
  averge = round((total_height /   number_of_student)) 
print(f"total height = {total_height}")
print(f"number of students = {number_of_student}")
print(f"average height = {averge}")
    
  
