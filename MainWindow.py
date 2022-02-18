from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Der Titel")

        centralWidget = QWidget(self)
        layout = QHBoxLayout(centralWidget)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        first_button = QPushButton(self)


        button_2 = QPushButton(self)
        button_2.setText("hallo")
        button_2.setToolTip("noooothing")


        first_button.setText("Mein erster QPushButton!")
        first_button.setToolTip("Das ist der Hinweistext")
        first_button.setToolTipDuration(10*200)

        layout.addWidget(first_button)


