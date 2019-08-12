# L2 Q5: play rock-paper-scissor - Beat the King
# You need to win the king three times in a row in order to throw him away from his throne
# Carefully think about where a loop should be place
# Suggested Logic:
#
# Repeat the following until you really win
#        Challenge the king three times, in each challenge
#               pick a choice for the King and a choice for the player
#               Repeat this if it is draw
#                      pick a choice for the King and a choice for the player
#               if fail the challenge, break from this loop
#        




# Import necessary modules
from random import randint

print('Welcome to the rock-paper-scissor game!\nYou are going to play against a minion!')

# ascii art from https://www.asciiart.eu/people/body-parts/hand-gestures
print("Please input your choice")
print("""
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
""") # 1 for rock; 2 for paper; 3 for scissor

# step1: get player's choice, save it in variable p_choice
p = int(input())

# step2: generate a random choice for minion, save it in variable m_choice
m = randint(1,3)



# status is used for the win/lose/draw of the game
# status = 1 means player wins; status = 2 means minion wins; status = 3 means draw;
# status = 4 means user gives invalid input, e.g. player inputs -1 or 4
#status = 0 # initialized as 0
# step 3: given choices from player and minion, decide the game status









# step4: display the minion's choice
if p == 3:
    if m == 1:
        print("Minion chooses rock!")
        print("minion wins")
    elif m == 2:
        print("Minion chooses paper!")
        print("minion lose")
    elif m == 3:
        print("Minion chooses scissor!")
        print("minion tie")

elif p == 2:
    if m == 1:
        print("Minion chooses rock!")
        print("minion lose")
    elif m == 2:
        print("Minion chooses paper!")
        print("minion tie")
    elif m == 3:
        print("Minion chooses scissor!")
        print("minion wins")

elif p == 1:
    if m == 1:
        print("Minion chooses rock!")
        print("minion tie")
    elif m == 2:
        print("Minion chooses paper!")
        print("minion wins")
    elif m == 3:
        print("Minion chooses scissor!")
        print("minion lose")
else:
    print("please enter the correct no.")
    print("(1 for rock; 2 for paper; 3 for scissor)")
