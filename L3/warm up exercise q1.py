# D002 Lesson 3
# Q1:  Warm up exercise

# a) Go Dutch
from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
print("So Kevin is going to paid $%d." % (ceil(bill/100)*100))   # replace with your code
print("The cafe is giving %d to Kevin." % (ceil(bill/100)*100-bill))  # replace with your code
print("Each one should give %f to Kevin." % (bill/(people)-1)) # replace with your code

# b) Clap at Seven 
# The purpose of the following program is to print the number from 1 to 100,
# in order. However, when the number is a multiple of 7 (e.g. 7/14/21) or when
# the last digit of the number is 7 (e.g. 17/27/37), it print a X instead

n = 1
while  n<= 100:
    if n % 7==0 or n% 10 ==7:   # replace with your code
        print('X', ' ')
    else:
        print(n,' ')    
    n = n + 1
print("\nGame Over.")

# c) How long it takes?
# In a Chinese board game the player can start its game only when he can
# get a 6 in rolling a dice. Please do an experiment to test your luck today
# and see how long it takes to get a dice

from random import randint

#code for rolling a dice
from random import randint 
number = randint(1,6)
print("I got a %d" % number)
count = 1
while number != 6 : # replace with your code
    # Write some more code
    print("I got a %d" % number)
    number = randint(1,6)
    count = count + 1

print("Oh, it takes me %d times to get a 6!!!" % count)

# d) How long it takes, in general?
# Repeat the experiment in part c for 100 times and see what is the average 
# value of the count would be. This is challenging, isn't it?# D002 Lesson 3
# Q1:  Warm up exercise

from random import randint 
from math import *
number = randint(1,6)
print("I got a %d" % number)
count = 1
t = 1
while(t<100):
    while number != 6 : # replace with your code
        # Write some more code
        #print("I got a %d" % number)
        number = randint(1,6)
        count = count + 1
        
        
    print(t)
    t = t+1
    #print("Oh, it takes me %d times to get a 6!!!" % count)
    number=0
print(t)
print("average time to get '6':%.2f "%(count/100))
