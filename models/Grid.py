

class Grid:
    def __init__(self):
        self.board = []
        self.reset()

    def reset(self):
        self.board = []
        for row in range(3):
            values = []
            for col in range(3):
                values.append(0)
            self.board.append(values)

    def is_empty(self, row, col):
        return self.board[row][col] == 0

    def play(self, row, col, player_val):
        if self.is_empty(row, col):
            self.board[row][col] = player_val
            return True
        else:
            return False
