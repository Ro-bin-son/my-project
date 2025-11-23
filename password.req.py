import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from unicodedata import digit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Password Security💀💀")
        self.setStyleSheet("background-color: white;")
        self.label = QLabel("Create a strong password",self)
        self.small_label = QLabel("Password must:",self)
        self.checkbox1 = QCheckBox("Be between 8-12 characters.", self)
        self.checkbox2 = QCheckBox("Contain a '@'.", self)
        self.button = QPushButton("Submit", self)
        self.password_label = QLabel("Password required:",self)
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter your password")

        self.initUI()

    def initUI(self):
        self.label.setGeometry(100, 0, 350, 50)
        self.small_label.setGeometry(100, 45, 300, 30)
        self.checkbox1.setGeometry(120, 80, 500,20)
        self.checkbox2.setGeometry(120, 110, 500,20)
        self.button.setGeometry(150, 380, 180, 40)
        self.password_label.setGeometry(100, 150, 300, 30)
        self.line_edit.setGeometry(100, 180, 180, 30)
        self.label.setStyleSheet("color: black;"
                                 "font-size:28px;")
        self.button.setStyleSheet("color: white;"
                                 "font-size:25px;"
                                  "background-color: #d9deda;"
                                  "border-radius: 10px;")
        self.button.setDisabled(True)
        self.line_edit.setStyleSheet("color: grey;"
                                  "font-size:15px;"
                                  "background-color: white;"
                                  )
        self.checkbox1.setStyleSheet("color: black;")
        self.checkbox2.setStyleSheet("color: black;")

        # Connect typing signal to validation
        self.line_edit.textChanged.connect(self.condition_one)
        self.line_edit.textChanged.connect(self.condition_two)
        self.line_edit.textChanged.connect(self.both_conditions_true)

        # Button click
        self.button.clicked.connect(self.on_clicked)



    def on_clicked(self):
        self.small_label.hide()
        self.checkbox1.hide()
        self.checkbox2.hide()
        self.line_edit.hide()
        self.password_label.hide()
        self.button.hide()
        self.label.setGeometry(100, 170, 300, 40)
        self.label.setText("Logged in Successfully.")
        self.label.setStyleSheet("color: white;"
                                 "font-size:28px;")
        self.setStyleSheet("Background-color: grey;")


    def condition_one(self):
        answer = self.line_edit.text().strip()

        # If user is typing → default both to red
        if 8 <= len(answer) >= 12:
            self.checkbox1.setStyleSheet("color: green;")
            self.checkbox1.setChecked(True)
        else:
            self.checkbox1.setStyleSheet("color: red;")

    def condition_two(self):
        answer = self.line_edit.text().strip()
        if "@" in answer:
            self.checkbox2.setStyleSheet("color: green;")
            self.checkbox2.setChecked(True)
        else:
            self.checkbox2.setStyleSheet("color: red;")


    def both_conditions_true(self):
        answer = self.line_edit.text().strip()
        if 8 <= len(answer) >= 12 and "@" in answer :
            self.button.setStyleSheet("color: white;"
                                      "font-size:25px;"
                                      "background-color: #1ab6ff;"
                                      "border-radius: 10px;")
            self.button.setDisabled(False)
        else:
            self.button.setStyleSheet("color: white;"
                                      "font-size:25px;"
                                      "background-color: #d9deda;"
                                      "border-radius: 10px;")
            self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
