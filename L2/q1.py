from math import *
n = int(input("please input a positive integer bigger than 2\n"))
x = int(2)
if n > 2:
    while(x <= sqrt(n)): 
        if(n % x == 0):
            print("it's not a prime number",x,n/x)
            break
        else:
            x = x + 1
            
    if( x > sqrt(n)):
        print("it's a prime number")

else:
    print("it's not a positive integer bigger than 2")
