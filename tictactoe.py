"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None
board_size = 3 #size of the board


def initial_state():
    """
    Returns starting state of the board.
    """
    #creates size x size array of EMPTY elements
    return [[EMPTY for _ in range(board_size)] for _ in range(board_size)]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #if number of X in the board greater than the number of O, its turn for O
    if ( sum(row.count(X) for row in board) > sum(row.count(O) for row in board) ):
        return O
    #else its turn for X
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #the set of actions possible for the game is all EMPTY cells in the board
    return {(i,j) for i in range(board_size) for j in range(board_size) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if ( board[i][j] != EMPTY):
        raise ValueError("Cell already occupied")
    
    current_player = player(board)
    board[i][j] = current_player
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check rows 
    for i in range(board_size):
        for j in range (board_size -2):
            if ( board[i][j] != EMPTY):
                if (board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2]):
                    return board[i][j]
        
    #check columns
    for i in range(board_size - 2):
        for j in range (board_size):
            if ( board[i][j] != EMPTY):
                if (board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j]):
                    return board[i][j]

    #check diagonally
    for i in range(board_size -2):
        for j in range (board_size -2):
            if (board[i][j] != EMPTY):
                if (board[i][j] == board[i+1][j+1] and board[i][j] == board[i+2][j+2]):
                    return board[i][j]
            if (board[i+2][j] != EMPTY):
                if (board[i+2][j] == board[i+1][j+1] and board[i+2][j] == board[i][j+2]):
                    return board[i+2][j]
    #if there is no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if there is a winner or all cells are occupied the game is ended.
    return winner(board) is not None or all (cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if ( win == X):
        return 1
    if ( win == O):
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): #if board is finished
        return None
    
    current_player = player(board)

    if ( current_player == X): #if player is X tries to maximize the utility
        _, best_action = max_value(board)
    else: #if player is O tries to minimize the utility
        _, best_action = min_value(board)
    
    return best_action #return the best action possible

def max_value(board): #maximizer
    if terminal(board): #if game is finished there is no action can be taken
        return utility(board), None
    
    value = -math.inf
    best_action = None
    for action in actions(board): #for each available action in the board
        min_val, _  = min_value( result(board, action)) #try the next action
        if (min_val > value or (min_val == value and random.random() < 0.5)):
            value = min_val
            best_action = action #if its the best action, update
        i,j = action
        board[i][j] = EMPTY

    return value, best_action #return best action

def min_value(board): #minimizer
    if terminal(board): #if game is finished there is no action can be taken
        return utility(board), None
    
    value = math.inf
    best_action = None
    for action in actions(board): #for each available action in the board
        max_val, _  = max_value( result(board, action)) #try the next action
        if (max_val < value or (max_val == value and random.random() < 0.5)):
            value = max_val
            best_action = action #if its the best action, update
        i,j = action
        board[i][j] = EMPTY

    return value, best_action #return best action
