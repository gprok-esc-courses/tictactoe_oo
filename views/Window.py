
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QStatusBar, QGridLayout

from views.AbstractWindow import AbstractWindow
from views.Cell import Cell


class Window(QMainWindow, AbstractWindow):
    def __init__(self, controller):
        super(Window, self).__init__()
        self.controller = controller
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
        self.play_again_btn.clicked.connect(self.controller.button_clicked)

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
                cell = Cell("-", row, col, self.controller)
                row_buttons.append(cell)
                cell.reset()
                layout.addWidget(cell, row, col, 1, 1)
            self.board.append(row_buttons)
        widget.setLayout(layout)
        self.layout.addWidget(widget)

    def display_status(self, msg):
        self.status_bar.showMessage(msg)

    def reset(self):
        self.status_bar.showMessage("")
        for row in range(3):
            for col in range(3):
                self.board[row][col].reset()



