from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax


class Board(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.size = 9
        self.board = [['.' for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 1

    def show(self):
        print("  " + " ".join(str(i) for i in range(1, len(self.board) + 1)))
        for i in range(len(self.board)):
            print(f"{i + 1} {' '.join(self.board[i])}")

    def possible_moves(self):
        moves = []
        for row in range(1, self.size + 1):
            for col in range(1, self.size + 1):
                if self.board[row - 1][col - 1] == '.':
                    moves.append('{},{}'.format(row, col))
        return moves

    def make_move(self, coord):
        coord_data = coord.split(',')
        row = int(coord_data[0]) - 1
        col = int(coord_data[1]) - 1
        if self.board[row][col] == '.':
            if game.current_player == 1:
                symbol = 'x'
            else:
                symbol = 'o'
            self.board[row][col] = symbol
            return True
        else:
            return False

    def win(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        def check_direction(start_row, start_col, dr, dc, symbol):
            for i in range(5):
                r, c = start_row + i * dr, start_col + i * dc
                if not (0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == symbol):
                    return False
            return True

        for start_row in range(len(self.board)):
            for start_col in range(len(self.board[0])):
                symbol = self.board[start_row][start_col]
                if symbol in ['x', 'o']:
                    for dr, dc in directions:
                        if check_direction(start_row, start_col, dr, dc, symbol):
                            return True
        return False

    def is_over(self):
        return self.win() or all(cell != '.' for row in self.board for cell in row)

    # def switch_player(self):
    #     self.current_player = 'o' if self.current_player == 'x' else 'x'

    def scoring(self):
        return 100 if self.win() else 0


# def main():
#     ai = Negamax(10)  # The AI will think 10 moves in advance
#     game = Board([AI_Player(ai), Human_Player()])
#     history = game.play()
#
#     while True:
#         game.show()
#         moves = game.possible_moves()
#         print(f'Possible moves: {moves}')
#
#         coord = []
#         row = int(input(f'Player {game.current_player}, enter row (1-9): ')) - 1
#         coord.append(row)
#         col = int(input(f'Player {game.current_player}, enter col (1-9): ')) - 1
#         coord.append(col)
#
#         # if coord in moves:
#         #     if game.make_move(coord):
#         #         if game.win():
#         #             game.show()
#         #             print(f'Player {game.current_player} wins!')
#         #             break
#         #
#         # else:
#         #     print('Invalid move. Try again.')

#
ai = Negamax(5)  # The AI will think 10 moves in advance
game = Board([Human_Player(), AI_Player(ai)])
history = game.play()
