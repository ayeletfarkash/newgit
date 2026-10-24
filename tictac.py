def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # בדוק שורות
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # בדוק עמודות
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # בדוק אלכסונים
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    for row in board:
        if any([cell == ' ' for cell in row]):
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"תור השחקן: {player}")
        try:
            row = int(input("בחר שורה (0-2): "))
            col = int(input("בחר עמודה (0-2): "))
            if board[row][col] != ' ':
                print("המקום תפוס. נסה שוב.")
                continue
        except (ValueError, IndexError):
            print("בחירה לא חוקית. נסה שוב.")
            continue
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"השחקן {player} ניצח!")
            break
        if is_full(board):
            print_board(board)
            print("תיקו!")
            break
        turn += 1

if __name__ == "__main__":
    main()