import sys
import time
import random
from PyQt5.QtCore import QTime, QTimer, Qt, QPoint, QEasingCurve
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QHBoxLayout, QWidget
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtCore import QTimer, QPropertyAnimation
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setWindowTitle("Small Magic ✨")
        self.setGeometry(500, 200, 1100, 600)

        # Central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.central_widget.setLayout(self.layout)

        # Magic label
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Georgia", 28))
        self.layout.addWidget(self.label)
        # Word pool
        self.words = ["", "R", "P", "R", "S"]
        # Timer to trigger word change
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_magic_word)
        self.timer.start(8000)  # every 8 seconds


        # Keep references to animations
        self.animations = []
        # First call
        self.show_magic_word()

    def show_magic_word(self):
        word = random.choice(self.words)
        self.label.setText(word)
        # Random color
        color = random.choice(["#ff6b6b", "#6bafff", "#feca57", "#ff9ff3", "#48dbfb", "#5352ed"])
        self.label.setStyleSheet(f"color: {color};")

        # Fade animation
        opacity_effect = QGraphicsOpacityEffect()
        self.label.setGraphicsEffect(opacity_effect)
        fade = QPropertyAnimation(opacity_effect, b"opacity")
        fade.setDuration(4000)
        fade.setStartValue(0)
        fade.setKeyValueAt(0.5, 1)
        fade.setEndValue(0)
        fade.start()

        # Slide animation
        slide = QPropertyAnimation(self.label, b"pos")
        slide.setDuration(6000)
        slide.setEasingCurve(QEasingCurve.OutCubic)

        current_pos = self.label.pos()
        width = self.width()
        y = current_pos.y()

        # Randomly decide: edge → center OR center → edge
        if random.choice([True, False]):
            # From edge → center
            if random.choice([True, False]):
                start = QPoint(-50, y) # from left
                end = QPoint(550 , y)

            else:
                start = QPoint(800, y)  # from right
                end = QPoint(10 , y)
        else:
            # From center → edge
            start = QPoint(550 , y)
            if random.choice([True, False]):
                end = QPoint(1000, y)
            else:
                end = QPoint(0 , y)

        slide.setStartValue(start)
        slide.setEndValue(end)
        slide.start()

        # Keep reference to avoid garbage collection
        self.animations = [fade, slide]


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
