#from minimax import *

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

ai = 'x'
human = 'o'
current_player = human

def checkIfLinesHaveSamePlayer(a, b, c):
    return a == b and b == c and a != ''

def placesToFill():
    empty_places = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == ''):
                empty_places+=1
    return empty_places

def checkWinner():
    winner = ''
    #Check horizontal
    for pos in range(len(board)):
        if(checkIfLinesHaveSamePlayer(board[pos][0], board[pos][1], board[pos][2])):
            winner = board[pos][0]
    #Check vertical
    for pos in range(len(board)):
        if(checkIfLinesHaveSamePlayer(board[0][pos], board[1][pos], board[2][pos])):
            winner = board[0][pos]
    #Check horizontal
    if(checkIfLinesHaveSamePlayer(board[0][0], board[1][1], board[2][2])):
        winner = board[0][0]
    if(checkIfLinesHaveSamePlayer(board[2][0], board[1][1], board[0][2])):
        winner = board[2][0]

    #Check if tie
    if(winner == '' and placesToFill() == 0):
        return 'tie'
    else:
        return winner

def drawPlay(x, y):
    if(current_player == human):
        x = x-1
        y = y-1
        if(board[x][y] == ''):
            board[x][y] = human
            current_player = ai
            bestMove()

score = {'x': 10, 'o': -10, 'tie': 0}

def bestMove():
    move = []
    best_score = -1000
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'):
                board[i][j] = ai
                score = minimax(board)
                board[i][j] = ''
                if(score > best_score):
                    best_score = score
                    move.append([i,j])
    print(move)
    board[move[i]][move[j]] = ai
    current_player = human

def minimax(board):
    return 1
bestMove()
result = checkWinner()
print('The winner is: {}!! \n Congrats!!'.format(result))
