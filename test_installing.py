from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Das Fenster')
window.setGeometry(100, 100, 300, 200)
helloMsg = QLabel('Hello World!', parent=window)
helloMsg.move(100, 100)

window.show()

sys.exit(app.exec())