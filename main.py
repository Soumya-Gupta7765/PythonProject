from board import create_board, rows, cols
from game_logic import reveal_cell, reveal_all_mines, check_win, display_board
from file_manager import save_game, load_game, has_save, remove_save, is_number

def play():
    if has_save():
        ans = input("Saved game found — load it? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            board = load_game()
            if board is None:
                board = create_board()
        else:
            board = create_board()
    else:
        board = create_board()

    moves = 0

    while True:
        display_board(board)
        print("Commands: 'r row col', 'f row col', 'save', 'load', 'quit'")
        raw = input("Enter: ").strip().lower()

        if raw == "quit":
            ans = input("Save game before exit? (y/n): ").strip().lower()
            if ans in ("y", "yes"):
                save_game(board)
            print("see u later...🙂")
            break

        if raw == "save":
            save_game(board)
            continue

        if raw == "load":
            nb = load_game()
            if nb:
                board = nb
            continue

        parts = raw.split()
        if len(parts) != 3:
            print("Bad input. Example: r 3 4")
            continue

        action, sr, sc = parts
        if not (is_number(sr) and is_number(sc)):
            print("Row and column must be integers.")
            continue

        r, c = int(sr), int(sc)
        if not (0 <= r < rows and 0 <= c < cols):
            print("Out of bounds.")
            continue

        moves += 1

        if action == "r":
            if board[r][c].mine:
                reveal_all_mines(board)
                display_board(board, show_mines=True)
                print(f"💥 Boom! You hit a mine. Game Over. Moves: {moves}")
                remove_save()
                break
            reveal_cell(board, r, c)
            if check_win(board):
                reveal_all_mines(board)
                display_board(board, show_mines=True)
                print(f"🏆 You cleared the field in {moves} moves!")
                remove_save()
                break

        elif action == "f":
            board[r][c].flagged = not board[r][c].flagged

        else:
            print("Unknown action. Use 'r' or 'f'.")

if __name__ == "__main__":
    play()
