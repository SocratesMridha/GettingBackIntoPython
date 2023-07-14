#Purpose: Simple game of rock/paper/scissors. App is for the use of lists, if and while loops.
#Code Written by: Socrates Mridha
#Start Date: 13/07/2023
#End Date: 13/07/2023

import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

print("Welcome to a game of Rock, Paper and Scissors.\n")

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    #-------------------------------------------------------Win-------------------------------------------------------
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    #-------------------------------------------------------Tie-------------------------------------------------------
    elif user_input == "rock" and computer_pick == "rock":
        print("It's a tie!")
        continue

    elif user_input == "paper" and computer_pick == "paper":
        print("It's a tie!")
        continue

    elif user_input == "scissors" and computer_pick == "scissors":
        print("It's a tie!")
        continue

    #-------------------------------------------------------Lose-------------------------------------------------------
    else:
        print("You lose!")
        computer_wins += 1
    

print("\nYou won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")