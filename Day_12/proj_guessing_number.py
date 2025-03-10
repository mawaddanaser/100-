import random

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

#function to check user's guess against actual number
def check_answer(guess, answer, turns):
    """ check guess against answer. return number of turns remaining """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#make function to set difficulty
def set_difiiculty():
    level = input("Choose a difficulty. Type 'easy or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choose a random number between(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}") 

    turns = set_difiiculty()

    #Reapeat the guessing functionality if they get wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")
        return
    elif guess != answer:
     print("Guess again.")

game()