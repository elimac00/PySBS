from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from MyWidget import MyWidget


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Title")

        self.myCentralWidget = MyWidget()
        self.setCentralWidget(self.myCentralWidget)

        myMenuBar = QMenuBar(self)
        self.setMenuWidget(myMenuBar)

        myMenu = myMenuBar.addMenu("Datei")
        myMenu.addAction("Bild laden....", self.myCentralWidget.open)
        myMenu.addAction("Vergrößern", self.myCentralWidget.bigger)
        myMenu.addAction("Verkleinern", self.myCentralWidget.smaller)
        myMenu.addAction("Orginal", self.myCentralWidget.orginal)
        myMenu.addSection("Ab hier wirds komisch")

        mySubMenu = myMenu.addMenu("UnterMenü")
        mySubSubMenu = mySubMenu.addMenu("Untermenü vom Untermenü")
        mySubSubMenu.addAction("Punkt")
        mySubSubMenu.addSeparator()
        mySubSubMenu.addAction("Punkt 2")
        mySubMenu.addAction("Irgendeine Funktion")

        myMenuBar.show()

