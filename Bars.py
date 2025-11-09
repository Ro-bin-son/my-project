import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow,QLabel,
                             QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Russia", self)
        label2 = QLabel("China", self)
        label3 = QLabel("Brazil", self)
        label4 = QLabel("United\nStates", self)
        label5 = QLabel("France", self)
        label6 = QLabel("Germany", self)
        labels = [label1, label2, label3, label4, label5, label6]
        for label in labels:
            label.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet("background-color: hsl(0, 50%, 25%);"
                             "font-style: italic;"
                             "font-size: 30px;"
                             "border-radius: 15px;")

        label2.setStyleSheet("background-color: hsl(300, 50%, 40%);"
                             "font-style: italic;"
                             "font-size: 30px;"
                             "border-radius: 15px;")
        label3.setStyleSheet("background-color:hsl(240, 50%, 40%);"
                             "font-style: italic;"
                             "font-size: 30px;"
                             "border-radius: 15px;")
        label4.setStyleSheet("background-color:hsl(120, 50%, 25%);"
                             "font-style: italic;"
                             "font-size: 30px;"
                             "border-radius: 15px;")
        label5.setStyleSheet("background-color:hsl(40, 50%, 25%);"
                             "font-style: italic;"
                             "font-size: 30px;"
                             "border-radius: 15px;")
        label6.setStyleSheet("background-color:hsl(270, 50%, 25%);"
                             "font-style: italic;"
                             "font-size: 30px;"
                             "border-radius: 15px;")



        #vbox = QVBoxLayout()
        #vbox.addWidget(label1)
        #vbox.addWidget(label2)
        #vbox.addWidget(label3)
        #vbox.addWidget(label4)
        #vbox.addWidget(label5)
        #central_widget.setLayout(vbox)

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 1, 1)
        grid.addWidget(label6, 1, 2)
        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
