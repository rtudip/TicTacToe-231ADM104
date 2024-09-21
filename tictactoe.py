"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
board_size = 4


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY for _ in range(board_size)] for _ in range(board_size)]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if ( sum(row.count(X) for row in board) > sum(row.count(O) for row in board) ):
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i,j) for i in range(board_size) for j in range(board_size) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if ( board[i][j] != EMPTY):
        raise ValueError("Cell already occupied")
    
    new_board = copy.deepcopy(board)
    current_player = player(board)
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(board_size):
        for j in range (board_size -2):
            if ( board[i][j] != EMPTY):
                if (board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2]):
                    return board[i][j]
        
    for i in range(board_size - 2):
        for j in range (board_size):
            if ( board[i][j] != EMPTY):
                if (board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j]):
                    return board[i][j]

    for i in range(board_size -2):
        for j in range (board_size -2):
            if (board[i][j] != EMPTY):
                if (board[i][j] == board[i+1][j+1] and board[i][j] == board[i+2][j+2]):
                    return board[i][j]
            if (board[i+2][j] != EMPTY):
                if (board[i+2][j] == board[i+1][j+1] and board[i+2][j] == board[i][j+2]):
                    return board[i+2][j]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
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
    if terminal(board):
        return None
    
    current_player = player(board)

    if ( current_player == X):
        _, best_action = max_value(board)
    else:
        _, best_action = min_value(board)
    
    return best_action

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    value = -math.inf
    best_action = None
    for action in actions(board):
        min_val, _  = min_value( result(board, action))
        if (min_val > value):
            value = min_val
            best_action = action

    return value, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    value = math.inf
    best_action = None
    for action in actions(board):
        max_val, _  = max_value( result(board, action))
        if (max_val < value):
            value = max_val
            best_action = action

    return value, best_action