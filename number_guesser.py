#Purpose: To let the user guess a number between 0 and the number inputed by the user. The app will keep asking the user till they get the random generated number correctly.
#Code Written by: Socrates Mridha
#Start Date: 08/07/2023
#End Date: 08/07/2023

#import random library
import random

print("Welcome to my number guessing game!")

#-------------------------------------------------------Ask_User_For_Input_Start-------------------------------------------------------


while True:
    top_of_range = input("\nType a number thats greater than 0: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        
        if top_of_range > 0:
            break

    else:
        print("*ERROR. Try Again.")
        
#-------------------------------------------------------Ask_User_For_Input_End--------------------------------------------------------

# Generate a random number using the user's input a max range from 0.
random_number = random.randint(1,top_of_range)
# Veriable to keep track of the number of user's guesses.
number_of_guess = 0

#-------------------------------------------------------Check_Guess_While_Loop_Start-------------------------------------------------------
# Basic while loop to keep looping till there is a break, which would be when the guess matches the random number.
while True:
    number_of_guess += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number.")
        continue

    if user_guess == random_number:
        print("\nYou got it RIGHT!")
        break
    elif user_guess > random_number:
        print("You guessed above the number.\n")
    else:
        print("You guessed below the number.\n")
#-------------------------------------------------------Check_Guess_While_Loop_End-------------------------------------------------------


print("It took you" , number_of_guess , "guesses.")
print("END OF GAME")