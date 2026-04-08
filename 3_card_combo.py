#!/usr/bin/python3

#learning maps, aka dictionaries: 
#keys->the first value. values->the second value. items->the whole item

import os # -> os.system('clear')
from time import sleep
import random

full_poker_deck = {'Ace of Diamonds':14, 'Ace of Hearts':14, 'Ace of Clubs':14, 'Ace of Spades':14,
'King of Diamonds':13, 'King of Hearts':13, 'King of Clubs':13, 'King of Spades':13,
'Queen of Diamonds':12, 'Queen of Hearts':12, 'Queen of Clubs':12, 'Queen of Spades':12,
'Jester of Diamonds':11, 'Jester of Hearts':11, 'Jester of Clubs':11, 'Jester of Spades':11,
'Ten of Diamonds':10, 'Ten of Hearts':10, 'Ten of Clubs':10, 'Ten of Spades':10,
'Nine of Diamonds':9, 'Nine of Hearts':9, 'Nine of Clubs':9, 'Nine of Spades':9,
'Eight of Diamonds':8, 'Eight of Hearts':8, 'Eight of Clubs':8, 'Eight of Spades':8,
'Seven of Diamonds':7, 'Seven of Hearts':7, 'Seven of Clubs':7, 'Seven of Spades':7,
'Six of Diamonds':6, 'Six of Hearts':6, 'Six of Clubs':6, 'Six of Spades':6,
'Five of Diamonds':5, 'Five of Hearts':5, 'Five of Clubs':5, 'Five of Spades':5,
'Four of Diamonds':4, 'Four of Hearts':4, 'Four of Clubs':4, 'Four of Spades':4,
'Three of Diamonds':3, 'Three of Hearts':3, 'Three of Clubs':3, 'Three of Spades':3,
'Deuce of Diamonds':2, 'Deuce of Hearts':2, 'Deuce of Clubs':2, 'Deuce of Spades':2}

os.system('clear')

def player_dealing():
    player_hand=random.sample(sorted(full_poker_deck.items()),3)
    print()
    print(f"\n  Player's hand is: \n")
    print(sorted(player_hand, reverse=True, key=lambda x:x[1]))
            
    return player_hand

def computer_dealing():
    computer_hand=random.sample(sorted(full_poker_deck.items()),3)
    print()
    print(f"\n  Computer's hand is: \n")
    print(sorted(computer_hand, reverse=True, key=lambda x:x[1]))
        
    return computer_hand

player_hand = player_dealing()
computer_hand = computer_dealing()

if player_hand > computer_hand:
    print(f"\n  Computer wins!\n")
elif computer_hand > player_hand:
    print(f"\n  Player wins!\n")
else:
    print(f"\n  We have a tie, draw again!\n")

print()
sleep(1)

