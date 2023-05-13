def display_board(board):
    for row in board:
        print("".join(row))


def check_win(board):
    for row in board:
        if row.count("X") == 3:
            print("X win executed")
            return "X"
        if row.count("O") == 3:
            print("O win executed!")
            return "O"

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] != "-":
        return board[2][0]

    return None


def make_move(player, board):
    row = int(input("chose the row"))
    col = int(input("chose the column"))
    board[row][col] = player


def play():
    board = [["-" for col in range(3)] for row in range(3)]
    player = ["X", "O"]
    player_curr = 0
    winner = None
    while winner is None and any("-" in row for row in board):
        display_board(board)
        make_move(player[player_curr % 2], board)
        winner = check_win(board)
        player_curr += 1

    if winner is not None:
        print(f"player {winner} won")
    else:
        print("tie")

if __name__ == "__main__":
    play()
