#Purpose of code: Simple quiz game that will ask the user some questions. The purpose behind the code is to get back into Python and refresh my mind on it's syntaxes.
#Code Written by: Socrates Mridha
#Start Date:07/07/2023
#End Date:07/07/2023

'''
Questions and answers for the game:
Q1:What is the capital of Canada?
A1:Ottawa

Q2:What is 4x4?
A1:16

Q3:How many months are there in a year?
A3:12

Q4:What colour is grass?
A4:green

Q5:Does the Moon rotate around the Sun?
A5:yes

Q6:Is water wet?
*Question 6 is a trick question and there is no correct answers*
'''

score = 0

#Title
title = "WELCOME TO MY QUIZ!"
newTitle = title.center(60)
print ("\n\n",newTitle)

#Rules
print("\n\nRules: \nYou will be asked 5 Questions. \nThe inputs for the answers are not case sensitive.")
print ("For questions that requires a number for its answer, \nyou may input a number or spell out the number.")

#Confirm if the user wants to play, if not, Terminate the application.
playing = input("\nDo you still want to play? ")

if playing.lower() != "yes":
    quit()
print ("Okay! Let's play :)")

#-------------------------------------------------------Question One-------------------------------------------------------
answerOne = input("\nQ1: What is the capital of Canada?: ")

if answerOne.lower() == "ottawa":
    print('Correct!')
    score+=1
else:
    print("Incorrect")
#-------------------------------------------------------Question Two-------------------------------------------------------
answerTwo = input("\nQ2: What is 4x4?(input a number): ")

if answerTwo == "16" or answerTwo.lower() == "sixteen":
    print('Correct!')
    score+=1
else:
    print("Incorrect")
#------------------------------------------------------Question Three------------------------------------------------------
answerThree = input("\nQ3: How many months are there in a year?(input a number): ")

if answerThree == "12" or answerThree.lower() == "twelve":
    print('Correct!')
    score+=1
else:
    print("Incorrect")
#------------------------------------------------------Question Four-------------------------------------------------------
answerFour = input("\nQ4: What colour is grass?: ")

if answerFour.lower() == "green":
    print('Correct!')
    score+=1
else:
    print("Incorrect")
#------------------------------------------------------Question Five-------------------------------------------------------
answerFive = input("\nQ5: Does the Moon rotate around the Sun?(yes/no): ")

if answerFive == "yes":
    print('Correct!')
    score+=1
else:
    print("Incorrect")
#-------------------------------------------------------Question Six-------------------------------------------------------
answerSix = input("\nQ6: Is water wet?: ")
print ("Just kidding, question 6 isn't a real question!")

#--------------------------------------------------------Conclusion--------------------------------------------------------
#Print out the user's score with a comment that reflects their score.
print("\nYou scored:" , score , "/5 (" , ((score/5)*100) , "%)")
if score == 5:
    print("Excellent!")
elif score == 4:
    print("Great!")
elif score == 3:
    print("Not so great...")
elif score == 2:
    print("Fail!")
elif score == 1:
    print("What happened?")
else:
    print("...")

#Give the user the option if they would like to know the answers.
giveAnswer = input("\nWould you like to know the answers?: ")

if  giveAnswer.lower() != "yes":
    print("Thanks for playing!")
    quit()
print("\nAnwers: \nA1: Ottawa \nA2: 16 \nA3: 12 \nA4: green \nA5: yes ")

print("\nThank you for playing!")
endGame = input("input anything to close app: ")
quit()