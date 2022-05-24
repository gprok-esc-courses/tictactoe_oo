from PyQt5.QtWidgets import QPushButton


class Cell(QPushButton):
    def __init__(self, label, row, col, controller):
        super(Cell, self).__init__(label)
        self.controller = controller
        self.row = row
        self.col = col
        self.setFixedWidth(150)
        self.setFixedHeight(150)
        self.setStyleSheet("font-size: 25px")
        self.clicked.connect(lambda state, b=self:  self.controller.cell_clicked(b))

    def display_player(self, symbol):
        self.setText(symbol)
        # self.setEnabled(False)
        self.setStyleSheet("background-color: red; font-size: 25px")
