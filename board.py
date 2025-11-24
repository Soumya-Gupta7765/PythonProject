import random
rows,cols,nmines = 9, 9, 10
SAVE_FILE = "pytxt.txt"                      #Saved in a file named pytxt.txt

class Cell:
    def _init_(self):
        self.mine = False                #intializing with no mines
        self.revealed = False
        self.flagged = False
        self.adjacent = 0
def create_board():
    board = [[Cell() for i in range(cols)] for j in range(rows)]
                                             #creating 9x9 board with Cell characteristics 
    mines = set()
    while len(mines) < nmines:
        r = random.randint(0, rows - 1)     #generating random row,cols for placing mine
        c = random.randint(0, cols - 1)  
        if not board[r][c].mine:
            board[r][c].mine = True     
            mines.add((r, c))
    for r in range(rows):
        for c in range(cols):
            if not board[r][c].mine:
                board[r][c].adjacent = count_adjacent(board, r, c)
    return board
def count_adjacent(board, r, c):
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:                 # counts the mines adjacent to cell
                continue
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc].mine:
                n += 1
    return n
