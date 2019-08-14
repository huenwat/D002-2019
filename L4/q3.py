def factors(n):
    result = []
    for x in range(1,n +1):
        if n % x == 0:
            result.append(x)
            #print("%d divides %d" % (x,n))
    return(result)
a=int(input("positive no.:"))
print(factors(a))
