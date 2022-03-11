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

        width = 20
        height = 20

        size = QSize(width, height)
        search_button = QPushButton(self)
        search_button.setText("search")
        icon_search = QIcon("./search_icon.png")
        search_button.setIcon(icon_search)
        search_button.setIconSize(size)
        layout.addWidget(search_button,4,3,1,1)

        self.combo1 = QComboBox(self)
        self.combo1.addItem("Lastname:")
        self.combo1.addItem("Firstname:")
        self.combo1.addItem("Telephone:")
        self.combo1.addItem("E-Mail:")
        self.combo1.addItem("Company:")
        layout.addWidget(self.combo1,0,2,1,2)
        self.combo1.currentTextChanged.connect(self.name)

        self.customer_search = QLabel(self)
        self.customer_search.setText("Customer-Search:")
        #customer = QIcon("./customer.jpeg")
        layout.addWidget(self.customer_search, 0, 0, 1, 2)

        self.textEdit1 = QLabel(self)
        self.textEdit1.setText("Id:")
        layout.addWidget(self.textEdit1, 1,1,1,1)

        self.LineEdit1 = QLineEdit(self)
        layout.addWidget(self.LineEdit1, 1, 2, 1, 1)

        self.LineEdit2 = QLineEdit(self)
        layout.addWidget(self.LineEdit2,2,2,1,1)

        self.textEdit2 = QLabel(self)
        layout.addWidget(self.textEdit2, 2,1,1,1)

    def name(self):
        text = self.combo1.currentText()
        self.textEdit2.setText(text)

        #TODO Bilder noch einsetzen ICONS

        #QRadioButton (Nur einen Punkt kann ich auswählen)
        #QCheckBox (Haken setzen)
        #QIcon (set.Icon) ----> Bild einfügen, den pfad einfügen





