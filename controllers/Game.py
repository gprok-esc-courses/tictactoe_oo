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

    def start(self):
        self.window.show()
        self.app.start()

    def button_clicked(self):
        print("button clicked")

    def cell_clicked(self, cell):
        print("cell clicked " + str(cell.row) + " " + str(cell.col))
        if self.grid.play(cell.row, cell.col, self.curent_player.value):
            cell.display_player(self.curent_player.symbol)
            self.swap_player()
        else:
            print("Invalid position")

    def swap_player(self):
        self.curent_player = self.p1 if self.curent_player == self.p2 else self.p2


if __name__ == '__main__':
    game = Game()
    game.start()
