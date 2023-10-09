def initialize_board(size):
    board = [['.' for _ in range(size)] for _ in range(size)]
    return board

def print_board(board):
    print("  " + " ".join(str(i) for i in range(1, len(board) + 1)))
    for i in range(len(board)):
        print(f"{i+1} {' '.join(board[i])}")

def check_win(board, row, col, player):
    # Check for a winning condition
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        r, c = row, col
        while 0 <= r + dr < len(board) and 0 <= c + dc < len(board) and board[r+dr][c+dc] == player:
            count += 1
            r, c = r + dr, c + dc
            if count == 5:
                return True
    return False

def is_draw(board):
    return all(cell != '.' for row in board for cell in row)

def main():
    size = 9
    board = initialize_board(size)
    player = 'x'

    while True:
        print_board(board)
        row = int(input(f'Player {player}, enter row (1-{size}): ')) - 1
        col = int(input(f'Player {player}, enter col (1-{size}): ')) - 1

        if board[row][col] == '.':
            board[row][col] = player

            if check_win(board, row, col, player):
                print_board(board)
                print(f'Player {player} wins!')
                break

            if is_draw(board):
                print_board(board)
                print('It\'s a draw!')
                break

            player = 'o' if player == 'x' else 'x'
        else:
            print('Invalid move. Try again.')

if __name__ == "__main__":
    main()

