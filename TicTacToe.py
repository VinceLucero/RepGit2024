import numpy as np

board = np.full(9,2)
turn = 1
start = 1
win = False

#   AVELLANEDA TREJO BRANDON

# ------------------------------------------ board -----------------------------------------------

def print_board(board):
    board_c = [' ' if valor == 2 else 'X' if valor == 3 else 'O' for valor in board]

    print(" {} | {} | {} ".format(board_c[0], board_c[1], board_c[2]))
    print("-----------")
    print(" {} | {} | {} ".format(board_c[3], board_c[4], board_c[5]))
    print("-----------")
    print(" {} | {} | {} ".format(board_c[6], board_c[7], board_c[8]))

# ------------------------------------------ make2 -----------------------------------------------

def make2():
    if board[4] == 2:
        return 5 
    for i in range(2,10,2):
        if board[i-1] == 2:
            return i
        
    return -1
  
# ------------------------------------------ Go ----------------------------------------------- 
  
def go(n):
    global turn
    board[n-1] = 5 if turn % 2 == 0 else 3 
    turn += 1
    print_board(board)
 
# ------------------------------------------ posswin -----------------------------------------------

# check if the product eq the cant to win             
def prod(n_start, n_end, step, prodWin):
    product, index =  1,  0
    for i in range(n_start, n_end, step):
        content = board[i-1]
        product *= content
        
        if content ==  2:
            index = i
        if product == prodWin:
            return index
    return -1

# Check rows
def prodRow(n_row, prodWin):
    k = n_row *  3 -  2
    l = n_row *  3 +  1
    return prod(k, l,  1, prodWin)

# Check columns
def prodColumn(n_col, prodWin):
    return prod(n_col,  10,  3, prodWin)

# Check diagonals
def prodDiag1(prodWin):
    return prod(1,  10,  4, prodWin)

def prodDiag2(prodWin):
    return prod(3,  9,  2, prodWin)
 
#posswin(p)  returns -1 if player p can't win on his next move
#otherwise it returns the winning position
 
def posswin(p):      
    
    prodWin = 18 if p else 50             # True: x   False: O
      
    for j in range(1,4):
        poss_row = prodRow(j, prodWin)
        if poss_row != -1:
            return poss_row 
        poss_column = prodColumn(j,prodWin)
        if poss_column != -1:
            return poss_column
    
    poss_diag1 = prodDiag1(prodWin)
    poss_diag2 = prodDiag2(prodWin)
    
    if poss_diag1 != -1:
        return poss_diag1
    
    if poss_diag2 != -1:
        return poss_diag2
            
    return -1


# ------------------------------------------ Empty spaces checking -----------------------------

def empty_on_board():
    k = 0
    for i in board:        
        if i == 2:
            return k+1
        k +=1
    return -1     #non-sense

# ----------------------------------------- Try to Win ------------------------------------------

#tries to win, if not, tries to cover the win:  posswin(symbol) ---> poswin(not symbol)

def tryWin(symbol):
    #True == x   False == o
    sym_on_bool = np.array([symbol,not symbol])
    performed = False
       
    for i in sym_on_bool:       
        place = posswin(i)        
        if i == symbol and place != -1:       # win
            go(place)
            print('Computer wins')
            global win 
            win = True 
            return True   # Returns True if the function found a move
        else:
            if place != -1:              # covers the win
                go(place)
                return True   
               
    return False  # Returns false if it couldn't find a good move


# ------------------------------------------ Player ------------------------------------------

def player(symbol):
    #check if is empty
    empty = True
    while empty:
        pos = int(input('where you want to place: '))
        if board[pos-1] == 2:
            empty = False    #then it's ocuppied
            if posswin(symbol) == pos:
                global win 
                win = True
                print('Player wins')
            go(pos)
            
        else:
            print('occupied')


# ------------------------------------------ Computer ------------------------------------------
def computer(symbol):        
    if turn ==  1:
        go(1)
        return
    if turn ==  2:
        go(5 if board[4] == 2 else 1)
        return
    if turn == 3:
        go(9 if board[8] == 2 else 3)
        return
    if turn == 4:
        if(tryWin(symbol) == False):
            go(make2())
        return
    if turn == 5:
        if(tryWin(symbol) == False): 
            go(7 if board[6] == 2 else 3)
        return
    if turn >= 6 and turn < 10:
        if(tryWin(symbol) == False):    #True
            goes = make2()
            go(goes if (turn == 6 and goes != -1) else empty_on_board())
        return
  
# ------------------------------------------ Game -----------------------------------------------
  
start = int(input('Wanna Start? Yes (1) no (2) '))
turnBool = True if start == 1 else False
symbol = True if start == 1 else False    
print_board(board)

while(not win):
    print('turn', turn)
    if(turnBool):
        print('your turn')
        player(symbol)
    else:
        print('my turn')
        computer(not symbol)

    turnBool = not turnBool  #turn 
  
    if turn >= 10 and win == False:
        print('DRAW')
        win = True       #it's a draw,  but 'True' stops the loop



