"""
This is a Blackjack game that a player can play against the computer. The goal of this game is for the player to have a higher hand than the dealer but less than or equal 21. The player can keep asking for cards, but he/she will lose if they go higher than 21. To make it more interesting the player can bet money. If they win they will get double the bet. 

First, the game will ask the player how much they will bet. Then the computer will issue two cards for itself and give them 2 cards. The computer’s hand will not be shown. The player can then keep asking for more cards but as soon as they go over 21 the computer will tell them that they lost. Once the player stops asking for cards they will be told if they won or lost. It will ask the player if they want to play again. If yes then the code loops, if no then the game ends
"""

import random
#dictionary for storing the cards
deck = {
  "diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen", "ace"],
  "clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen", "ace"],
  "spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen", "ace"],
  "hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen", "ace"]
}
suite_deck = ["diamonds", "hearts", "spades", "clubs"]
player_hand = []
comp_hand = []
player_count = []
comp_count = []
MIN_BET = 50
GAME_WON = 1
GAME_DRAWN = 2
GAME_LOST = 3
INSUFFICIENT_FUNDS = -1
bank = 1000

WELCOME_MESSAGE="Welcome to Pragyan's Black Jack!!! The goal of the game is to have a higher hand than the dealer. To do that, you can keep asking for cards, but if you go higher than 21, you lose. Jacks, kings, and queens are worth 10 and, aces are worth 11. Note: you will be given $1000 to bet, but if you run out, you lose. Also you have to bet a minimum of $50 to play. Good luck!"

"""
This function returns a number and a card. The number is used in player_count and comp_count to add them up. the formatted card is written in a way that is easy for the player to read. it is also the thing that is displayed
"""
def get_a_new_card():
  deck_removal_dict = deck
  rand_suite = random.randint(0, 3)
  suite = suite_deck[rand_suite]
  rand_card = random.randint(0, len(deck_removal_dict[suite]) - 1)
  card = deck_removal_dict.get(suite)[rand_card]
  deck_removal_dict[suite].pop(rand_card)
  formatted_card = str(card) + " of " + str(suite)
  card_value = card
  if card == 'jack' or card == 'queen' or card == 'king':
    card_value = 10
  if card == 'ace':
    card_value = 11

  return [card_value, formatted_card]



"""
This function gets bet amount from the Player. It does some basic validations.
"""
def get_bet():
  print("How much would you like to bet?")
  if bank < MIN_BET:
    print("Sorry, you don't have money to play. Go back to work!")
    return INSUFFICIENT_FUNDS
    
  bet=input()
  while True:
    try:
      bet = int(bet)
    except ValueError:
      print("Please enter a valid bet value")
      bet = input()
      continue

    if bet >= MIN_BET and bet<= bank: 
      print("Thank you for your bet.")
      return(bet)
      break
    
    if bet < MIN_BET:
      print("the minimum bet is $50. Please bet more than that")
      bet=input()
      continue

    if bet > bank:
      print("Your bet is higher than what is in the bank. Please enter a lower amount")
      bet =input()
      continue



"""
This function sets up a game; issues inital cards to the player and comp
"""
def initiate_game():
  for x in range(2):
    card = get_a_new_card()
    player_count.append(card[0])
    player_hand.append(card[1])

    card = get_a_new_card()
    comp_count.append(card[0])
    comp_hand.append(card[1])

  if sum(player_count) > 21 or sum(comp_count) > 21:
    print("reset")
    reset_game()
    initiate_game()


"""
This function supports additional card request
"""
def ask_for_more_cards():
  print("your hand is")
  print(str(player_hand) +" count:"+ str(sum(player_count)))
  print("would you like another card(yes or no)")
  answer = input()
  answer_y = answer.lower().startswith("y")
  answer_n = answer.lower().startswith("n")
  #user doesn't want more cards
  if answer_n == True:
    return

  if answer_y == True:
    # user wants more cards
    card = get_a_new_card()
    player_count.append(card[0])
    player_hand.append(card[1])
    if sum(player_count) <= 21:
      ask_for_more_cards()
    else:
      print(str(player_hand) +" count:"+ str(sum(player_count)))
      return
  else:
    print("invalid input")
    ask_for_more_cards()



"""
This function manages logic for getting cards for the comp
"""
def comp_logic():
  while sum(comp_count) <= 15:
    card = get_a_new_card()
    comp_count.append(card[0])
    comp_hand.append(card[1])



"""
This function evaluates who won the game
"""
def check_if_user_won():
  # if both are >21 - draw
  if sum(player_count) > 21 and sum(comp_count) > 21:
      print("You both went over 21. Your money will be returned")
      return GAME_DRAWN
  # if both are equal - draw
  if sum(player_count) == sum(comp_count):
    print("You tied. Your money will be returned")
    return GAME_DRAWN
  # if player < 21 and comp>21 - Player won
  if sum(player_count) <= 21 and sum(comp_count) > 21:
      print("You win")
      return GAME_WON
  # if player > 21 and comp < 21 - Comp won
  if sum(player_count) > 21 and sum(comp_count) <= 21:
      print("You lose :-(")
      return GAME_LOST
  # player is greater than comp
  if sum(player_count) > sum(comp_count):
    print("You win!!!")
    return GAME_WON
  else:
    print("You lose")
    return GAME_LOST




"""
This function has logic for playing a game
"""
def play():
  bet = get_bet()
  bank_temp = 0
  if bet == INSUFFICIENT_FUNDS:
    return INSUFFICIENT_FUNDS
  
  #set the game; issue two cards to user and comp
  initiate_game()
  ask_for_more_cards()
  comp_logic()

  print("Comp Hand: ")
  print(str(comp_hand) + " count:" +str(sum(comp_count)))
  game_status = check_if_user_won()
  if game_status == GAME_WON:
    bank_temp = bank + bet
  elif game_status == GAME_LOST:
    bank_temp = bank - bet
  else:
    bank_temp=bank

  return bank_temp
    
def reset_game():
  player_hand.clear()
  comp_hand.clear()
  player_count.clear()
  comp_count.clear()

print(WELCOME_MESSAGE)
while (True):
  print()
  print("-------- Starting Game --------")
  print("Bank Balance: " + "$" + str(bank))
  bank = play()
  if bank == INSUFFICIENT_FUNDS:
    break
    
  print("Bank Balance: " + "$" + str(bank))
  print("-------- Game Over --------")
  
  print()
  print("Do you want to play a new game (yes or enter any key to exit the game)")
  answer = input()
  answer_y = answer.lower().startswith("y")
  if (answer_y):
    reset_game()
    continue
  break
