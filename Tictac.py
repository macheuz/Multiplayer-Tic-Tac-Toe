import numpy as array


def createTable():
    table = array.full((3,3), ( '[ ]' ))
    return table

def verifyTablecoluns(table):
    cont = 0
    for x in range(0,3):
        contx=0
        contO = 0
        for i in range(0,3):
            if table[x][i] == '[x]':
                contx = contx+1
                if contx == 3:
                    print()
                    print("Player X wins")
                    return False
            elif table[x][i] == '[o]':
                contO = contO+1
                if contO == 3:
                    print()
                    print("Player O wins")
                    return False
    return True

                
def verifyTablelines(table):
    cont = 0
    for x in range(0,3):
        contx=0
        contO = 0
        for i in range(0,3):
            if table[i][x] == '[x]':
                contx = contx+1
                if contx == 3:
                    print()
                    print("Player X wins")
                    return False
            elif table[i][x] == '[o]':
                contO = contO+1
                if contO == 3:
                    print()
                    print("Player O wins")
                    return False
        return True
    
def verifyTableDiagonal(table):
    contx = 0
    conto = 0
    for x in range(0,3):
        if table[x][x] == '[x]':
            contx = contx+1
        if table[x][x]== '[o]':
            conto= conto+1
    if contx == 3:
        print()
        print("Player X wins")
        return False
    elif conto == 3:
        print()
        print("Player O wins")
        return False
    return True
    
def playWithX(table):
    line = int(input("Put the line you want to fill: "))-1
    columns = int(input("Put the column you want to fill: "))-1
    if table [line] [columns] == '[ ]':
        table[line] [columns] = '[x]'
    else:
        print("Invalid position, input an other position!")
        playWithX(table)



def playWithO(table):
    line = int(input("Put the line you want to fill: "))-1
    columns = int(input("Put the column you want to fill: "))-1
    if table [line] [columns] == '[ ]':
        table[line] [columns] = '[o]'
    else:
        print("Invalid position, input an other position!")
        playWithO(table)

    


table = createTable()
print(table[0][0])
print(table)
x=0
while(x<=9 and (verifyTablecoluns(table) == True and verifyTableDiagonal(table)== True and verifyTablelines(table)== True)):
    print("Player X:")
    print()
    playWithX(table)
    print(table)
    x=x+1
    if x == 9 or (verifyTablecoluns(table) == False or verifyTableDiagonal(table)== False or verifyTablelines(table)== False):
        break
    print('---'*30)
    print("Player O")
    playWithO(table)
    print(table)
    x= x+1
