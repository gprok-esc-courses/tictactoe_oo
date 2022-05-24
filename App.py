import sys

from PyQt5.QtWidgets import QApplication


class App(QApplication):
    def __init__(self):
        super(App, self).__init__(sys.argv)

    def start(self):
        sys.exit(self.exec())

