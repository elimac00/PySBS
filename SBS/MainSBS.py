from PyQt6.QtWidgets import QMainWindow, QMenuBar, QFileDialog, QTabWidget
from PyQt6.QtGui import QAction, QKeySequence, QPixmap
from Widget import Widget
from Widget2 import Widget2
from Widget3 import Widget3

class MainSBS(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Py SBS")

        self.myCentralWidget = QTabWidget()
        self.setCentralWidget(self.myCentralWidget)

        FirstTab = Widget()
        SecTab = Widget2()
        ThirdTab = Widget3()

        self.myCentralWidget.addTab(FirstTab, "Customer-Search")
        self.myCentralWidget.addTab(SecTab, "Customer-Core-Data")
        self.myCentralWidget.addTab(ThirdTab, "Customer-Overview")

        mymenuBar = QMenuBar(self)
        self.setMenuWidget(mymenuBar)
