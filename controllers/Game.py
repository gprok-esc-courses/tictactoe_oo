from models.Grid import Grid
from models.Player import Player
from views.App import App
from views.Window import Window


class Game:
    def __init__(self):
        self.app = App()
        self.window = Window(self)
        self.grid = Grid()
        self.p1 = Player('X', 1)
        self.p2 = Player('O', 2)
        self.curent_player = self.p1
        self.display_player()
        self.game_over = False

    def start(self):
        self.window.show()
        self.app.start()

    def button_clicked(self):
        print("button clicked")
        self.game_over = False
        self.grid.reset()
        self.window.reset()
        self.display_player()

    def display_player(self):
        self.window.display_status(self.curent_player.symbol + " PLAYS")

    def cell_clicked(self, cell):
        if self.game_over:
            return
        print("cell clicked " + str(cell.row) + " " + str(cell.col))
        if self.grid.play(cell.row, cell.col, self.curent_player.value):
            cell.display_player(self.curent_player.symbol)
            self.swap_player()
            self.display_player()
            self.check_for_winner_or_tie()
        else:
            print("Invalid position")

    def swap_player(self):
        self.curent_player = self.p1 if self.curent_player == self.p2 else self.p2

    def check_for_winner_or_tie(self):
        w = self.grid.winner()
        if w > 0:
            winner = self.p1 if self.p1.value == w else self.p2
            self.window.display_status(winner.symbol + " WINS!")
            self.game_over = True
        else:
            if self.grid.is_tie():
                self.window.display_status("IT'S A TIE!")
                self.game_over = True



if __name__ == '__main__':
    game = Game()
    game.start()
