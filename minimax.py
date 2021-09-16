from main import *

score = {'x': 10, 'o': -10, 'tie': 0}

def bestMove():
    global best_move
    best_score = -100
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'):
                board[i][j] = ai
                score = minimax(board)
                board[i][j] = ''
                if(score>best_score):
                    best_score = score
                    best_move = [i,j]
    board[best_move[i]][best_move[j]] = ai
    current_player = human

def minimax(board):
    return 1