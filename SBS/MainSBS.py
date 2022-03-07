from PyQt6.QtWidgets import QMainWindow, QMenuBar, QFileDialog
from PyQt6.QtGui import QAction, QKeySequence, QPixmap
from Widget import Widget

class MainSBS(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Py SBS")
        self.myCentralWidget = Widget()
        self.setCentralWidget(self.myCentralWidget)

        #self.setFixedSize(700, 700)

        mymenuBar = QMenuBar(self)
        self.setMenuWidget(mymenuBar)
