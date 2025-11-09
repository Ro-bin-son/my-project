from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, Qt
from PyQt5.QtGui import QColor, QPalette
import sys

class HoverButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
            QPushButton {
                background-color: hsl(180, 38%, 17%);
                border-radius: 15px;
                color: white;
                font-size: 30px;
            }
        """)
        self.default_color = QColor(18, 73, 73)   # hsl(180, 38%, 17%)
        self.hover_color = QColor(35, 100, 100)   # hsl(180, 38%, 27%)
        self.anim = QPropertyAnimation(self, b"color")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)

    def enterEvent(self, event):
        self.animate_color(self.default_color, self.hover_color)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animate_color(self.hover_color, self.default_color)
        super().leaveEvent(event)

    def animate_color(self, start, end):
        # Apply color change through stylesheet
        self.anim.stop()
        self.anim = QPropertyAnimation(self, b"")
        self.anim.setDuration(200)
        self.anim.valueChanged.connect(lambda: self.update_color(end))
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: rgb({end.red()}, {end.green()}, {end.blue()});
                border-radius: 15px;
                color: #feca57;
                font-size: 30px;
            }}
        """)

    def update_color(self, color):
        # This can be used to blend colors if you want a smoother gradient later
        pass


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animated Hover Button")
        layout = QVBoxLayout()

        self.button1 = HoverButton("Hover Me 😎")
        layout.addWidget(self.button1, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.resize(400, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
