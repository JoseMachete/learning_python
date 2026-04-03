#!/usr/bin/python3
# Let's code a parosci game.

import random  

def get_choices():
    print()
    player_choice= input("  Enter a choice: rock,paper,scissors,spock,lizard : ")
    options=["rock","paper","scissors","spock","lizard"]
    computer_choice=random.choice(options)
    print()
    choices={"player": player_choice, "computer": computer_choice} 
    return choices
    
    
def check_win(player, computer):
    print(f"  You choose {player}, Computer chooses {computer}")
    if player == computer:
        return "  Tie, no winner."
    elif player == "rock" and computer == "scissors":
        return "  Rock smashes Scissors!"
    elif computer == "rock" and player == "scissors":
        return "  Rock smashes Scissors!"
    elif player == "rock" and computer == "lizard":
        return "  Rock smashes Lizard!"
    elif computer == "rock" and player == "lizard":
        return "  Rock smashes Lizard!"
    elif player == "scissors" and computer == "lizard":
        return "  Scissors decapitates Lizard!"
    elif computer == "scissors" and player == "lizard":
        return "  Scissors decapitates Lizard!"
    elif player == "scissors" and computer == "paper":
        return "  Scissors cut paper!"
    elif computer == "scissors" and player == "paper":
        return "  Scissors cut Paper!"
    elif player == "paper" and computer == "rock":
        return "  Paper covers Rock!"
    elif computer == "paper" and player == "rock":
        return "  Paper covers Rock!"
    elif player == "paper" and computer == "spock":
        return "  Paper disproves Spock!"
    elif computer == "paper" and player == "spock":
        return "  Paper disproves Spock!"
    elif player == "lizard" and computer == "paper":
        return "  Lizard eats Paper!"
    elif computer == "lizard" and player == "paper":
        return "  Lizard eats Paper!"
    elif player == "lizard" and computer == "spock":
        return "  Lizard poisons Spock!"
    elif computer == "lizard" and player == "spock":
        return "  Lizard poisons Spock!"
    elif player == "spock" and computer == "rock":
        return "  Spock vaporizes Rock!"
    elif computer == "spock" and player == "rock":
        return "  Spock vaporizes Rock!"
    elif player == "spock" and computer == "scissors":
        return "  Spock smashes Scissors!"
    elif computer == "spock" and player == "scissors":
        return "  Spock smashes Scissors!"

choices=get_choices()
result=check_win(choices["player"], choices["computer"])
print()
print(result)
print()        
