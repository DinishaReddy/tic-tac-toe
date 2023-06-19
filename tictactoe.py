import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentplayer = 'X'
winner = None
tie = 0

def checkboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("---------")
    print(board[3] + '|' + board[4] + '|' + board[5])
    print("---------")
    print(board[6] + '|' + board[7] + '|' + board[8])

def playerinput(board):
    inpu = int(input("enter the position:"))
    if inpu >= 1 and inpu <= 9 and board[inpu-1] == '-':
        board[inpu-1] = currentplayer
    else:
        print('player is already in the spot')

def checkrow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
    if board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[4]
    if board[6] == board[7] == board[8] and board[7] != '-':
        winner = board[7]

def checkcolumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[4]
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[8]

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[4]

def check_tie():
    global tie
    if '-' not in board and winner is None:
        print('it is a tie')
        tie = 1

def switchplayer():
    global currentplayer
    if currentplayer == 'X':
        currentplayer = 'O'
    else:
        currentplayer = 'X'

def checkwin():
    checkcolumn(board)
    checkrow(board)
    checkdiagonal(board)
    if winner:
        print(f"the winner is {winner}")

def computerplayer(board):
    if currentplayer == 'O':
        position = random.randint(0, 8)
        if board[position] == '-':
            board[position] = currentplayer
            switchplayer()

while winner is None and tie == 0:
    checkboard(board)
    playerinput(board)
    checkwin()
    check_tie()
    switchplayer()
    computerplayer(board)
    checkwin()
    check_tie()
