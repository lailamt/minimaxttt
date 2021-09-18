import time

def printBoard(board):
    print('{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n'.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))

def spaceIsFree(position):
    if board[position] == '_':
        return True
    else:
        return False

def insertOnBoard(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkTie()):
            print("Tie!")
            exit()
        if findWinner() == 'X':
            print("AI wins!")
            exit()
        elif findWinner() == 'O':
            print("You win!")
            exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

def insertLetter(letter, position):
    if(letter == ai):
        insertOnBoard(letter, position)
    if(letter == human):
        insertOnBoard(letter, position)    

def compare(a, b, c):
    return a == b and a == c and a != '_'

def findWinner():
    #Check horizontal
    if(compare(board[0], board[1], board[2])):
        return board[0] 
    if(compare(board[3], board[4], board[5])):
        return board[3]
    if(compare(board[6], board[7], board[8])):
        return board[6]
    #Check vertical
    if(compare(board[0], board[3], board[6])):
        return board[0]
    if(compare(board[1], board[4], board[7])):
        return board[1]
    if(compare(board[2], board[5], board[8])):
        return board[2]
    #Check diagonal
    if(compare(board[0], board[4], board[8])):
        return board[0]
    if(compare(board[2], board[4], board[6])):
        return board[2]

def compareMinimax(a, b, c, d):
    return a == b and a == c and a == d

def checkWinnerInLevelMinimax(who):
    #Check horizontal
    if(compareMinimax(board[0], board[1], board[2], who)):
        return who
    if(compareMinimax(board[3], board[4], board[5], who)):
        return who
    if(compareMinimax(board[6], board[7], board[8], who)):
        return who
    #Check vertical
    if(compareMinimax(board[0], board[3], board[6], who)):
        return who
    if(compareMinimax(board[1], board[4], board[7], who)):
        return who
    if(compareMinimax(board[2], board[5], board[8], who)):
        return who
    #Check diagonal
    if(compareMinimax(board[0], board[4], board[8], who)):
        return who
    if(compareMinimax(board[2], board[4], board[6], who)):
        return who

def checkTie():
    for key in board.keys():
        if (board[key] == '_'):
            return False
    return True

def playerMove():
    print('Human turn!')
    print("Positions:\n0, 1, 2\n3, 4, 5\n6, 7, 8\n")
    position = int(input("Enter the position for 'O':  "))
    insertLetter(human, position)
    return

def aiMoveMinimax():
    print('AI turn!')
    bestScore = -100
    bestMove = 0
    start = time.time()
    for key in board.keys():
        if (board[key] == '_'):
            board[key] = ai
            score = minimax(board, 0, False)
            board[key] = '_'
            if (score > bestScore):
                bestScore = score
                bestMove = key
    end = time.time()
    print('AI took {}s to make a decision'.format(round(end - start, 5)))
    insertLetter(ai, bestMove)
    return

def minimax(board, depth, isMaximizing):
    if (checkWinnerInLevelMinimax(ai) == ai):
        return 10
    elif (checkWinnerInLevelMinimax(human) == human):
        return -10
    elif (checkTie()):
        return 0
    if (isMaximizing):
        bestScore = -100
        for key in board.keys():
            if (board[key] == '_'):
                board[key] = ai
                score = minimax(board, depth + 1, False)
                board[key] = '_'
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 100
        for key in board.keys():
            if (board[key] == '_'):
                board[key] = human
                score = minimax(board, depth + 1, True)
                board[key] = '_'
                if (score < bestScore):
                    bestScore = score
        return bestScore

def aiMoveWithPruning():
    print('AI turn!')
    bestScore = -100
    bestMove = 0
    start = time.time()
    for key in board.keys():
        if (board[key] == '_'):
            board[key] = ai
            score = minimaxWithPruning(board, 8, False, -100, 100)
            board[key] = '_'
            if (score > bestScore):
                bestScore = score
                bestMove = key
    end = time.time()
    print('AI took {}s to make a decision'.format(round(end - start, 5)))
    insertLetter(ai, bestMove)
    return

def minimaxWithPruning(board, depth, isMaximizing, alpha, beta):
    if (depth == 0 or findWinner() != '_'):
        if (checkWinnerInLevelMinimax(ai) == ai):
            return 10
        elif (checkWinnerInLevelMinimax(human) == human):
            return -10
        elif (checkTie()):
            return 0
    if (isMaximizing):
        bestScore = -100
        for key in board.keys():
            if (board[key] == '_'):
                board[key] = ai
                score = minimaxWithPruning(board, depth - 1, False, alpha, beta)
                board[key] = '_'
                if (score >= bestScore):
                    bestScore = score
                    #bestMove = key
                alpha = max(alpha, score)
                if(beta <= alpha):
                    break 
        return bestScore
    else:
        bestScore = 100
        for key in board.keys():
            if (board[key] == '_'):
                board[key] = human
                score = minimaxWithPruning(board, depth - 1, True, alpha, beta)
                board[key] = '_'
                if (score < bestScore):
                    bestScore = score
                    #bestMove = key
                beta = min(beta, score)
                if (beta <= alpha):
                    break
        return bestScore

board = {0: '_', 1: '_', 2: '_',
         3: '_', 4: '_', 5: '_',
         6: '_', 7: '_', 8: '_'}

printBoard(board)
print('Human starts the game!!\n')
human = 'O'
ai = 'X'
alpha = -100
beta = 100

try:
    print('Choose the algorithm:\n 1 - Minimax\n 2 - Minimax with pruning')
    algorithm = input('Input: ')
    if(int(algorithm) == 1):
        while not findWinner():
            playerMove()
            aiMoveMinimax()
    elif(int(algorithm) == 2):
        while not findWinner():
            playerMove()
            aiMoveWithPruning()
    else:
        print('Invalid input!')

except:
    pass
