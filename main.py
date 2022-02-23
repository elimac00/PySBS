from PyQt6.QtWidgets import QApplication
from MainWindow import MyMainWindow
import sys

if __name__ == '__main__':
    application = QApplication(sys.argv)

    mainWindow = MyMainWindow()
    mainWindow.show()

    application.exec()

