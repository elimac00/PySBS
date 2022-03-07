from PyQt6.QtWidgets import QApplication
from MainSBS import MainSBS
import sys

if __name__ == '__main__':
    application = QApplication(sys.argv)

    mainWindow = MainSBS()
    mainWindow.show()

    application.exec()


