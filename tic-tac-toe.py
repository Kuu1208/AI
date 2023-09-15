import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game(player1, player2):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = random.choice([player1, player2])

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        row = int(input(f"Enter row (0, 1, 2): "))
        col = int(input(f"Enter column (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("다시 시도하세요")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return current_player
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            return "Tie"

        current_player = player1 if current_player == player2 else player2

def main():
    player1_wins = 0
    player2_wins = 0

    while player1_wins < 2 and player2_wins < 2:
        winner = play_game("X", "O")

        if winner == "X":
            player1_wins += 1
        elif winner == "O":
            player2_wins += 1

        print(f"Score: Player X {player1_wins} - {player2_wins} Player O")

    if player1_wins >= 2:
        print("Player X wins!")
    elif player2_wins >= 2:
        print("Player O wins!")

if __name__ == "__main__":
    main()
