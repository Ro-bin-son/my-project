import sys
import time
import random
from PyQt5.QtCore import QTimer, QPropertyAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsColorizeEffect, QLineEdit, QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, 800, 600)
        self.setStyleSheet("background-color: hsl(124, 16%, 26%);")
        self.punchlines = [
            "Na you be the password wey unlock my happiness 🔑❤️.",
            "Even AI no fit predict how fine you dey.",
            "If love na exam, you don already score A+\n without try.",
            "You dey shine pass my laptop screen when\n brightness dey 100% ✨.",
            "The way you sabi me, e clear say na only you\n fit operate my heart system."
        ]
        self.label = QLabel("In today’s landscape, a majority of applications are automated\nor accessed by bots."
                            "Our platform, however, maintains a strict\npolicy against non-human interactions. "
                            "As part of our security\nprotocol, we require you to validate that you are indeed a\nhuman. "
                            "Kindly proceed with the verification.", self)
        self.button1 = QPushButton("Proceed", self)
        self.button2 = QPushButton("Cancel", self)
        self.lineEdit = QLineEdit(self)

        self.question_index = -1  # start before first question
        self.lineEdit.hide()

        self.initUI()

    def initUI(self):
        self.label.setGeometry(80, 50, 1000, 150)
        self.label.setStyleSheet("font-size: 25px; color: grey; font-family: sans-serif;")
        self.button1.setGeometry(150, 350, 200, 80)
        self.button2.setGeometry(500, 350, 200, 80)
        self.button1.setStyleSheet(
            "font-size: 30px;"
            "background-color: hsl(180, 38%, 17%);"
            "color: white;"
            "border-radius: 15px;"
        )
        self.button2.setStyleSheet(
            "font-size: 30px;"
            "background-color: hsl(180, 38%, 40%);"
            "color: white;"
            "border-radius: 15px;"
        )

        # initially hide the input box; will show later
        self.lineEdit.hide()

        # connect button
        self.button1.clicked.connect(self.on_click1)
        self.button2.clicked.connect(self.close_program)



    def on_click1(self):
        time.sleep(0.15)
        self.button1.setGeometry(170, 250, 500, 80)
        self.button1.setText("Loading..... please wait")
        self.label.setText("")
        self.button2.hide()
        self.lineEdit.hide()
        QTimer.singleShot(1000, self.start_questions)
        QTimer.singleShot(1000, lambda: self.lineEdit.show())
        QTimer.singleShot(1000, lambda: self.button1.show())

    def close_program(self):
        self.label.setText("Goodbye 👋")
        self.label.setGeometry(250, 220, 500, 150)
        self.label.setStyleSheet("font-size: 40px; color: lightgreen; font-family: sans-serif;")
        self.button1.hide()
        self.button2.hide()
        self.lineEdit.hide()
        QTimer.singleShot(1000, self.close)

    def start_questions(self):

        #show first question
        self.question_index = 0
        self.show_question()

    def show_question(self):
        # Ensure input + button hidden then show new
        self.button2.hide()
        question_text = ""
        placeholder = ""
        if self.question_index == 0:
            self.label.setGeometry(240, 100, 1000, 100)
            self.label.setStyleSheet("font-size: 30px; color: lightgreen; font-weight: bold;")
            question_text = "Who is your "
            placeholder = "Type his name here"

        elif self.question_index == 1:
            self.label.setGeometry(210, 100, 1000, 100)
            self.label.setStyleSheet("font-size: 30px; color: lightgreen; font-weight: bold;")
            question_text = "What is five plus two?"
            placeholder = "Type your answer"
        elif self.question_index == 2:
            self.label.setGeometry(190, 100, 1000, 100)
            self.label.setStyleSheet("font-size: 30px; color: lightgreen; font-weight: bold;")
            question_text = "What is your favorite color?\n (blue/green/red)"
            placeholder = "Type your color"
        self.label.setText(question_text)

        # show input and button after small delay so user can see question
        QTimer.singleShot(30, lambda: self.lineEdit.show())
        QTimer.singleShot(30, lambda: self.button1.show())

        # reconfigure lineEdit
        self.lineEdit.clear()
        self.lineEdit.setPlaceholderText(placeholder)
        self.lineEdit.setGeometry(220, 250, 300, 50)
        self.lineEdit.setStyleSheet(
            "font-size: 25px; background-color: hsl(180, 38%, 47%); color: white;"
        )

        # reconfigure button
        self.button1.setText("Send")
        self.button1.setGeometry(270, 380, 200, 70)
        self.button1.setStyleSheet(
            "background-color: hsl(180, 38%, 17%); border-radius: 15px; color: white; font-size: 30px;"
        )
        self.button1.setDisabled(False)

        try:
            self.button1.clicked.disconnect()
        except Exception:
            pass
        self.button1.clicked.connect(self.validate_answer)

    def validate_answer(self):
        user_input = self.lineEdit.text().strip().lower()
        correct = False
        # Depending on question_index, validate differently
        if self.question_index == 0:
            if user_input == "robinson" or user_input == "robin":
                correct = True
        elif self.question_index == 1:
            if user_input.isdigit() and int(user_input) == 7:
                correct = True
        elif self.question_index == 2:
            if user_input in ["blue", "green", "red"]:
                correct = True

        if correct:
            # sometimes show punchline instead of just "Correct"
            #if random.random() < 0.7:  # 70% chance for punchline
            msg = random.choice(self.punchlines)
            #else:
            #msg = "Correct ✅"
            self.label.setText(msg)
            self.label.setGeometry(150, 120, 1000, 80)
            self.label.setStyleSheet("font-size: 25px; color: lightgreen; font-weight: bold;")
            self.lineEdit.hide()
            self.button1.hide()
            #correct = False

            # After 1.5 seconds, go to next question (if any)
            QTimer.singleShot(3500, self.advance_or_finish)
        else:
            # wrong answer: blink + shake
            self.label.setText("Incorrect. Try again.")
            self.label.setStyleSheet("font-size: 30px; color: red; font-weight: bold;")
            self.label.setGeometry(220, 120, 300, 80)
            # blinking limited times
            self.blink_state = True
            self.blink_count = 0
            self.blink_timer = QTimer()
            self.blink_timer.timeout.connect(self.toggle_blink)
            self.blink_timer.start(280)

            # shake the input box
            from PyQt5.QtCore import QPropertyAnimation
            rect = self.lineEdit.geometry()
            anim = QPropertyAnimation(self.lineEdit, b"geometry")
            anim.setDuration(500)
            anim.setLoopCount(2)
            anim.setKeyValueAt(0, rect)
            anim.setKeyValueAt(0.25, rect.translated(-10, 0))
            anim.setKeyValueAt(0.5, rect.translated(10, 0))
            anim.setKeyValueAt(0.75, rect.translated(-10, 0))
            anim.setKeyValueAt(1, rect)
            anim.start()

    def toggle_blink(self):
        # blink only up to 4 full cycles
        if self.blink_count >= 2:
            self.blink_timer.stop()
            self.label.setText("")
            self.label.setStyleSheet("font-size: 35px; color: lightgreen; font-weight: bold;")
            QTimer.singleShot(100, self.show_question)

            return

        if self.blink_state:
            self.label.setStyleSheet("font-size: 30px; color: red; font-weight: bold;")
            QApplication.beep()  # 🔔 play system beep
        else:
            self.label.setStyleSheet("font-size: 30px; color: transparent; font-weight: bold;")

        self.blink_state = not self.blink_state
        self.blink_count += 1

    def advance_or_finish(self):
        # move to next question or finish
        if self.question_index < 2:
            self.question_index += 1
            # restore label geometry if needed
            self.label.setGeometry(150, 100, 1000, 100)
            self.show_question()
        else:
            # no more questions: final message
            self.label.setText("All done! Thank you for your\n cooperation.")
            self.label.setGeometry(170, 240, 800, 100)
            self.label.setStyleSheet("font-size: 30px;")
            self.lineEdit.hide()
            self.button1.hide()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
