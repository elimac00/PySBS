from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

if __name__ == "__main__":
    application = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    application.exec()