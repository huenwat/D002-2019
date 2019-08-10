from math import *
a = int(1)
b = int(1)
c = int(1)
d = int(1)
x = int(a + b + c + d)
y = int(a*b + b*c + c*d)
while (x < 60 ):
   a = 1
   while((b + c + d)<(60 - a)):
       while((c + d)<(60 - a - b)):
           while(d<(60- a - b- c)):
                print("a = %d\tb = %d\tc = %d\td = %d" % (a,b,c,d))
                print("\n")
                d = d + 1              
           c = c + 1
       b = b + 1
   a = a + 1
   if y > m:
        m = n
   else:
        m = a




    
##13 14 16 17
