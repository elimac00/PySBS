from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Widget2(QWidget):
    def __init__(self):
        super().__init__()

        #layout = QGridLayout(self)
        #self.setLayout(layout)

        widgetLayout = QVBoxLayout()
        self.setLayout(widgetLayout)

        stackedLayout = QHBoxLayout()

        self.customer_core_data = QLabel(self)
        self.customer_core_data.setText("Customer Core data:")
        widgetLayout.addWidget(self.customer_core_data)

        self.box = QTreeWidget()
        self.box.setHeaderLabels(["ID", "Lastname", "Firstname", "Title", "Telephone", "Telefax", "E-Mail", "Company"])
        widgetLayout.addWidget(self.box)
        widgetLayout.addLayout(stackedLayout)

        width = 20
        height = 20

        size_save = QSize(width, height)
        save_button = QPushButton(self)
        save_button.setText("Save")
        icon_save = QIcon("./safeicon.jpg")
        save_button.setIcon(icon_save)
        save_button.setIconSize(size_save)
        stackedLayout.addWidget(save_button)

        size_delete = QSize(width, height)
        delete_button = QPushButton(self)
        delete_button.setText("Delete")
        icon_delete = QIcon("./delete_icon.jpg")
        delete_button.setIcon(icon_delete)
        delete_button.setIconSize(size_delete)
        stackedLayout.addWidget(delete_button)

        size_edit = QSize(width, height)
        edit_button = QPushButton(self)
        edit_button.setText("Edit")
        icon_edit = QIcon("./edit_icon.png")
        edit_button.setIcon(icon_edit)
        edit_button.setIconSize(size_edit)
        stackedLayout.addWidget(edit_button)

        size_add = QSize(width, height)
        add_button = QPushButton(self)
        add_button.setText("Add")
        icon_add = QIcon("./add_icon.png")
        add_button.setIcon(icon_add)
        add_button.setIconSize(size_add)
        stackedLayout.addWidget(add_button)


    #def save(self):


    #def delete(self):

    #def edit(self):

    #def add(self):