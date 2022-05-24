import sys

from App import App
from Window import Window


class Game:
    def __init__(self):
        self.app = App()
        self.window = Window()

    def start(self):
        self.window.show()
        self.app.start()


if __name__ == '__main__':
    game = Game()
    game.start()
