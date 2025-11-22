from board import rows, cols, count_adjacent

def reveal_cell(board, r, c):
    if not (0 <= r < rows and 0 <= c < cols):
        return

    cell = board[r][c]
    if cell.revealed or cell.flagged:
        return

    cell.revealed = True

    if cell.adjacent == 0 and not cell.mine:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                reveal_cell(board, r + dr, c + dc)

def reveal_all_mines(board):
    for r in range(rows):
        for c in range(cols):
            if board[r][c].mine:
                board[r][c].revealed = True

def check_win(board):
    for r in range(rows):
        for c in range(cols):
            if not board[r][c].mine and not board[r][c].revealed:
                return False
    return True

def display_board(board, show_mines=False):
    print("    " + " ".join(str(c) for c in range(cols)))
    print("   " + "--" * cols)

    for r in range(rows):
        row = []
        for c in range(cols):
            cell = board[r][c]

            if cell.revealed or (show_mines and cell.mine):
                if cell.mine:
                    row.append("*")
                elif cell.adjacent == 0:
                    row.append(" ")
                else:
                    row.append(str(cell.adjacent))
            elif cell.flagged:
                row.append("⚑")
            else:
                row.append("■")

        print(f" {r} | " + " ".join(row))
    print()
