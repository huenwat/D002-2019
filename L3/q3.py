list = []
x = ["a" , "e" , "i" , "o" , "u"]
for i in range(0,10):
    word = input("enter your word please:")
    if i != 10:
        print("next,")
    list.append(word)
for i in list:
    for j in x:
        if (j==i[0]):
            print(i)
