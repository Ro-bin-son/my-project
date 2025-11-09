import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("     Do you love Robinson?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(60,40, 500,200)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "color: red;"
                                    ""
                                    "font-family: sans-serif;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("Yes,you do.")
        else:
            print("No,you don't.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
