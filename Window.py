
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QStatusBar, QGridLayout

from Cell import Cell


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Tic Tac Toe OO")
        self.layout = QVBoxLayout()
        self.add_play_again_btn()
        self.add_status_bar()
        self.add_board()
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def add_play_again_btn(self):
        self.play_again_btn = QPushButton("Play Again")
        self.layout.addWidget(self.play_again_btn)

    def add_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("test")

    def add_board(self):
        self.board = []
        widget = QWidget()
        layout = QGridLayout()
        for row in range(3):
            row_buttons = []
            for col in range(3):
                cell = Cell("-")
                row_buttons.append(cell)
                layout.addWidget(cell, row, col, 1, 1)
            self.board.append(row_buttons)
        widget.setLayout(layout)
        self.layout.addWidget(widget)


