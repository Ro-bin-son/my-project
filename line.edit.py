import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.label = QLabel(self)
        self.button =QPushButton("Submit", self)
        self.initUI()


    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.label.setGeometry(150, 70, 500, 40)
        self.label.setStyleSheet("font-size: 25px;"
                                 "color: orange;")
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.clicked.connect(self.submit)
    def submit(self):
        text = self.line_edit.text()
        self.label.setText(f"Vipi {text}😎")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
