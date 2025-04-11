def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Rows, Columns, Diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    return (board[0][0] == board[1][1] == board[2][2] == player or
            board[0][2] == board[1][1] == board[2][0] == player)

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current = "X"

    print("🎮 Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current}, enter row (0, 1, 2): "))
            col = int(input(f"Player {current}, enter col (0, 1, 2): "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("❌ Invalid position! Choose row/col between 0-2.")
            continue

        if board[row][col] != " ":
            print("❌ That spot is already taken!")
            continue

        board[row][col] = current
        print_board(board)

        if check_win(board, current):
            print(f"🏆 Player {current} wins!")
            break
        if check_draw(board):
            print("🤝 It's a draw!")
            break

        current = "O" if current == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
