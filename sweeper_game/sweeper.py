import numpy as np
from enum import Enum
from sweeper_game.utils.tile import Tile

class Sweeper_game:
    
    class ACTION(Enum):
        CHECK = 0
        FLAG = 1
        UNFLAG = 2
    
    def __init__(self):
        self._rows = 0
        self._cols = 0
        self._num_mines = 0
        self._status = False
        self._score = 0
        self._board = []
        self._unrevealed = 0

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols
    
    @property
    def num_mines(self):
        return self._num_mines
    
    @property
    def status(self):
        return self._status
    
    @property
    def score(self):
        return (self._score / (self._rows * self._cols - self._num_mines))
    
    def get_tile(self, row, col):
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            return -2
        if self._board[row][col].revealed:
            return self._board[row][col].value
        else:
            return -3

    def render(self, rows=None, cols=None, num_mines=None):
        self._rows = rows if rows is not None else self._rows
        self._cols = cols if cols is not None else self._cols
        self._num_mines = num_mines if num_mines is not None else self._num_mines
        self._status = True
        self._score = 0
        self._board = self.generate_board(rows, cols, num_mines)
        self._unrevealed = rows * cols - num_mines

    def generate_board(self, rows, cols, mines):
        board = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Tile(i, j, float('-inf')))
            board.append(row)

        for i in range(mines):
            x = np.random.randint(0, rows)
            y = np.random.randint(0, cols)
            while board[x][y].value == -1:
                x = np.random.randint(0, rows)
                y = np.random.randint(0, cols)
            board[x][y].value = -1

        for i in range(rows):
            for j in range(cols):
                if board[i][j].value != -1:
                    num = 0
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if i+k >= 0 and i+k < rows and j+l >= 0 and j+l < cols and board[i+k][j+l].value == -1:
                                num += 1
                    board[i][j].value = num

        for i in range(rows):
            for j in range(cols):
                board[i][j].value = 0

        board = np.array(board)
        return board

    def print_board(self):
        print('╔' + '═' * (self._cols) + '╗')
        for i in range(self._rows):
            string = '║'
            for j in range(self._cols):
                if self._board[i,j].revealed:
                    string += str(self._board[i,j].value)
                elif self._board[i,j].flagged:
                    string += '⚑'
                else:
                    string += '▣'
            string += '║'
            print(string)
        print('╚' + '═' * (self._cols) + '╝')

    def print_fail_board(self, row, col):
        print('╔' + '═' * (self._cols) + '╗')
        for i in range(self._rows):
            string = '║'
            for j in range(self._cols):
                if self._board[i,j].revealed:
                    if i == row and j == col:
                        string += 'X'
                    else:
                        string += str(self._board[i,j].value)
                elif self._board[i,j].flagged:
                    string += '⚑'
                else:
                    string += '▣'
            string += '║'
            print(string)
        print('╚' + '═' * (self._cols) + '╝')

    def step(self,action, row: int, col: int):
        if self.status == False:
            return False
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            self._status = False
            print(f'[ERROR] Out of bounds at row: {row}, col: {col}')
            return False
        if action not in [self.ACTION.CHECK, self.ACTION.FLAG, self.ACTION.UNFLAG]:
            self._status = False
            print(f'[ERROR] Invalid action: {action}')
            return False
        if action == self.ACTION.CHECK:
            if self._board[row, col].flagged:
                self._status = False
                print(f'[ERROR] Tile already flagged at row: {row}, col: {col}')
                return False
            if self._board[row, col].revealed:
                self._status = False
                print(f'[ERROR] Tile already revealed at row: {row}, col: {col}')
                return False
            if self._board[row, col].value == -1:
                self._board[row, col].reveal()
                self._status = False
                self.print_fail_board(row, col)
                print('[:(] Game Over, you stepped on a mine')
                return False
            else:
                self._board[row, col].reveal()
                self._score += 1
                self._unrevealed -= 1

                if self._unrevealed == 0:
                    self._status = False
                    self.print_board()
                    print(f'[:)] Congratulations, you won! Your score is: {str(self._score / (self._rows * self._cols - self._num_mines))}')

                return True
        elif action == self.ACTION.FLAG:
            if self._board[row, col].flag():
                return True
            else:
                self._status = False
                print(f'[ERROR] Tile already flagged at row: {row}, col: {col}')
                return False
        elif action == self.ACTION.UNFLAG:
            if self._board[row, col].unflag():
                return True
            else:
                self._status = False
                print(f'[ERROR] Tile is already not flagged at row: {row}, col: {col}')
                return False