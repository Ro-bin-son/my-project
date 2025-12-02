import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 150, 900, 800)
        self.label = QLabel("Do you like Samsung Galaxy A1Os", self)
        self.button = QPushButton("Yes", self)
        self.initUI()

    def initUI(self):
        self.label.setGeometry(80, 100, 600, 100)
        self.label.setStyleSheet("font-size: 40px;")
        self.button.setGeometry(150, 300, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.label.setGeometry(80, 100, 700, 100)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.button.setText("Confirmed")
        self.label.setText("Thank you.😎")
        self.button.setDisabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()          
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
