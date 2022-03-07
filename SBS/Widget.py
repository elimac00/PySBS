from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)
        self.setLayout(layout)

        #add_button = QPushButton(self)
        #add_button.setText("add")
        #layout.addWidget(add_button,2,2)

        #delete_button = QPushButton(self)
        #delete_button.setText("delete")
        #layout.addWidget(delete_button,1,2)



        self.customer_search = QLabel(self)
        self.customer_search.setText("Customer-Search:")
        layout.addWidget(self.customer_search, 0, 0, 1, 2)

        self.textEdit = QLabel(self)
        self.textEdit.setText("Id:")
        layout.addWidget(self.textEdit, 1,1,1,1)

        self.textEdit = QLabel(self)
        self.textEdit.setText("Name:")
        layout.addWidget(self.textEdit, 2,1,1,1)

        lineEdit1 = QLineEdit(self)
        layout.addWidget(lineEdit1, 1,2,1,1)

        lineEdit2 = QLineEdit(self)
        layout.addWidget(lineEdit2,2,2,1,1)

        self.customer_overview = QLabel(self)
        self.customer_overview.setText("Customer-Overview:")
        layout.addWidget(self.customer_overview, 0,5,1,2)






