import random
import time
#test for commit

# Initialize Variables
def isValidEntry():
    invalid_entry = True
    while invalid_entry:
        user_choice = input('Rock? Paper? Scissors? ')

        if user_choice == 'Rock' or user_choice == 'Paper' or user_choice == 'Scissors':
            return user_choice
        if user_choice != 'Rock' or user_choice != 'Paper' or user_choice != 'Scissors':
            print('Invalid Input Detected.\n')
            invalid_entry = True

# 1=Rock/ 2=Paper/ 3=Scissors
def computer_throw(comp_Choice):
    if comp_Choice == 1:
        print("The computer chooses Rock")
    if comp_Choice == 2:
        print('The computer chooses Paper')
    if comp_Choice == 3:
        print('The computer chooses Scissors')

# 1=Rock/ 2=Paper/ 3=Scissors
def versus(cc, uc):
    if cc == 1 and uc == "Rock":  # Rock vs Rock
        print('Rock vs Rock \nTIE GAME')
    if cc == 2 and uc == "Rock":  # Paper vs Rock
        print('Paper vs Rock \nPaper Wins...\nYOU LOSE!')
    if cc == 3 and uc == "Rock":  # Scissors vs Rock
        print('Scissors vs Rock \nRock Wins...\nCONGRATS YOU BEAT THE COMPUTER!')
    if cc == 1 and uc == "Paper":  # Rock vs Paper
        print('Rock vs Paper \nPaper Wins\nCONGRATS YOU BEAT THE COMPUTER!')
    if cc == 2 and uc == "Paper":  # Paper vs Paper
        print('Paper vs Paper \nTIE GAME!')
    if cc == 3 and uc == "Paper":  # Scissors vs Paper
        print('Scissors vs Paper \nScissors Win\nYOU LOSE!')
    if cc == 1 and uc == "Scissors":  # Rock vs Scissors
        print('Rock vs Scissors \nRock Wins\nYOU LOSE!')
    if cc == 2 and uc == "Scissors":  # Paper vs Scissors
        print('Paper vs Scissors \nScissors Win\nCONGRATS YOU BEAT THE COMPUTER!')
    if cc == 3 and uc == "Scissors":  # Scissors vs Scissors
        print('Scissors vs Scissors \nTIE GAME!')

#Both Choose Rock, Paper or Scissors. Computer choice uses a random integer declaration
compChoice = random.randint(1, 3)
userChoice = isValidEntry()

computer_throw(compChoice)
time.sleep(2)
versus(compChoice, userChoice)
reply = input('Play Again? ')

#Replay Loop
while reply == 'yes' or reply == 'y':
    compChoice = random.randint(1, 3)
    userChoice = isValidEntry()

    computer_throw(compChoice)
    time.sleep(2) #DRAMATIC EFFECT
    versus(compChoice, userChoice)
    reply = input('Play Again? \n')
