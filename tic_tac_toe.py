# This function updates the board
def printBoard(xState, zState):
    one = 'X' if xState[0] else ('O' if zState[0] else 0)
    two = 'X' if xState[1] else ('O' if zState[1] else 1)
    three = 'X' if xState[2] else ('O' if zState[2] else 2)
    four = 'X' if xState[3] else ('O' if zState[3] else 3)
    five = 'X' if xState[4] else ('O' if zState[4] else 4)
    six = 'X' if xState[5] else ('O' if zState[5] else 5)
    seven = 'X' if xState[6] else ('O' if zState[6] else 6)
    eight = 'X' if xState[7] else ('O' if zState[7] else 7)
    nine = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f" {one} | {two} | {three} ")
    print(f"---|---|---")
    print(f" {four} | {five} | {six} ")
    print(f"---|---|---")
    print(f" {seven} | {eight} | {nine} ")
    
# Check Winnings
def checkWin(xState,zState):
    Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in Wins:
        if xState[win[0]] == xState[win[1]] == xState[win[2]] == 1:
            print("X Wins")
            return 1
        if zState[win[0]] == zState[win[1]] == zState[win[2]] == 1:
            print("O Wins")
            return 0
        
    return -1
    
# Invalid selection
def invalidSelection():
    while True:
        value = int(input("Confirm the position: "))
        # checkSameValue(xState,zState)
        if value < 0 or value > 8:
            print("Invalid Selection")
        else:
            return value
        
#Function to check whether same value is now selected
def checkSameValue(xState,zState):
    if xState[value] == 1 or zState[value] == 1:
        print("Invalid Selection")
        invalidSelection()
    else:
        return False

if __name__ == "__main__":
    xState =[0,0,0,0,0,0,0,0,0]
    zState =[0,0,0,0,0,0,0,0,0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while(True):
        printBoard(xState, zState)
        if(turn ==1 ):
            print("X's Chance")
            value = int(input("Enter the position: "))
            invalidSelection()
            checkSameValue(xState,zState)
            xState[value] = 1
            
        else:
            print("O's Chance")
            value = int(input("Enter the position:"))
            invalidSelection()
            checkSameValue(xState,zState)
            zState[value] = 1
            
        cwin = checkWin(xState,zState)
        if(cwin != -1):
            print("Match Over")
            break
        
        turn = 1- turn
        # break
    
    