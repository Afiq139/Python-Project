from random import randrange
#Variable for my input decision
my_decision= str(input("Please choose 1 for Rock, 2 for Papper, and 3 for Scissors : "))
#Variable for computer's random choice
decision_computer= randrange(1,4)

#Game Logic
if my_decision == 1:  #First Decision is Rock
    print("You play Rock")
    if decision_computer == 1:
        print("Computer play Rock")
        print("Draw")        
    elif decision_computer == 2:
        print("Computer play Paper")
        print("You Lose!")
    else : print("Computer play Scissor")
    print("You Win!")
elif my_decision == 2: #Second Decision is Paper
    print("You play Paper")
    
    if decision_computer == 1:
        print("Computer play Rock")
        print("You Win!")
    elif decision_computer == 2:
        print("Computer play Paper")
        print("Draw!")
    else : print("Computer play Scissor")
    print("You Lose!")
else: #Third Decision is Scissor
    print("You play scissor")
    
    if decision_computer == 1:
        print("Computer play Rock")
        print("You Lose!")
    elif decision_computer == 2:
        print("Computer play Paper")
        print("You Win!")
    else :
        print("Computer play Scissor")
        print("Draw!")