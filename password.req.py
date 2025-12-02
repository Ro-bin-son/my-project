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
        self.checkbox3 = QCheckBox("Contain at least one digit.", self)
        self.button = QPushButton("Submit", self)
        self.save_button = QPushButton("Save", self)
        self.cancel_button = QPushButton("Cancel", self)
        self.password_label = QLabel("Password required:",self)
        self.line_edit = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter your password")
        self.initUI()

    def initUI(self):
        self.line_edit2.hide()
        self.save_button.hide()
        self.cancel_button.hide()
        self.label.setGeometry(100, 0, 350, 50)
        self.small_label.setGeometry(100, 45, 300, 30)
        self.checkbox1.setGeometry(120, 80, 500,20)
        self.checkbox2.setGeometry(120, 110, 500,20)
        self.checkbox3.setGeometry(120, 140, 500,20)
        self.button.setGeometry(150, 380, 180, 40)
        self.password_label.setGeometry(100, 170, 300, 30)
        self.line_edit.setGeometry(100, 200, 180, 30)
        self.label.setStyleSheet("color: black;"
                                 "font-size:28px;")
        self.button.setStyleSheet("color: white;"
                                 "font-size:25px;"
                                  "background-color: #d9deda;"
                                  "border-radius: 10px;")
        self.button.setDisabled(True)
        self.line_edit.setStyleSheet("color: black;"
                                  "font-size:15px;"
                                  "background-color: white;"
                                  )
        self.checkbox1.setStyleSheet("color: black;")
        self.checkbox2.setStyleSheet("color: black;")
        self.checkbox3.setStyleSheet("color: black;")

        # Connect typing signal to validation
        self.line_edit.textChanged.connect(self.condition_one)
        self.line_edit.textChanged.connect(self.condition_two)
        self.line_edit.textChanged.connect(self.both_conditions_true)
        self.line_edit.textChanged.connect(self.condition_three)
        # Button click
        self.button.clicked.connect(self.on_clicked)



    def on_clicked(self):
        self.small_label.hide()
        self.checkbox1.hide()
        self.checkbox2.hide()
        self.checkbox3.hide()
        self.line_edit.hide()
        self.password_label.hide()
        self.button.hide()
        self.label.setGeometry(60, 60, 500, 80)
        self.label.setText("You just created a Password. Do you\n wish to save it?")
        self.save_button.show()
        self.cancel_button.show()
        self.save_button.setGeometry(90, 260, 130, 40)
        self.cancel_button.setGeometry(290, 260, 130, 40)
        self.label.setStyleSheet("color: white;"
                                 "font-size:25px;")
        self.save_button.setStyleSheet("color: white;"
                                       "background-color: #2d2dff;"
                                      "font-size:28px;"
                                       "border-radius: 10px;")
        self.cancel_button.setStyleSheet("color: white;"
                                       "background-color: #1ab6ff;"
                                       "font-size:28px;"
                                         "border-radius: 10px;")

        self.setStyleSheet("Background-color: grey;")
        try:
            self.save_button.clicked.disconnect()
        except Exception:
            pass
        self.save_button.clicked.connect(self.create_file)


    def condition_one(self):
        answer = self.line_edit.text().strip()

        # If user is typing → default both to red
        if 8 <= len(answer) <= 25:
            self.checkbox1.setStyleSheet("color: green;")
            self.checkbox1.setChecked(True)
        else:
            self.checkbox1.setStyleSheet("color: red;")
            self.checkbox1.setChecked(False)
    def condition_two(self):
        answer = self.line_edit.text().strip()
        if "@" in answer:
            self.checkbox2.setStyleSheet("color: green;")
            self.checkbox2.setChecked(True)
        else:
            self.checkbox2.setStyleSheet("color: red;")

    def condition_three(self):
        answer = self.line_edit.text().strip()
        if ("0" in answer or "1" in answer or "2" in answer or "3" in answer or "4" in answer or
                "5" in answer or "6" in answer or "7" in answer or "8" in answer or "9" in answer):
            self.checkbox3.setStyleSheet("color: green;")
            self.checkbox3.setChecked(True)
        else:
            self.checkbox3.setStyleSheet("color: red;")

    def both_conditions_true(self):
        self.condition_three()
        answer = self.line_edit.text().strip()
        if 8 <= len(answer) <= 25  and ("@" in answer) and ("0" in answer or "1" in answer or "2" in answer
                             or "3" in answer or "4" in answer or "5" in answer or "6" in answer or
                                                         "7" in answer or "8" in answer or "9" in answer):
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

    def create_file(self):
        self.line_edit2.show()
        self.label.setGeometry(60, 30, 500, 80)
        self.small_label.setGeometry(90, 120, 500, 30)
        self.label.setText("Create a file to save your password.")
        self.save_button.setText("Create")
        self.small_label.show()
        self.small_label.setText("Create file path:")
        self.line_edit2.setGeometry(100, 160, 180, 30)
        self.line_edit2.setPlaceholderText("example 'file.text'")

        try:
            self.save_button.clicked.disconnect()
        except Exception:
            pass
        self.save_button.clicked.connect(self.save_file)


    def save_file(self):
            self.save_button.hide()
            self.cancel_button.hide()
            self.line_edit2.hide()
            self.small_label.hide()
            file_path = self.line_edit2.text().strip()
            with open(file_path, "w") as file:
                for x in range(5):
                    file_content = self.line_edit.text().strip()
                    file.write(f"{file_content}\n")
                self.label.setGeometry(60, 100, 500, 120)
                self.label.setText(f"File '{file_path}' has been created and its\ncontent appended"
                                   f" successfully😎.\nOpen IDE side bar to view.")


def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
if __name__ == '__main__':
    main()
