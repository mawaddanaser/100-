# Dictionary comprehension
import random

names = ["Alex", "Bath", "Caroline", "Dave", "Eleanor", "Ferddie"]
score_student = {student: random.randint(1, 100) for student in names}
print(score_student)

passed_student = {student: score for (student, score) in score_student.items() if score > 50}
print(passed_student)