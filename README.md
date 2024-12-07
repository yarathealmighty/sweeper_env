# Sweeper Game

## Overview
--------

Sweeper Game is a simple minesweeper game implemented in Python. The game is played on a rectangular board with a specified number of rows, columns, and mines.

## Game Steps
-------------

The game can be played by performing the following steps:

### 1. Initialize the Game

Create a new instance of the `Sweeper_game` class, specifying the number of rows, columns, and mines.

### 2. Render the Game

Use the `render` method to set up the game board with the specified number of rows, columns, and mines.

### 3. Print the Board

Use the `print_board` method to display the current state of the board.

### 4. Perform an Action

Use the `step` method to perform one of the following actions:

* `CHECK`: Reveal the contents of a cell.
* `FLAG`: Mark a cell as potentially containing a mine.
* `UNFLAG`: Remove a flag from a cell.

### 5. Check the Game Status

Use the `status` property to check if the game is still active.

### 6. Get the Score

Use the `score` property to get the current score.

## Game Rules
-------------

* If a cell containing a mine is revealed, the game ends and the `print_fail_board` method is called to display the final board state.
* If a cell is flagged, it cannot be revealed until it is unflagged.
* If a cell is revealed and does not contain a mine, the score is incremented.

## Example Usage

```python
from sweeper_game.sweeper import Sweeper_game
import random

env = Sweeper_game()
env.render(rows=16, cols=16, num_mines=40)
status = True
while status == True:
    env.print_board()
    row = random.randint(0, 15)
    col = random.randint(0, 15)
    print(f'[LOG] Player chooses {row}, {col}')
    status = env.step(Sweeper_game.ACTION.CHECK, row, col)