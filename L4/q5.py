def printer(secret,o):
    i = 0
    while( i < len(secret)):
        if i in o:
            print(secret[i])
        else:
            print("_")
        i = i+1
       
        #print()

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
