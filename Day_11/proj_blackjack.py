import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def init_players_cards():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    return user_cards, computer_cards


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will   represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
def is_blackjack(computer_score, user_score):
    if computer_score == 0 or user_score == 0 or user_score > 21:
        return True
    return False


# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.


# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
def user_turn(user_cards, user_score, computer_cards):
    to_continue = False
    while input("if you want to draw another card?: Type 'y' or 'n': ") == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        to_continue = True
        print(f"""
      Your cards: {user_cards}. Current Score: {user_score}
      Computer first card: {computer_cards[0]}
    """)
    return user_score, to_continue


# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
def computer_turn(computer_cards, computer_score):
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    return computer_score


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
def game():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        user_cards, computer_cards = init_players_cards()
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if is_blackjack(user_score, computer_score):
            return

        print(f"""
      Your cards: {user_cards}. Current Score: {user_score}
      Computer first card: {computer_cards[0]}
    """)

        # Hint 10:
        user_score, to_continue = user_turn(user_cards, user_score, computer_cards)
        if to_continue:
            computer_score = computer_turn(computer_cards, computer_score)
        print(f"""
      Your final hand: {user_cards}. Your final score: {user_score}
      Computer final hand: {computer_cards}. Computer final score: {computer_score}
    """)

        result = compare(user_score, computer_score)
        print(result)


def main():
    game()

    while input("Do you want to restart the game . Write 'y'or 'n': ") == "y":
        clear()
        game()


main()
