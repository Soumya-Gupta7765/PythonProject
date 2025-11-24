from board import rows, cols, SAVE_FILE, count_adjacent, Cell

def save_game(board, filename=SAVE_FILE):
    with open(filename, "w") as f:
        f.write(f"{rows} {cols} {cols}\n")             # saves number of rows, columns and num_mines
        
        mines = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c].mine:
                    mines.append(f"{r},{c}")                # saves locations of mines into text file
        f.write(" ".join(mines) + "\n")
        
        revealed = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c].revealed:
                    revealed.append(f"{r},{c}")             # saves revealed cells into text file
        f.write(" ".join(revealed) + "\n")
        
        flagged = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c].flagged:
                    flagged.append(f"{r},{c}")              # saves flagged cells into text file
        f.write(" ".join(flagged) + "\n")
def load_game(filename=SAVE_FILE):
    f = open(filename, "a+")            # file is opened
    f.seek(0)
    lines = f.readlines()               # saves lines in list as strings
    f.close()

    if not lines:
        return None

    board = [[Cell() for i in range(cols)] for j in range(rows)]        # create a board
    
    for pos in lines[1].split():
        r, c = map(int, pos.split(","))                 # sets the mines as the saved game
        board[r][c].mine = True

    for r in range(rows):
        for c in range(cols):                           # gives number of mines surrounding as the saved game
            if not board[r][c].mine:
                board[r][c].adjacent = count_adjacent(board, r, c)

    for pos in lines[2].split():
        r, c = map(int, pos.split(","))                 # gives the revealed cells as the saved game
        board[r][c].revealed = True
    
    for pos in lines[3].split():
        r, c = map(int, pos.split(","))                 # gives thr flagged cells as the saved game
        board[r][c].flagged = True

    print("[save loaded]")
    return board


def has_save(filename=SAVE_FILE):
    f = open(filename, "r")
    f.seek(0)
    content = f.read().strip()              #saves the game in the text file
    f.close()

    if(content==""):
        return False
    return True

def remove_save(filename=SAVE_FILE):
    f = open(filename, "w")                 # removes the previous game to give place to the running one
    f.write("")
    f.close()

def is_number(s):
    return s.isdigit()
