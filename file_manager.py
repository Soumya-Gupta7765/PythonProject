from board import rows, cols, SAVE_FILE, count_adjacent, Cell

def save_game(board, filename=SAVE_FILE):
    with open(filename, "w") as f:
        f.write(f"{rows} {cols} {cols}\n")

        mines = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c].mine:
                    mines.append(f"{r},{c}")
        f.write(" ".join(mines) + "\n")

        revealed = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c].revealed:
                    revealed.append(f"{r},{c}")
        f.write(" ".join(revealed) + "\n")

        flagged = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c].flagged:
                    flagged.append(f"{r},{c}")
        f.write(" ".join(flagged) + "\n")

def load_game(filename=SAVE_FILE):
    f = open(filename, "a+")
    f.seek(0)
    lines = f.readlines()
    f.close()

    if not lines:
        return None

    board = [[Cell() for i in range(cols)] for j in range(rows)]

    for pos in lines[1].split():
        r, c = map(int, pos.split(","))
        board[r][c].mine = True

    for r in range(rows):
        for c in range(cols):
            if not board[r][c].mine:
                board[r][c].adjacent = count_adjacent(board, r, c)

    for pos in lines[2].split():
        r, c = map(int, pos.split(","))
        board[r][c].revealed = True

    for pos in lines[3].split():
        r, c = map(int, pos.split(","))
        board[r][c].flagged = True

    print("[save loaded]")
    return board

def has_save(filename=SAVE_FILE):
    f = open(filename, "r")
    f.seek(0)
    content = f.read().strip()
    f.close()
    return content != ""

def remove_save(filename=SAVE_FILE):
    open(filename, "w").write("")

def is_number(s):
    return s.isdigit()
