"""
Autorzy:
Hołdakowski, Mikołaj (s23739)
Rutkowski, Marcin (s12497)
Gra Gomoku
Zasady: https://en.wikipedia.org/wiki/Gomoku
"""
import pydoc
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class Board(TwoPlayerGame):
    def __init__(self, players=None):
        """
        Initialization of the Gomoku game

        ":param" players (list) a Human_Player then AI_Player.
        :returns: None
        """
        self.players = players
        self.size = 9
        self.board = [['.' for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 1

    def show(self):
        """
        Displays the board with index numbers from 1 to 'size'.

        :param: None
        :returns: None
        """
        print("  " + " ".join(str(i) for i in range(1, len(self.board) + 1)))
        for i in range(len(self.board)):
            print(f"{i + 1} {' '.join(self.board[i])}")

    def possible_moves(self):
        """
        Returns a list of available moves on the board.

        :param: None
        :returns: list of available moves as a pair of coordinates (first rows then columns).
        """
        moves = []
        for row in range(1, self.size + 1):
            for col in range(1, self.size + 1):
                if self.board[row - 1][col - 1] == '.':
                    moves.append('{},{}'.format(row, col))
        return moves

    def make_move(self, coord):
        """
        Makes a move.

        :param coord: a list of two strings taken from movement input later split into two values and cast to integers
        :returns: True / False
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
        """
        Checks if there is a winning move on the board

        :param: None
        :returns: True / False - True when there is a winning move, False when not
        """
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
        """
        Checks if the game is over by win or draw.

        :param: None
        :returns: True / False - True when there is game over
        """
        return self.win() or all(cell != '.' for row in self.board for cell in row)

    # def switch_player(self):
    #     self.current_player = 'o' if self.current_player == 'x' else 'x'

    def scoring(self):
        """
        Calculating Score of current game state

        :param: None
        :returns: Score of the current game state as int.
        """
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
        """
        Evaluates the position on the board for a given player using tactical approach, it judges every single field
        instead of whole board altogether.

        :param row: Row number.
        :param col: Column number.
        :param symbol: Player symbol ('x' or 'o').

        :returns: Score of the position for the given player as int.
        """
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


ai = Negamax(3)  # The AI will think n moves in advance
game = Board([Human_Player(), AI_Player(ai)])
pydoc.doc(Board)
history = game.play()