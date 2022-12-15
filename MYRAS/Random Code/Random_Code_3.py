from random import randrange
#done
#Variable for my input decision
dec_me= int(input("Please choose 1 for Rock, 2 for Papper, and 3 for Scissors : "))

#Variable for computer's random choice
dec_comp= randrange(1,4)
w = "computer choose"
x = " Rock "
y = " Papper "
z = " Scissors "
draw = "and it's Draw!"
loose = "and You Loose!"
win = "and You Win!"
#Game Logic
if dec_me == 1:
    if dec_comp == 1:
        print(w + x + draw)
    elif dec_comp == 2:
        print(w + y + loose)
    else:
        print(w + z + win)
elif dec_me == 2:
    if dec_comp == 1:
        print(w + x + win)
    elif dec_comp == 2:
        print(w + y + draw)
    else:
        print(w + z + loose)
else:
    if dec_comp == 1:
        print(w + x + loose)
    elif dec_comp == 2:
        print(w + y + win)
    else:
        print(w + z + draw)