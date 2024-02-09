print("TIC-TAC-TOE Game")
print("Instruction to play the game:-")
print("1. Player need to select one of the signs from 'x' or 'o' and the other player gets automatically assigned the other sign")
print("2. First player to fill the board horizontally, vertically or diagonally with the smae sign wins the game")

Winner= None
Player="x"
gamerunning=True

board =[" ", " ", " ",                                       #board with empty strings created to later insert the value
        " ", " ", " ",
        " ", " ", " "]


def showboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def inputvalue(board):                                      # taking value from user
    i=int(input("Enter a no. 1-9:- "))
    if i>=1 and i<=9 and board[i-1]==" ":
        board[i-1]=Player
    else:
        print('The spot is already filled')

def switchplayer():
    global Player
    if Player=="x":
        Player="o"
    else:
        Player="x"

def check_horizontal(board):                                 
    global Winner
    if board[0]==board[1]==board[2] and board[1]!=" ":                        # for horizontal
        Winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!=" ":                      # for horizontal
        Winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!=" ":                      # for horizontal
        Winner=board[6]
        return True
    
def check_vertical(board):
    global Winner
    if board[0]== board[3] == board[6] and board[0]!=" ":                      # for vertical
        Winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!=" ":                      # for vertical
        Winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!=" ":                      # for vertical
        Winner=board[2]
        return True
    
def check_diagonal(board):
    global Winner
    if (board[0] == board[4] == board[8] )and board[0]!=" ":                      # for diagonal
        Winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!=" ":                      # for diagonal
        Winner=board[2]
        return True

def check_tie(board):
    global gamerunning
    if " " not in board:
        showboard(board)
        print("Its a tie")
        gamerunning = False
    
def check_all(board):
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        showboard(board)
        print(f"The winner is {Winner}")
        exit()
    gamerunning = False

while gamerunning:
    showboard(board)
    inputvalue(board)
    check_all(board)
    check_tie(board)
    switchplayer()

