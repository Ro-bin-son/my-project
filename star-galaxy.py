import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PROJECT1_@g")
        self.setGeometry(500, 150, 800, 800)
        label1 = QLabel("Welcome to the platform😎" , self)
        label2 = QLabel("Sign in to continue", self)
        label3 = QLabel("Sign in", self)
        label4 = QLabel("Cancel", self)
        label1.setGeometry(0, 0, 800, 100)
        label2.setGeometry(60, 150, 800, 150)
        label3.setGeometry(100, 400, 120, 45)
        label4.setGeometry(450, 400, 120, 45)
        label1.setFont(QFont("Arial", 20))
        label2.setFont(QFont("Arial", 20))
        label3.setFont(QFont("Arial", 30))
        label4.setFont(QFont("Arial", 30))
        self.setStyleSheet("background-color: hsl(124, 16%, 26%);")
        label1.setStyleSheet("color: white;"
                            "background-color: hsl(180, 38%, 17%);"
                            #"font-weight: bold;"
                            #"font-style: italic;"
                            "font-size: 30px;"
                            #"text-decoration: underline;"#
                            "")
        label3.setStyleSheet("color: white;"
                             "background-color: hsl(180, 38%, 17%);"
                             "font-size: 30px;"
                             "border-radius: 10px;"
         
                             "")

        label4.setStyleSheet("color: white;"
                             #"background-color: hsl(180, 8%, 30%);"
                             "font-size: 30px;"
                             "border-radius: 10px;"

                             "")
        label1.setAlignment(Qt.AlignVCenter  | Qt.AlignHCenter)
        #label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)
        label4.setAlignment(Qt.AlignCenter)


        #label.setAlignment(Qt.AlignCenter)
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignHCenter)
        #label.setAlignment(Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignHCenter  | Qt.AlignTop)
        #label.setAlignment(Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignHCenter  | Qt.AlignTop)





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
