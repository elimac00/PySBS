#startdesignerwithqt5-toolsdesigner
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QGraphicsView, QPushButton
from PyQt6 import uic

class MyDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyDialog, self).__init__()
        uic.loadUi("Hallo2.ui", self)
        self.__btn1 = self.findChild(QPushButton, "btn1")
        self.__btn1.clicked.connect(self.btn_test)



    def btn_test(self):
        print("clicked!!!")



app=QtWidgets.QApplication(sys.argv)
window=MyDialog()
window.show()
sys.exit(app.exec())

