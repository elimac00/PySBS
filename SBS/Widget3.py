from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Widget3(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.customer_overview = QLabel(self)
        self.customer_overview.setText("Customer-Overview:")
        layout.addWidget(self.customer_overview, 1, 1, 1, 2)

        self.box = QTreeWidget()
        self.box.setHeaderLabels(["ID", "Lastname", "Firstname"])
        layout.addWidget(self.box, 5,1,1,2)


