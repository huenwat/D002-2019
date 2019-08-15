l=[]
for e in range(0,10):
    a=int(input("please enter a number:\t"))
    l.append(a)
m = 9999999999999999
p = l
print(l)
for i in l:
    for j in p:
        if (j-i)<m and (j-i)>0 and m==9999999999999999:
            m = (i-j)
        elif (i-j)<m and (i-j)>0 and m==9999999999999999:
            m = (i-j)
        else:
            m = m
print(m)
