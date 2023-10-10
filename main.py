class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.current_player = 'x'

    def print(self):
        print("  " + " ".join(str(i) for i in range(1, len(self.board) + 1)))
        for i in range(len(self.board)):
            print(f"{i + 1} {' '.join(self.board[i])}")

    def make_move(self, row, col):
        if self.board[row][col] == '.':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def check_win(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            r, c = row, col
            while 0 <= r + dr < self.size and 0 <= c + dc < self.size and self.board[r + dr][c + dc] == self.current_player:
                count += 1
                r, c = r + dr, c + dc
                if count == 5:
                    return True
        return False

    def is_draw(self):
        return all(cell != '.' for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = 'o' if self.current_player == 'x' else 'x'


def main():
    size = 9
    board = Board(size)

    while True:
        board.print()
        row = int(input(f'Player {board.current_player}, enter row (1-{size}): ')) - 1
        col = int(input(f'Player {board.current_player}, enter col (1-{size}): ')) - 1

        if board.make_move(row, col):
            if board.check_win(row, col):
                board.print()
                print(f'Player {board.current_player} wins!')
                break

            if board.is_draw():
                board.print()
                print('It\'s a draw!')
                break

            board.switch_player()
        else:
            print('Invalid move. Try again.')


if __name__ == "__main__":
    main()
