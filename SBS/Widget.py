from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)
        self.setLayout(layout)

        client_button = QPushButton(self)
        client_button.setText("customer")

        add_button = QPushButton(self)
        add_button.setText("add")