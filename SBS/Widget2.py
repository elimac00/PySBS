from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Widget2(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.customer_core_data = QLabel(self)
        self.customer_core_data.setText("Customer Core data:")
        layout.addWidget(self.customer_core_data, 1,1)

        self.box = QTreeWidget()
        self.box.setHeaderLabels(["ID", "Lastname", "Firstname", "Title", "Telephone", "Telefax", "E-Mail", "Company"])
        layout.addWidget(self.box, 2, 1, 1, 2)
