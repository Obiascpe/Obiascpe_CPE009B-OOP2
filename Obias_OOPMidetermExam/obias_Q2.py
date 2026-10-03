import os
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP2"
        self.x = 400
        self.y = 200
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.button = QPushButton("Click to Change the Color of the button", self)
        self.button.setGeometry(160, 180, 180, 40)
        self.button.clicked.connect(self.change_color)

        self.show()

    def change_color(self):
        self.button.setStyleSheet("background-color: yellow;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())