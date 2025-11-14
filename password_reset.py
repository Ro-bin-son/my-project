import sys
from PyQt5.QtCore import QTimer, QPropertyAnimation
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton, QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Interface")
        self.setGeometry(1200, 150, 500, 600)
        self.setStyleSheet("background-color:grey;")
        self.label = QLabel("Please fill out the fields and get started", self)
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.label1 = QLabel("Email required:", self)
        self.label2 = QLabel("Password required:", self)
        self.submit_button = QPushButton("Submit",self)
        self.initUI()

    def initUI(self):
       self.label.setGeometry(40, 10, 550, 50)
       self.label1.setGeometry(130, 100, 120, 20)
       self.label2.setGeometry(130, 220, 120, 20)
       self.line_edit1.setGeometry(120, 130, 250, 30)
       self.line_edit2.setGeometry(120, 250, 250, 30)
       self.submit_button.setGeometry(80, 340, 340, 40)
       self.label.setStyleSheet("color:white;"
                                "font-size:25px;")



    def shaking_effect(self):
        ### 1️⃣ SHAKE EFFECT
        rect = self.lineEdit.geometry()
        self.anim_shake = QPropertyAnimation(self.lineEdit, b"geometry")
        self.anim_shake.setDuration(400)
        self.anim_shake.setLoopCount(1)
        self.anim_shake.setKeyValueAt(0, rect)
        self.anim_shake.setKeyValueAt(0.25, rect.translated(-5, 0))
        self.anim_shake.setKeyValueAt(0.5, rect.translated(5, 0))
        self.anim_shake.setKeyValueAt(0.75, rect.translated(-5, 0))
        self.anim_shake.setKeyValueAt(1, rect)
        self.anim_shake.start()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
