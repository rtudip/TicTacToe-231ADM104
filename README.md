# Tic Tac Toe

This project implements a Tic Tac Toe game using the minimax algorithm to determine the optimal moves for each player. The game is designed in Python and features functions for handling the game's logic, including checking the current state of the board, determining the winner, and deciding the next move.

## Features

- **Initial State**: The game starts with an empty board of size 3x3.
- **Turn Management**: The program automatically determines whose turn it is based on the current state of the board.
- **Action Availability**: The program identifies all possible moves for the current player.
- **Result Calculation**: Updates the board with the current player's move.
- **Winner Detection**: Identifies if there is a winner by checking rows, columns, and diagonals.
- **Terminal State Check**: Determines if the game is over either by a win or a draw.
- **Utility Calculation**: Evaluates the final outcome of the game: +1 if "X" wins, -1 if "O" wins, and 0 for a draw.
- **Minimax Algorithm**: Implements the minimax algorithm to find the optimal move for the current player, ensuring the best possible outcome.

## How It Works

### Functions

- **`initial_state()`**: Returns the starting state of the board, which is a 3x3 grid of `EMPTY` cells.
  
- **`player(board)`**: Determines the current player based on the number of moves already made. "X" plays first, and players alternate turns.
  
- **`actions(board)`**: Returns a set of all available moves (empty cells) on the board.
  
- **`result(board, action)`**: Updates the board with the current player's move at the specified position. Raises a `ValueError` if the move is invalid (e.g., the cell is already occupied).
  
- **`winner(board)`**: Checks the board for a winner by evaluating rows, columns, and diagonals. Returns "X" or "O" if there's a winner, or `None` if there isn't.
  
- **`terminal(board)`**: Determines if the game is over by checking if there's a winner or if the board is full.
  
- **`utility(board)`**: Returns the game's outcome as a utility value: `1` if "X" wins, `-1` if "O" wins, and `0` for a draw.
  
- **`minimax(board)`**: Uses the minimax algorithm to return the optimal move for the current player. It alternates between maximizing "X"'s chances and minimizing "O"'s chances.
  
- **`max_value(board)`** and **`min_value(board)`**: These are helper functions used by `minimax` to evaluate the best move by maximizing or minimizing the utility.

### Minimax Algorithm

The minimax algorithm is a recursive function that explores all possible game states to find the best move for the current player. It simulates each possible move, evaluates the resulting board state, and chooses the move that maximizes the player's chances of winning while minimizing the opponent's chances.

