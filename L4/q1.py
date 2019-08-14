# Q1

# a) Gotcha.
# You are a Pokemon trainer and you catch new monster everyday.
# A list, which is called "collection", stores all kinds of pokemon that you
# have collected so far. The list "collection" does not stores how many same kind of
# monster you have got. Each monster of the same kind will be stored once.

collection = ["Pikachu", "Bulbasaur", "Squirtle", "Nidoqueen"]
newly_caught = ["Bulbasaur", "Kakuna", "Arbok", "Jigglypuff"]

for i in newly_caught:
    for j in collection:
        if j == i : # your code here
            newly_caught.remove(i )# your code here
collection.append(newly_caught)
print(collection) # should print ['Pikachu', 'Bulbasaur', 'Squirtle', 'Nidoqueen', 'Kakuna', 'Arbok', 'Jigglypuff']



# b) Shaking the stock market.
# You are given a list that stores the Hangseng Index
# of a period of time. Each number represents the HSI recorded at the end of a
# day. You want to find how many points it goes up and down in each day.
# Put those changes into another list.

hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []

a = 20000
for i in hsi:
    if i !=a:
        change.append(i-a)
        a = i
    else:
        change.append(0)
# your code here

print(change)  # should print [1000, 500, 625, -1110, 998, -2071, 4558]


# c) TV remote control
# Not sure how many of you are still watching TV. Assume we have a list of channels
# preset in your TV. If you press Up (U), it shows the next channel in the list.
# If you press Down (D), it shows the previous channel. If you press Off (O), the
# TV will explode and the program ends.

c = ["TVB", "CCTV", "VIU", "RTHK", "Netflix", "TBS", "KBS"]

c_c = 0
while True:
    U = int(1)
    D = int(2)
    O = int(3)
    print("You are now watching %s" % c[c_c])
    a = int(input("Please choose either U/D/O\n"))
    if a == 1:
        c_c = c_c + 1
    elif a == 2:
        c_c = c_c - 1
    elif a == 3:
        break
print("you turn off the TV")
    # may be some more code




### Expected Result
##You are now watching TVB
##Please choose either Up/Down/Off
##U
##You are now watching CCTV
##Please choose either Up/Down/Off
##U
##You are now watching VIU
##Please choose either Up/Down/Off
##U
##You are now watching RTHK
##Please choose either Up/Down/Off
##D
##You are now watching VIU
##Please choose either Up/Down/Off
##D
##You are now watching CCTV
##Please choose either Up/Down/Off
##U
##You are now watching VIU
##Please choose either Up/Down/Off
##D
##You are now watching CCTV
##Please choose either Up/Down/Off
##D
##You are now watching TVB
##Please choose either Up/Down/Off
##D
##You are now watching KBS
##Please choose either Up/Down/Off
##D
##You are now watching TBS
##Please choose either Up/Down/Off
##U
##You are now watching KBS
##Please choose either Up/Down/Off
##U
##You are now watching TVB
##Please choose either Up/Down/Off
##O
##>>>

        
