import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulyator")
        self.input_values1 = ""
        self.input_values2 = ""
        self.operation = ""

        self.mainBox = QVBoxLayout()
        self.mainBox.setAlignment(Qt.AlignTop)

        # Box1
        self.Box1 = QHBoxLayout()
        self.input = QLineEdit()
        self.Box1.addWidget(self.input)

        # Box2
        self.Box2 = QHBoxLayout()
        self.c_button = QPushButton("C")
        self.c_button.setStyleSheet("background-color: red")

        self.minus_button = QPushButton("+/-")
        self.divide_button = QPushButton("/")
        self.backspace_button = QPushButton("<--")
        self.Box2.addWidget(self.c_button)
        self.Box2.addWidget(self.minus_button)
        self.Box2.addWidget(self.divide_button)
        self.Box2.addWidget(self.backspace_button)

        # Box 3
        self.Box3 = QHBoxLayout()
        self._7_button = QPushButton("7")
        self._8_button = QPushButton("8")
        self._9_button = QPushButton("9")
        self._x_button = QPushButton("x")
        self.Box3.addWidget(self._7_button)
        self.Box3.addWidget(self._8_button)
        self.Box3.addWidget(self._9_button)
        self.Box3.addWidget(self._x_button)

        # Box 4
        self.Box4 = QHBoxLayout()
        self._4_button = QPushButton("4")
        self._5_button = QPushButton("5")
        self._6_button = QPushButton("6")
        self.minus_button = QPushButton("-")
        self.Box4.addWidget(self._4_button)
        self.Box4.addWidget(self._5_button)
        self.Box4.addWidget(self._6_button)
        self.Box4.addWidget(self.minus_button)

        # Box 5
        self.Box5 = QHBoxLayout()
        self._1_button = QPushButton("1")
        self._2_button = QPushButton("2")
        self._3_button = QPushButton("3")
        self.plyus_button = QPushButton("+")
        self.Box5.addWidget(self._1_button)
        self.Box5.addWidget(self._2_button)
        self.Box5.addWidget(self._3_button)
        self.Box5.addWidget(self.plyus_button)

        #Box 6
        self.Box6 = QHBoxLayout()
        self._0_button = QPushButton("0")
        self.dot_button = QPushButton(".")
        self.exit_button = QPushButton("exit")
        self.equal_button = QPushButton("=")
        self.Box6.addWidget(self._0_button)
        self.Box6.addWidget(self.dot_button)
        self.Box6.addWidget(self.exit_button)
        self.Box6.addWidget(self.equal_button)

        self.mainBox.addLayout(self.Box1)
        self.mainBox.addLayout(self.Box2)
        self.mainBox.addLayout(self.Box3)
        self.mainBox.addLayout(self.Box4)
        self.mainBox.addLayout(self.Box5)
        self.mainBox.addLayout(self.Box6)

        container = QWidget()
        container.setLayout(self.mainBox)

        self.setCentralWidget(container)

        self._0_button.clicked.connect(lambda: self.number_clicked("0"))
        self._1_button.clicked.connect(lambda: self.number_clicked("1"))
        self._2_button.clicked.connect(lambda: self.number_clicked("2"))
        self._3_button.clicked.connect(lambda: self.number_clicked("3"))
        self._4_button.clicked.connect(lambda: self.number_clicked("4"))
        self._5_button.clicked.connect(lambda: self.number_clicked("5"))
        self._6_button.clicked.connect(lambda: self.number_clicked("6"))
        self._7_button.clicked.connect(lambda: self.number_clicked("7"))
        self._8_button.clicked.connect(lambda: self.number_clicked("8"))
        self._9_button.clicked.connect(lambda: self.number_clicked("9"))

        self.c_button.clicked.connect(self.c_click)

        self.plyus_button.clicked.connect(lambda: self.operation_chosen("+"))
        self.minus_button.clicked.connect(lambda: self.operation_chosen("-"))
        self.divide_button.clicked.connect(lambda: self.operation_chosen("/"))
        self._x_button.clicked.connect(lambda: self.operation_chosen("*"))

        self.backspace_button.clicked.connect(lambda: self.delete())

        self.equal_button.clicked.connect(self.get_result)

        self.exit_button.clicked.connect(sys.exit)


    def number_clicked(self, num: str) -> None:
        if not self.operation:
            self.input_values1 += num
            self.input.setText(self.input_values1)
        else:
            self.input_values2 += num
            self.input.setText(self.input_values2)

    def c_click(self):
        self.input_values1 = self.input_values2 = self.operation = ""
        self.input.setText(self.input_values1)

    def operation_chosen(self, op):
        self.operation = op
        self.input_values2 = ""

    def get_result(self):
        if self.operation == "+":
            self.input_values1 = str(float(self.input_values1) + float(self.input_values2))
        elif self.operation == "/":
            self.input_values1 = str(float(self.input_values1) / float(self.input_values2))
        elif self.operation == "-":
            self.input_values1 = str(float(self.input_values1) - float(self.input_values2))
        else:
            self.input_values1 = str(float(self.input_values1) * float(self.input_values2))

        if self.input_values1.split(".")[-1] == "0":
            self.input_values1 = self.input_values1.split(".")[0]
        self.input.setText(self.input_values1)

    def delete(self):
        list1 = []
        if self.input_values1 == "":
            pass
        else:
            list1.extend(self.input_values1)
            list1.pop(-1)
            self.input_values1 = "".join(list1)
            self.input.setText(self.input_values1)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
