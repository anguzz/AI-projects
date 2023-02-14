"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCTR = 0
    oCTR = 0

    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if board[x][y] == X:
                xCTR += 1
            elif board[x][y] == O:
                oCTR += 1

    if xCTR > oCTR:
        return O
    else:
        return X


def actions(board):
    moves = set() # set of all seen possible moves available

    #loop through board and check if that tile is empty and add it to possible moves
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if board[x][y] == EMPTY:
                moves.add((x, y))
    return moves


def result(board, action):
 #make a copy of the board to modify and check it instead of original
    ans = copy.deepcopy(board)
    ans[action[0]][action[1]] = player(board)
    return ans


def winner(board):
     #check every single possible win condition(rows/cols/diagnols) and tie condition
     # since its only a 3x3 board
    
    #rows
    if(board[0][0] is not None and board[0][0] == board[0][1] and board[0][1] == board[0][2]):
        return board[0][0]
    elif(board[1][0] is not None and board[1][0] == board[1][1] and board[1][1] == board[1][2]):
        return board[1][0]
    elif(board[2][0] is not None and board[2][0] == board[2][1] and board[2][1] == board[2][2]):
        return board[2][0]

    #cols
    elif(board[0][0] is not None and board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        return board[0][0]
    elif(board[0][1] is not None and board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        return board[0][1]
    elif(board[0][2] is not None and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        return board[0][2]

    #diag
    elif(board[0][0] is not None and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]
    elif(board[0][2] is not None and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]   
    #tie condition 
    else:
        return None



def terminal(board):
    #check conditions to continue game state
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False



def score(board):
    #long as game state continues we check for winners
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

            
def checkMax(board):
    if terminal(board):
        return score(board), None
    smallest = float('-inf')
    move = None
    for action in actions(board):
        a, act = checkMin(result(board, action))
        if a > smallest:
            smallest = a
            move = action
            if smallest == 1:
                return smallest, move
    return smallest, move



def checkMin(board):
    if terminal(board):
        return score(board), None
    largest = float('inf')
    move = None
    for action in actions(board):
        a, act = checkMax(result(board, action))
        if a < largest:
            largest = a
            move = action
            if largest == -1:
                return largest, move
    return largest, move
    

def minimax(board):
    #check for best move using helper functions
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v, move = checkMax(board)
            return move
        else:
            v, move = checkMin(board)
            return move


