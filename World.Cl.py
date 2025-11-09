import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.label = QLabel("-----THE STAR-GALAXY UPDATES-----", self)

        self.timer = QTimer()

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(400, 400, 1100, 500)
        self.label.setGeometry(150, 70, 950, 100)
        self.label.setStyleSheet("font-size: 40px;"
                                 "color: green;"
                                 "font-weight: bold;")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.time_label.setStyleSheet("color: purple;"
                                      "font-size: 150px;"
                                      )
        self.setStyleSheet("background-color:black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)


        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

