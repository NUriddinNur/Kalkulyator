from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulyator")

        self.mainBox = QVBoxLayout()
        self.mainBox.setAlignment(Qt.AlignTop)

        # Box1
        self.Box1 = QHBoxLayout()
        self.input = QLineEdit()
        self.Box1.addWidget(self.input)

        # Box2
        self.Box2 = QHBoxLayout()
        self.c_button = QPushButton("C")
        self.minus_button = QPushButton("+/-")
        self.divide_button = QPushButton("/")
        self.backspace_button = QPushButton("<--")
        self.Box2.addWidget(self.c_button)
        self.Box2.addWidget(self.minus_button)
        self.Box2.addWidget(self.divide_button)
        self.Box2.addWidget(self.backspace_button)



        self.mainBox.addLayout(self.Box1)
        self.mainBox.addLayout(self.Box2)

        container = QWidget()
        container.setLayout(self.mainBox)

        self.setCentralWidget(container)




app = QApplication([])

window = MainWindow()
window.show()

app.exec()

