import random

rows, cols, nmines = 9, 9, 10
SAVE_FILE = "pytxt.txt"

class Cell:
    def __init__(self):
        self.mine = False
        self.revealed = False
        self.flagged = False
        self.adjacent = 0

def count_adjacent(board, r, c):
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc].mine:
                n += 1
    return n

def create_board():
    board = [[Cell() for i in range(cols)] for j in range(rows)]

    mines = set()
    while len(mines) < nmines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if not board[r][c].mine:
            board[r][c].mine = True
            mines.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if not board[r][c].mine:
                board[r][c].adjacent = count_adjacent(board, r, c)

    return board
