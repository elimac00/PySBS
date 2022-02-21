from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
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

        text = QLabel(self)
        text.setText("Bild")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(text)

        first_button = QPushButton(self)
        first_button.setText("verkleinern!")
        first_button.setToolTip("Hilfetext")
        first_button.setToolTipDuration(10 * 200)
        first_button.clicked.connect(self.smaller)

        second_button = QPushButton(self)
        second_button.setText("vergrößern!")
        second_button.setToolTip("Hilfetext")
        second_button.setToolTipDuration(10 * 200)
        second_button.clicked.connect(self.bigger)

        self.picture = QPixmap("pragser_wildsee_lago_di_braies_suedtirol_italien_GettyImages-1179457554.jpg")
        self.pictureLabel = self.picture.scaled(600, 450)

        self.label = QLabel()
        self.label.setPixmap(self.pictureLabel)

        textLabel = QLabel
        textLabel.setText("Bildvergrößerer")

        layout.addWidget(textLabel, 0, 1)
        layout.addWidget(first_button, 2, 0)
        layout.addWidget(second_button, 2, 2)
        layout.addWidget(self.label, 1, 0, 1, 0)

        #third_button = QPushButton(self)
        #third_button.setText("Naja!")
        #third_button.setToolTip("Hilfetext")
        #third_button.setToolTipDuration(10 * 200 )

        layout.addWidget(first_button)
        layout.addWidget(second_button)
        #layout.addWidget(third_button)


    def smaller(self):
        self.pictureLabel = self.piture.scaled(400, 300)
        self.label.setPixmap(self.picture)

    def bigger(self):
        self.pictureLabel = self.picture.scaled(800,600)
        self.label.setPixmap(self.picture)


