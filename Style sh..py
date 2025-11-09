import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("B1")
        self.button2 = QPushButton("B2")
        self.button3 = QPushButton("B3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
                        QPushButton {
                        font-size: 40px;
                        border-radius: 15px;
                        font-family: arial;
                        margin: 25px;
                        padding: 15px 75px;
                        border: 3px solid;
                        }
                      QPushButton#button1 {
                            background-color: hsl(0, 75%, 54%);
                            }
                      QPushButton#button2 {
                            background-color: hsl(136, 75%, 32%);
                            }
                      QPushButton#button3 {
                            background-color: hsl(247, 83%, 45%);
                            }
                      QPushButton#button1:hover {
                            background-color: hsl(0, 65%, 54%);
                            }
                      QPushButton#button2:hover {
                            background-color: hsl(136, 75%, 37%);
                            }
                      QPushButton#button3:hover {
                            background-color: hsl(247, 80%, 50%);
                            }
                      }
                        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
