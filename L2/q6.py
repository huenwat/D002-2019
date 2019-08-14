#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
from random import randint
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
n = randint(1,100)
#print ("shhh, Dave hides %s bananas" % n)
# define a flag for found/not found and counter on how many trials
found = False
count = 0
#Step 4: Give three chances to the players 
while(count<3):
    m = int(input("please enter a number:\n"))
    count = count+1
    if m == n:
        found = True
        break
    elif m<n and m >= 1:
        print("too small,you have %d times left." %(3-count))
       # m = int(input("please enter again:\n"))
        #continue
    elif m>n and  m<=100:
        print("too big,you have %d times left." %(3-count))
       # m = int(input("please enter again:\n"))
       # continue
    else:
        print("please enter a correct number(1-100)")
        count = count - 1
       # continue
#Step 5: Display a message
if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
else:
        print ("shhh, Dave hides %s bananas" % n)
        print("You failed to find the number of bananas Dave hid! Try again next")
