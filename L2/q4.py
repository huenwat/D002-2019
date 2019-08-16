a = int(1)
b = int(1)
c = int(1)
d = int(1)
m = int(1)
t = int(input("total number:\n")) + 1
for a in range(0,t):
    #print(a)
    m = (a*b) + (b*c) + (c*d)
    if a*b+b*c+c*d > m and a+b+c+d==t:
        m = (a*b) + (b*c) + (c*d)
    for b in range(0,t-a):
        #print(b)
        for c in range(0,t-a-b):
         #   print(c)
            print(a,b,c,d,m)
            d = t-a-b-c
            if a*b+b*c+c*d > m and a+b+c+d==t-1:
                m = (a*b) + (b*c) + (c*d)
print(a,b,c,d,m)





    
##13 14 16 17
