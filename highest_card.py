#!/usr/bin/python3

import random

def diam_ace():
    print(r"  ------  ")
    print(r" |A     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Ace of Diamonds'
        
def hear_ace():
    print(r"  ------  ")
    print(r" |A     |  ")
    print(r" |      |  ")
    print(r" | /\/\ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Ace of Hearts'
    
def club_ace():
    print(r"  ------  ")
    print(r" |A __  |  ")
    print(r" | |  | |  ")
    print(r" ||    ||  ")
    print(r" | \  / |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Ace of Clubs'
    
def spad_ace():
    print(r"  ------  ")
    print(r" |A     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \/\/ |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Ace of Spades'

def diam_king():
    print(r"  ------  ")
    print(r" |K     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'King of Diamonds'
        
def hear_king():
    print(r"  ------  ")
    print(r" |K     |  ")
    print(r" |      |  ")
    print(r" | /\/\ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'King of Hearts'
    
def club_king():
    print(r"  ------  ")
    print(r" |K __  |  ")
    print(r" | |  | |  ")
    print(r" ||    ||  ")
    print(r" | \  / |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'King of Clubs'
    
def spad_king():
    print(r"  ------  ")
    print(r" |K     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \/\/ |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'King of Spades'

def diam_queen():
    print(r"  ------  ")
    print(r" |Q     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Queen of Diamonds'
        
def hear_queen():
    print(r"  ------  ")
    print(r" |Q     |  ")
    print(r" |      |  ")
    print(r" | /\/\ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Queen of Hearts'
    
def club_queen():
    print(r"  ------  ")
    print(r" |Q __  |  ")
    print(r" | |  | |  ")
    print(r" ||    ||  ")
    print(r" | \  / |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Queen of Clubs'
    
def spad_queen():
    print(r"  ------  ")
    print(r" |Q     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \/\/ |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Queen of Spades'

def diam_jester():
    print(r"  ------  ")
    print(r" |J     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Jester of Diamonds'
        
def hear_jester():
    print(r"  ------  ")
    print(r" |J     |  ")
    print(r" |      |  ")
    print(r" | /\/\ |  ")
    print(r" | \  / |  ")
    print(r" |  \/  |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Jester of Hearts'
    
def club_jester():
    print(r"  ------  ")
    print(r" |J __  |  ")
    print(r" | |  | |  ")
    print(r" ||    ||  ")
    print(r" | \  / |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Jester of Clubs'
    
def spad_jester():
    print(r"  ------  ")
    print(r" |J     |  ")
    print(r" |  /\  |  ")
    print(r" | /  \ |  ")
    print(r" | \/\/ |  ")
    print(r" | _||_ |  ")
    print(r" |      |  ")
    print(r"  ------  ")
    return 'Jester of Spades'

aces = [diam_ace, hear_ace, club_ace, spad_ace]
kings = [diam_king, hear_king, club_king, spad_king]
queens = [diam_queen, hear_queen, club_queen, spad_queen]
jesters = [diam_jester, hear_jester, club_jester, spad_jester]

print()
options = [diam_ace, hear_ace, club_ace, spad_ace, diam_king, hear_king, club_king, spad_king, diam_queen, hear_queen, club_queen, spad_queen, diam_jester, hear_jester, club_jester, spad_jester]

player_card=random.choice(options)()
computer_card=random.choice(options)()
card_picks={"  Player gets the... ": player_card, "  Computer gets the... ": computer_card}
    
print()
print(card_picks)
print()

if player_card == aces and computer_card == aces:
    print("  It's a tie, draw again. ")
elif player_card == kings and computer_card == kings:
    print("  It's a tie, draw again. ")
elif player_card == queens and computer_card == queens:
    print("  It's a tie, draw again. ")
elif player_card == jesters and computer_card == jesters:
    print("  It's a tie, draw again. ")
elif player_card == aces and computer_card != aces:
    print("  Player wins! ")
elif computer_card == aces and player_card != aces:
    print("  Computer wins! ")
elif player_card == kings or queens and computer_card == jesters:
    print("  Player wins! ")
elif computer_card == kings or queens and player_card == jesters:
    print("  Computer wins! ")
elif player_card == jesters and computer_card != jesters:
    print("  Computer wins! ")
elif computer_card == jesters and player_card != jesters:
    print("  Player wins! ")

   
