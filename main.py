import sys
sys.setrecursionlimit(10000)

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

score = {'x': 10, 'o': -10, 'tie': 0}

ai = 'x'
human = 'o'
current_player = human
winner = ''

def checkIfLinesHaveSamePlayer(a, b, c):
    res = (a == b and b == c and a != '')
    print(res)
    return res

def placesToFill():
    empty_places = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == ''):
                empty_places+=1
    return empty_places

def checkWinner():
    global winner
    #Check horizontal
    if(checkIfLinesHaveSamePlayer(board[0][0], board[0][1], board[0][2])):
        winner = board[0][0]
    if(checkIfLinesHaveSamePlayer(board[1][0], board[1][1], board[1][2])):
        winner = board[1][0]
    if(checkIfLinesHaveSamePlayer(board[2][0], board[2][1], board[2][2])):
        winner = board[2][0]

    #Check vertical
    if(checkIfLinesHaveSamePlayer(board[0][0], board[1][0], board[2][0])):
        winner = board[0][0]
    #Check horizontal
    if(checkIfLinesHaveSamePlayer(board[0][1], board[1][1], board[2][1])):
        winner = board[0][1]
    if(checkIfLinesHaveSamePlayer(board[0][2], board[1][2], board[2][2])):
        winner = board[0][2]

    empty_places = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == ''):
                empty_places+=1

    #Check if tie
    if(winner == '' and empty_places == 0):
        return 'tie'
    else:
        #print(winner)
        return winner

def drawPlay(x, y):
    global current_player
    if(current_player == human):
        x = x
        y = y
        if(board[x][y] == ''):
            board[x][y] = human
            current_player = ai
            bestMove()

def printBoard():
    for i in range(len(board)):
        print(board[i])

def bestMove():
    global current_player
    move = []
    best_score = -1000
    for i in range(3):
        for j in range(3):
            # Is the spot available?
            if(board[i][j] == ''):
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = ''
                if(score > best_score):
                    best_score = score
                    move.append(i)
                    move.append(j)
    print(move)
    board[move[0]][move[1]] = ai
    current_player = human

def minimax(board, depth, isMax):
    global score
    result = checkWinner()
    if(result != ''):
        return score[result]

    if (isMax):
        best_score = -1000
        for i in range(3):
            for j in range(3):
                # Is the spot available?
                if(board[i][j] == ''):
                    board[i][j] == ai
                    score = minimax(board, depth+1, False)
                    board[i][j] == ''
                    if(score > best_score):
                        best_score = score
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                # Is the spot available?
                if(board[i][j] == ''):
                    board[i][j] == human
                    score = minimax(board, depth+1, True)
                    board[i][j] == ''
                    if(score < best_score):
                        best_score = score
        return best_score

while(checkWinner() == ''):
    print('Digite as coordenadas para a jogada: ', end='')
    x, y = input().split(' ')
    drawPlay(int(x), int(y))
    printBoard()

bestMove()
result = checkWinner()

print('The winner is: {}!! \n Congrats!!'.format(result))
