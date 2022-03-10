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
        layout.addWidget(self.box, 2,1,1,8)

        save_button = QPushButton(self)
        save_button.setText("Save")
        layout.addWidget(save_button,4,0)

        delete_button = QPushButton(self)
        delete_button.setText("Delete")
        layout.addWidget(delete_button, 4, 1)

        edit_button = QPushButton(self)
        edit_button.setText("Edit")
        layout.addWidget(edit_button, 4, 2)

        add_button = QPushButton(self)
        add_button.setText("Add")
        layout.addWidget(add_button, 4, 3)


    #def save(self):


    #def delete(self):

    #def edit(self):

    #def add(self):