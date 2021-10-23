from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulyator")

        self.setCentralWidget()



app = QApplication([])

window = QMainWindow()
window.show()


app.exec()