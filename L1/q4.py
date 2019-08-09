from math import *
y = input("which year?\n")
if int(y) % 400 ==0:
    print("it's a leap year")
elif int(y) % 100 == 0:
    print("it's not a leap year")
elif int(y) % 4 == 0 :
    print("it's a leap year") 
else :
    print("it's not a leap year")
 
