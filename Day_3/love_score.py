print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
couple_name = name1 + name2
couple_name = couple_name.lower()
true_count = (
  couple_name.count("t") + 
  couple_name.count("r") + 
  couple_name.count("u") +
  couple_name.count("e")
)
love_count = (
  couple_name.count("l") + 
  couple_name.count("o") + 
  couple_name.count("v") +
  couple_name.count("e")
)
love_score = int(str(true_count) + str(love_count))
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
   
  