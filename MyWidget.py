from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)
        # https://doc.qt.io/qtforpython-6/
        # Nutzen Sie drei weitere Layouts, welche Sie über die Qt-Doku finden.

        self.setLayout(layout)

        first_button = QPushButton(self)
        first_button.setText("verkleinern")
        first_button.setToolTip("Das ist der Hinweis Text")
        first_button.setToolTipDuration(5*1000)
        first_button.setShortcut("M")
        first_button.clicked.connect(self.smaller)
        layout.addWidget(first_button, 1, 1)

        second_button = QPushButton(self)
        second_button.setText("vergrößern")
        second_button.setToolTip("Das ist der Hinweis Text")
        second_button.setToolTipDuration(5 * 1000)
        second_button.clicked.connect(self.bigger)

        layout.addWidget(second_button, 1, 2)

        button_3 = QPushButton(self)
        button_3.setText("Orginal")
        button_3.setToolTip("Das ist der Hinweis Text")
        button_3.setToolTipDuration(5 * 1000)
        button_3.clicked.connect(self.orginal)

        layout.addWidget(button_3, 6, 1)

        slider_1 = QSlider(self)
        slider_1.setOrientation(Qt.Orientation.Horizontal)
        slider_1.setTickPosition(QSlider.TickPosition.TicksAbove)
        slider_1.setTickInterval(10)
        slider_1.setRange(1, 100)
        slider_1.setValue(50)
        slider_1.setToolTip("Bild vergrößern und verkleinern")
        slider_1.setToolTipDuration(5 * 1000)
        slider_1.valueChanged.connect(self.zoom)

        layout.addWidget(slider_1, 6, 2)


        lineEdit = QLineEdit(self)
        lineEdit.setText("Anfangstext")

        self.label35 = QLabel(self)
        self.label35.setText(lineEdit.text())
        lineEdit.textChanged.connect(self.label35.setText)
        layout.addWidget(lineEdit, 7, 1)

        self.textEdit = QTextEdit(self)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.textEdit.setText("Hallo Welt")
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.textEdit, 7, 0, 7, 3)
        layout.addWidget(self.label35, 7, 2)
        layout.addWidget(self.label35, 7, 2)


        self.picture = QPixmap("Katze3.jpeg")
        self.pictureLabel = self.picture.scaled(640, 480)

        self.label = QLabel()
        self.label.setPixmap(self.pictureLabel)

        layout.addWidget(self.label, 3, 1, 3, 2)

    def smaller(self):
        self.pictureLabel = self.picture.scaled(200, 300)
        self.label.setPixmap(self.pictureLabel)

    def bigger(self):
        self.pictureLabel = self.picture.scaled(800, 600)
        self.label.setPixmap(self.pictureLabel)

    def orginal(self):
        self.pictureLabel = self.picture.scaled(640, 480)
        self.label.setPixmap(self.pictureLabel)

    def zoom(self, percent):
        size = self.picture.size()
        scaled_size = size * percent/100.0
        self.label.setPixmap(self.picture.scaled(scaled_size))



    def open(self):
        path = "/Users/student/Pictures"
        title = "Katzenbild öffnen"
        fileType = "PNG (*.png *.jpg *.jpeg)"
        filename, type = QFileDialog.getOpenFileName(self, title, path, fileType)

        if filename == "":
            return

        if filename.endswith(".py"):
            file = QFile(filename)

            if file.open(QIODevice.OpenModeFlag.ReadOnly):
                out = QTextStream(file)
                text = out.readAll()
            else:
                text = "Could not open files " + filename

            self.textEdit.setText(text)
            return

        self.picture = QPixmap(filename)
        self.label.setPixmap(self.picture)
        self.label35.setText(type)


        self.textEdit.setText(filename)