from PyQt6.QtWidgets import *
from MyWidget import MyWidget


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Title")

        myCentralWidget = MyWidget()
        self.setCentralWidget(myCentralWidget)

        myMenuBar = QMenuBar(self)
        self.setMenuWidget(myMenuBar)

        myMenu = myMenuBar.addMenu("Datei")
        myMenu.addAction("Bild laden", self.fileHandler)
        myMenu.addAction("Vergrößern", myCentralWidget.bigger)
        myMenu.addAction("Verkleinern", myCentralWidget.smaller)
        myMenu.addAction("Orginal", myCentralWidget.orginal)
        myMenu.addSection("Ab hier wirds komisch")

        mySubMenu = myMenu.addMenu("UnterMenü")
        mySubSubMenu = mySubMenu.addMenu("Untermenü vom Untermenü")
        mySubSubMenu.addAction("Punkt")
        mySubSubMenu.addSeparator()
        mySubSubMenu.addAction("Punkt 2")
        mySubMenu.addAction("Irgendeine Funktion")

        myMenuBar.show()

        self.fileHandler()

    def fileHandler(self):
        dialog = QFileDialog(self)
        dialog.setNameFilter("Hundebilder (*.png *.jpeg *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        #dialog.exec()
         #   fileName = dialog.selectFile()
          #  print(fileName)
