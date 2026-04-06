#!/usr/bin/python3

import os
from time import sleep
import random

def diam_ace():
    print(r""" 
       ----------  
      |          |
      | A        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        A |
      |          |
       ----------  
         
    """ )
    
    return 'Ace of Diamonds'
        
def hear_ace():
    print(r""" 
       ----------  
      |          |
      | A        |  
      |          |
      |   /\/\   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        A |
      |          |
       ----------  
         
    """ )
    
    return 'Ace of Hearts'
    
def club_ace():
    print(r""" 
       ----------  
      |          |
      | A        |  
      |    __    |
      |  _/  \_  |  
      | /      \ |  
      | \_    _/ |  
      |   \  /   |  
      |   _||_   |  
      |        A |
      |          |
       ----------  
         
    """ )
    
    return 'Ace of Clubs'
    
def spad_ace():
    print(r""" 
       ----------  
      |          |
      | A        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      | |      | |  
      |  \/||\/  |  
      |   _||_   |  
      |        A |
      |          |
       ----------  
         
    """ )
    
    return 'Ace of Spades'

def diam_king():
    print(r""" 
       ---------- 
      |          |
      | K        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        K |
      |          |
       ----------  
    
    """ )
    return 'King of Diamonds'
        
def hear_king():
    print(r""" 
       ----------  
      |          |
      | K        |  
      |          |
      |   /\/\   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        K |
      |          |
       ----------  
             
    """ )
    return 'King of Hearts'
    
def club_king():
    print(r""" 
       ----------  
      |          |
      | K        |  
      |    __    |
      |  _/  \_  |  
      | /      \ |  
      | \_    _/ |  
      |   \  /   |  
      |   _||_   |  
      |        K |
      |          |
       ----------  
         
    """ )
    return 'King of Clubs'
    
def spad_king():
    print(r""" 
       ----------  
      |          |
      | K        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      | |      | |  
      |  \/||\/  |  
      |   _||_   |  
      |        K |
      |          |
       ----------  
             
    """ )
    return 'King of Spades'

def diam_queen():
    print(r""" 
       ----------  
      |          |
      | Q        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        Q |
      |          |
       ----------  
         
    """ )
    return 'Queen of Diamonds'
        
def hear_queen():
    print(r""" 
       ----------  
      |          |
      | Q        |  
      |          |
      |   /\/\   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        Q |
      |          |
       ----------  
         
    """ )
    return 'Queen of Hearts'
    
def club_queen():
    print(r""" 
       ----------  
      |          |
      | Q        |  
      |    __    |
      |  _/  \_  |  
      | /      \ |  
      | \_    _/ |  
      |   \  /   |  
      |   _||_   |  
      |        Q |
      |          |
       ----------  
         
    """ )
    return 'Queen of Clubs'
    
def spad_queen():
    print(r""" 
       ----------  
      |          |
      | Q        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      | |      | |  
      |  \/||\/  |  
      |   _||_   |  
      |        Q |
      |          |
       ----------  
         
    """ )
    return 'Queen of Spades'

def diam_jester():
    print(r""" 
       ----------  
      |          |
      | J        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        J |
      |          |
       ----------  
         
    """ )
    return 'Jester of Diamonds'
        
def hear_jester():
    print(r""" 
       ----------  
      |          |
      | J        |  
      |          |
      |   /\/\   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |        J |
      |          |
       ----------  
         
    """ )
    return 'Jester of Hearts'
    
def club_jester():
    print(r""" 
       ----------  
      |          |
      | J        |  
      |    __    |
      |  _/  \_  |  
      | /      \ |  
      | \_    _/ |  
      |   \  /   |  
      |   _||_   |  
      |        J |
      |          |
       ----------  
    
    """ )
    return 'Jester of Clubs'
    
def spad_jester():
    print(r""" 
       ----------  
      |          |
      | J        |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      | |      | |  
      |  \/||\/  |  
      |   _||_   |  
      |        J |
      |          |
       ----------  
         
    """ )
    return 'Jester of Spades'

def diam_ten():
    print(r""" 
       ----------  
      |          |
      | 10       |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |       10 |
      |          |
       ----------  
         
    """ )
    return 'Ten of Diamonds'
        
def hear_ten():
    print(r""" 
       ----------  
      |          |
      | 10       |  
      |          |
      |   /\/\   |  
      |  /    \  |  
      |  \    /  |  
      |   \  /   |  
      |    \/    |  
      |       10 |
      |          |
       ----------  
         
    """ )
    return 'Ten of Hearts'
    
def club_ten():
    print(r""" 
       ----------  
      |          |
      | 10       |  
      |    __    |
      |  _/  \_  |  
      | /      \ |  
      | \_    _/ |  
      |   \  /   |  
      |   _||_   |  
      |       10 |
      |          |
       ----------  
         
    """ )
    return 'Ten of Clubs'
    
def spad_ten():
    print(r""" 
       ----------  
      |          |
      | 10       |  
      |    /\    |
      |   /  \   |  
      |  /    \  |  
      | |      | |  
      |  \/||\/  |  
      |   _||_   |  
      |       10 |
      |          |
       ----------  
         
    """ )
    return 'Ten of Spades'


aces = [diam_ace, hear_ace, club_ace, spad_ace]
kings = [diam_king, hear_king, club_king, spad_king]
queens = [diam_queen, hear_queen, club_queen, spad_queen]
jesters = [diam_jester, hear_jester, club_jester, spad_jester]
tens = [diam_ten, hear_ten, club_ten, spad_ten]

options = [diam_ace, hear_ace, club_ace, spad_ace, diam_king, hear_king, club_king, spad_king, diam_queen, hear_queen, club_queen, spad_queen, diam_jester, hear_jester, club_jester, spad_jester, diam_ten, hear_ten, club_ten, spad_ten]

player_card=random.choice(options)
computer_card=random.choice(options)
os.system ('clear')
card_picks={"  Player gets the... ": player_card(), "  Computer gets the... ": computer_card()}

print(card_picks)
sleep(1)
print()

def check_win():
    if player_card in aces and computer_card in aces:
        print("  It's a tie, draw again.")
    elif player_card in kings and computer_card in kings:
        print("  It's a tie, draw again. ")
    elif player_card in queens and computer_card in queens:
        print("  It's a tie, draw again. ")
    elif player_card in jesters and computer_card in jesters:
        print("  It's a tie, draw again. ")
    elif player_card in tens and computer_card in tens:
        print("  It's a tie, draw again. ")
    elif player_card in aces and computer_card not in aces:
        print("  Player wins! ")
    elif computer_card in aces and player_card not in aces:
        print("  Computer wins! ")
    elif player_card in tens and computer_card not in tens:
        print("  Computer wins! ")
    elif computer_card in tens and player_card not in tens:
        print("  Player wins! ")
    elif player_card in kings and computer_card in queens:
        print("  Player wins! ")
    elif computer_card in kings and player_card in queens:
        print("  Computer wins! ")
    elif player_card in kings or queens and computer_card in jesters:
        print("  Player wins! ")
    elif computer_card in kings or queens and player_card in jesters:
        print("  Computer wins! ")
    elif player_card in kings or queens and computer_card in tens:
        print("  Player wins! ")
    elif computer_card in kings or queens and player_card in tens:
        print("  Computer wins! ")
    elif player_card in queens or jesters and computer_card in tens:
        print("  Player wins! ")
    elif computer_card in queens or jesters and player_card in tens:
        print("  Computer wins! ")
    
    
check=check_win()
print()
sleep(1)

