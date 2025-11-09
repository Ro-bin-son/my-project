import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton, QLabel
from GUI import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Graphical User Interface")
        self.setStyleSheet("background-color: grey;")
        self.setGeometry(1000, 250, 700, 650)
        self.label = QLabel("Let's do some math here😎",self)
        self.button = QPushButton("Get result", self)
        self.line_edit1 = QLineEdit(self)

        self.line_edit2 = QLineEdit(self)
        self.line_edit3 = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.label.setGeometry(200, 0, 1000, 150)
        self.line_edit1.setGeometry(270, 120, 200, 40)
        self.line_edit2.setGeometry(270, 210, 200, 40)
        self.line_edit3.setGeometry(270, 300, 200, 40)
        self.button.setGeometry(270, 550, 150, 40)
        self.button.setStyleSheet("background-color: pink;"
                                  "border-radius: 10px;"
                                  "text-align: center;"
                                  "color: black;"
                                  "font-size: 20px;"
                                  )
        self.label.setStyleSheet("font-size: 35px; color: white; font-family: sans-serif;")

        self.line_edit1.setStyleSheet("background-color: white;"
                                      "font-size: 16px;")
        self.line_edit2.setStyleSheet("background-color: white;"
                                      "font-size: 16px;")
        self.line_edit3.setStyleSheet("background-color: white;"
                                      "font-size: 16px;")
        self.line_edit1.setPlaceholderText("Enter value1 here")
        self.line_edit2.setPlaceholderText("Enter value2 here")
        self.line_edit3.setPlaceholderText("Enter operator")

        self.button.clicked.connect(self.do_math)

    def do_math(self):
            try:
                num1 = float(self.line_edit1.text().strip())
                num2 = float(self.line_edit2.text().strip())
                operator = self.line_edit3.text().strip()

                if operator == "+":
                    self.label.setStyleSheet("font-size: 60px; color: white; font-weight: bold;")
                    result = num1 + num2
                elif operator == "-":
                    self.label.setStyleSheet("font-size: 60px; color: white; font-weight: bold;")
                    result = num1 - num2
                elif operator == "*":
                    self.label.setStyleSheet("font-size: 60px; color: white; font-weight: bold;")
                    result = num1 * num2

                elif operator == "/":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        self.label.setStyleSheet("font-size: 30px; color: white; font-weight: bold;")
                        result = "Error: Division by zero!"
                else:
                    self.label.setStyleSheet("font-size: 30px; color: white; font-weight: bold;")
                    result = "Invalid operator!"

            except ValueError:
                self.label.setStyleSheet("font-size: 30px; color: white; font-weight: bold;")
                result = "Please enter valid numbers."

            self.label.setText(str(result))
            self.button.hide()
            self.label.setGeometry(250, 320, 500, 200)


    def close_program(self):
        self.label.setText("Goodbye 👋")
        self.label.setGeometry(250, 220, 500, 150)
        self.label.setStyleSheet("font-size: 50px; color: lightgreen; font-family: sans-serif;")
        QTimer.singleShot(1000, self.close)

    def close_program0(self):
        self.label.setText("You left too soon😏")
        self.label.setGeometry(140, 220, 500, 250)
        self.label.setStyleSheet("font-size: 35px; color: lightgreen; font-family: sans-serif;")
        self.button0.hide()
        self.button00.hide()
        self.lineEdit.hide()
        self.time_label.hide()
        QTimer.singleShot(4000, self.close)  # close after 3 sec

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
