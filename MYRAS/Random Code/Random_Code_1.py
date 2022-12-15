from random import randrange

#Variable for my input decision
my_decision= str(input("Please choose 1 for Rock, 2 for Papper, and 3 for Scissors : "))

#Variable for computer's random choice
decision_computer= randrange(1,4)

#Game Logic
if my_decision == 1:
    if decision_computer == 1:
        print("Draw")
    elif decision_computer == 2:
        print("Loose!")
    else:
        print("Win!")
elif my_decision == 2:
    if decision_computer == 1:
        print("Win!")
    elif decision_computer == 2:
        print("Draw!")
    else:
        print("Loose!")
else:
    if decision_computer == 1:
        print("Loose!")
    elif decision_computer == 2:
        print("Win!")
    else:
        print("Draw!")