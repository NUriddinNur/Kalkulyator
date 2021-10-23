from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulyator")

        self.mainBox = QVBoxLayout()
        self.mainBox.setAlignment(Qt.AlignTop)

        self.Box1 = QHBoxLayout()
        self.input = QLineEdit()
        self.Box1.addWidget(self.input)

        self.mainBox.addLayout(self.Box1)

        container = QWidget()
        container.setLayout(self.mainBox)

        self.setCentralWidget(container)




app = QApplication([])

window = MainWindow()
window.show()

app.exec()

