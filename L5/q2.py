# Tic-Tac-Toe

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 3):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
            
    return False

def check_row(cells):
    for i in range(0, 3):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
            
    return False

def check_diagonal(cells):
    for i in range(0, 3):
        if cells[i][i] == cells[i][i] == cells[i][i] != ' ':
            return True
        return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False

count = 1
    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

printcell(cells)



while True:
    check(cells)
    col = int(input("Please enter column\t"))-1
    row = int(input("Please enter row\t"))-1
    if row<3 and col<3 and cells[row][col] == ' ' and count == 1 :
        cells[row][col] = 'X'
        count = 0
        
        printcell(cells)
        if check_col(cells) or check_row(cells): 
            break
        
    elif row<3 and col<3 and cells[row][col] == ' ' and count == 0 :
        cells[row][col] = 'O'
        count = 1
        printcell(cells)
        if check_col(cells) or check_row(cells): 
            break
    else:
        print("It is taken already")
    
print("game over")   
