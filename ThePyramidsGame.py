import random

global matrix
global col 
global rows 
global l
global BlueCellOnBorderFlag
global PinkCellConditionsFlag
global YellowCellConditionFlag

def BlueCellOnBorder():
    global BlueCellOnBorderFlag
    mid = int(col/2)
    for i in range(0,rows-1):
        if(matrix[i][mid+i] == 'B'):
            calculateRandom(i,mid+i,'B')
            BlueCellOnBorderFlag = True
        if(matrix[i][mid-i] == 'B'):
            calculateRandom(i,mid-i,'B')   
            BlueCellOnBorderFlag = True
    i+=1
    for j in range(0,col):
        if(matrix[i][j] == 'B'):
            calculateRandom(i,j,'B')
            BlueCellOnBorderFlag = True



def initialize():
    k = 0
    count=0
    count1=0
    row_id = 0
    col_id = 0
    for i in range(1, rows+1):
        for _ in range(1, (rows-i)+1):
            col_id+=1
            count+=1

        while k!=((2*i)-1):
            if count<=rows-1:
                count+=1
            else:    
                count1+=1
            calculateRandom(row_id,col_id,None)
            k += 1
            col_id+=1

        count1 = count = k = col_id = 0  
        row_id +=1

def printMatrix():
    for i in range(0, rows):
        for j in range(0, col):
            if matrix[i][j] == 0:
                print("  ", end="")
            else:
                print( matrix[i][j], end=" ")
        print()
    print()
print()


def checkIfValidIndex(i,j):
    if (i<0 or i>=rows) or (j<0 or j>=col) or ( matrix[i][j] == 0):
        return False
    return True

def calculateRandom(i,j,color):
    rand = random.choice(l) 
    while(rand == color and color != None):
         rand = random.choice(l) 
    matrix[i][j] = rand


def PinkCellConditions():
    global PinkCellConditionsFlag 
    while True:
        localFlag = False 
        for i in range(0, rows):
            for j in range(0, col):
                if(matrix[i][j] == 'B'):
                    #look down
                    if(checkIfValidIndex(i+1,j) and matrix[i+1][j]=='P'):
                        calculateRandom(i+1,j,'P')
                        PinkCellConditionsFlag = True
                        localFlag = True 
                    #look up
                    if(checkIfValidIndex(i-1,j) and matrix[i-1][j]=='P'):
                        calculateRandom(i-1,j,'P')
                        PinkCellConditionsFlag = True
                        localFlag = True 
                    #look left
                    if(checkIfValidIndex(i,j-1) and matrix[i][j-1]=='P'):
                        calculateRandom(i,j-1,'P')
                        PinkCellConditionsFlag = True
                        localFlag = True 
                    #look right
                    if(checkIfValidIndex(i,j+1) and matrix[i][j+1]=='P'):
                        calculateRandom(i,j+1,'P')
                        PinkCellConditionsFlag = True
                        localFlag = True   
        if localFlag == False:
            break

def YellowCounter(i):
    yellowCounter =0
    for k in range(0, col):
        if(matrix[i][k] == 'Y'):
            yellowCounter+=1
    return yellowCounter


def YellowCellCondition():
    global YellowCellConditionFlag
    for i in range(2, rows):
        yellowCounter = YellowCounter(i)
        while(yellowCounter>4):
            YellowCellConditionFlag = True
            for k in range(0, col):
                if(matrix[i][k] != 0):
                    calculateRandom(i,k,None)
                    yellowCounter = YellowCounter(i)
        
                   


col = 9
rows = 5
l = ['B','Y','P']
matrix = [[0 for x in range(col)] for y in range(rows)] 

'''
for i in range(0, rows):
    for j in range(0, col):
        print( matrix[i][j], end=" ")
    print()
print()
'''
#Each cell in the pyramid is randomly initialized to one of the colors
initialize() 
print('initialize')
printMatrix()

counter =1

while True:

    BlueCellOnBorderFlag = False
    PinkCellConditionsFlag = False
    YellowCellConditionFlag = False

    #The blue cell cannot be within the boundaries of the pyramid
    BlueCellOnBorder()
    if(BlueCellOnBorderFlag == True):
        print('Blue rule')
        printMatrix()

    #A pink cell cannot appear to the right/left/above/below a blue cell
    PinkCellConditions()
    if(PinkCellConditionsFlag == True):
        print('Pink rule')
        printMatrix()

    #If there are more than 4 yellow cells in a row, grill the whole row again
    YellowCellCondition()
    if(YellowCellConditionFlag == True):
        print('Yellow rule')
        printMatrix()


    counter+=1

    if BlueCellOnBorderFlag == False and PinkCellConditionsFlag == False and YellowCellConditionFlag == False:
        print('This is number of iterations until a legal pyramid came out',counter)
        printMatrix()
        break



