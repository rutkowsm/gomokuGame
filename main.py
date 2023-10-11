"""
Autorzy:
Hołdakowski, Mikołaj
Rutkowski, Marcin (s12497)
Gra Gomoku
Zasady: https://en.wikipedia.org/wiki/Gomoku
"""

from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax


class Board(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.size = 9
        self.board = [['.' for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 1

    def show(self):
        """Prints index numbers on the board numbered 1 - {size}
        Parameters: none
        Returns: none
        """
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
        """
        :param coord: a list of two strings taken from movement input later split into two values and cast to integers
        :return: True / False
        """
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
        if self.win():
            if self.current_player == 1:
                return 100
            else:
                return -100
        score = 0
        for row in range(self.size):
            for col in range(self.size):
                symbol = self.board[row][col]
                if symbol == 'x':
                    score += self.evaluate_position(row, col, 'x')
                elif symbol == 'o':
                    score -= self.evaluate_position(row, col, 'o')
        return score

    def evaluate_position(self, row, col, symbol):
        score = 0
        if (row, col) in [(2, 2), (2, 4), (4, 2), (4, 4)]:
            score += 5  # Center control
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            threat = False
            for i in range(5):
                r, c = row + i * dr, col + i * dc
                if not (0 <= r < self.size and 0 <= c < self.size):
                    break
                if self.board[r][c] == symbol:
                    score += 1  # Pieces in a row
                elif self.board[r][c] == '.':
                    if threat:
                        score += 2  # Win Threats
                    else:
                        score += 1  # Open position
                else:
                    threat = True
        return score


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
ai = Negamax(3)  # The AI will think 10 moves in advance
game = Board([Human_Player(), AI_Player(ai)])
history = game.play()
