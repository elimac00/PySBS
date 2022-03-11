from PyQt6.QtWidgets import QMainWindow, QMenuBar, QFileDialog, QTabWidget
from PyQt6.QtGui import QAction, QKeySequence, QPixmap, QIcon
from Widget import Widget
from Widget2 import Widget2
from Widget3 import Widget3

class MainSBS(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Py SBS")
        #self.setFixedSize(600,600)

        self.myCentralWidget = QTabWidget()
        self.setCentralWidget(self.myCentralWidget)

        FirstTab = Widget()
        SecTab = Widget2()
        ThirdTab = Widget3()

        width = 20
        height = 20

        self.myCentralWidget.addTab(FirstTab, QIcon("./customer_search.png"), "Customer-Search")
        self.myCentralWidget.addTab(SecTab,QIcon("./customer.jpeg"), "Customer-Core-Data")
        self.myCentralWidget.addTab(ThirdTab, QIcon("./customers.png"), "Customer-Overview")

        mymenuBar = QMenuBar(self)
        self.setMenuWidget(mymenuBar)
