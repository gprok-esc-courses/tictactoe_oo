from PyQt5.QtWidgets import QPushButton


class Cell(QPushButton):
    def __init__(self, label):
        super(Cell, self).__init__(label)
        self.setFixedWidth(150)
        self.setFixedHeight(150)
        self.setStyleSheet("font-size: 25px")
