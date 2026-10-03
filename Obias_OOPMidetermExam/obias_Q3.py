import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.x = 400
        self.y = 500
        self.width = 750
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.label = QLabel("Enter your fullname", self)
        self.label.setGeometry(100, 120, 200, 30)

        self.inputName = QLineEdit(self)
        self.inputName.setGeometry(400, 115, 300, 40)

        self.button = QPushButton("Click to display your fullname", self)
        self.button.setGeometry(100, 180, 250, 40)
        self.button.clicked.connect(self.displayName)

        self.outputName = QLabel("", self)
        self.outputName.setGeometry(400, 180, 300, 40)

        self.show()

    def displayName(self):
        name = self.inputName.text()
        self.outputName.setText(name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())