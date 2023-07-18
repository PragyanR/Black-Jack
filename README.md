Capstone Program Explanation:
For the capstone final project, I will be writing a Blackjack game that a player can play against the computer. The goal of this game is for the player to have a higher hand than the dealer but less than or equal 21. The player can keep asking for cards, but he/she will lose if they go higher than 21. To make it more interesting the player can bet money. If they win they will get double the bet. 

Here are some of the conditions for the game:
Only 1 player can play this game
The dealer is the  computer
The player will be given $1,000 to bet
The minimum bet is $50 
The player needs to be able to type to provide game input.
The player cannot split their hand
Ace counts as 11, not as 1
King, jack, and queen count as 10
If you tie, you get your bet back
After every game the deck resets 


Explanation of how the game will function
First, the game will ask the player how much they will bet. Then the computer will issue two cards for itself and give them 2 cards. The computer’s hand will not be shown. The player can then keep asking for more cards but as soon as they go over 21 the computer will tell them that they lost. Once the player stops asking for cards they will be told if they won or lost. It will ask the player if they want to play again. If yes then the code loops, if no then the game ends


Description of the modules that will need to be developed in order to accomplish the functionality described in step 1 of the SDLC

Pseudocode

Dictionary:
deck={"diamonds":[1,2,3,4,5,6,7,8,9,10,"jack","king","queen","ace"],
"Clubs":[1,2,3,4,5,6,7,8,9,10,"jack","king","queen","ace"],
"Spades":[1,2,3,4,5,6,7,8,9,10,"jack","king","queen","ace"],
"Hearts":[1,2,3,4,5,6,7,8,9,10,"jack","king","queen","ace"]}
List of all the suits[spades,hearts,ect]
List for storing the players hand[]
#this will be displayed so it will be formatted like- # of suite
List for storing the computers hand[]
#same as above
Player count
comp_count

Define a function to get a card for both player and computer.
new _card()
Gets random number from 0-3
Gets random suite from suoite list
Gets randm number from 0 to 12
num=gets random number(or face)
	Formatted card=”num of suite”
Returns card,formated card
	
Start game()
	Ask how much they want to bet
	Check if input is >50, <bank and if an int
	Thank you for your bet
	Loops twice
		Puts format card in player_hand
		Puts num in player count
	
		Puts format card in comp_hand
		Puts num in comp_hand
ask_for _card()definse a function if they want a new card or not
	Do you want another card?
	If input yes
		Put format card in player_hand
		Put num in player count
		If comp_count >=15
			Continue
		Else
			Puts format card in comp_hand
			Puts num in comp_hand

	


check()Functions adds all values of hand then comp hand then compares it 
In a for loop
	Check if count of x is jack king or queen
		If so turn them into 10
	Check if count of x is ace
		Set as 11
	
	
hand=sum(hand)
comp_hand=sum(comp_hand)

If comp hand < 21
If hand <21
		If hand >comps hand
			You win
			bank=bank+bet
Else 
print you lose
		bank=bank-bet
Else 
Print you lose
bank=bank-bet
Else
	Dealer has busted return the money
	Ask to play again


“””
