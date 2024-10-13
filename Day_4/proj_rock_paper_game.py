rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(player_choice)
comp_choices = [rock, paper, scissors]
comp_choice = random.choice(comp_choices)
print(comp_choice)
if comp_choice == rock and player_choice == 2:
  print("You lost")
elif comp_choice == scissors and player_choice == 1:
  print("You lost")
elif comp_choice == paper and player_choice == 0:
  print("You lost")
elif comp_choice == player_choice:
  print("It's a draw")
else:
  print("You Won")




