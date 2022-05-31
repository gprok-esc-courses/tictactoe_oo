

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

    def winner(self):
        for i in range(3):
            if self.board[i][0] != 0:
                if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                    return self.board[i][0]
            if self.board[0][i] != 0:
                if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                    return self.board[0][i]
        if self.board[1][1] != 0:
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return self.board[1][1]
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return self.board[1][1]
        return 0

    def is_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return False
        return True
