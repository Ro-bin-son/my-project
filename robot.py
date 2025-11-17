import sys
import time
import random
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QHBoxLayout
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtCore import QTimer, QPropertyAnimation
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, 800, 600)
        self.setStyleSheet("background-color: hsl(124, 16%, 30%);")
        self.time_label = QLabel(self)
        self.timer = QTimer()

        # Punchlines
        self.punchlines = [
            "You are the password to unlock\n my happiness 🔑❤️.",
            "Even AI cannot predict\nhow fine you are.",
            "If love was an exam, you \n already score A+ without\n trying.",
            "You shine more than my laptop screen\n when brightness is 100% ✨.",
            "The way you know me, it's clear\n that only you is fit to operate my\n heart system."
        ]

        # Questions (list of dicts for flexibility)
        self.questions = [
            {"q": "Who is y", "answers": ["robinson", "robin"], "placeholder": "Type his name here"},
            {"q": "How many elephant emojis do you\n see down here?\n  🐘🐇🐍🐘🐕🐒🐘🐖🐘",
             "answers": ["4", "four"], "placeholder": "Type your answer"},
            {"q": "What is your favorite color?\n (blue/green/red)", "answers": ["blue", "green", "red"], "placeholder":
                "Type your color"},
            {"q": "Complete this: Love is ...?", "answers": ["sweet", "kind", "beautiful"],
             "placeholder": "Type your answer here"},
            {"q": "Do you like surprises? (yes/no)", "answers": ["yes", "no"], "placeholder": "Type yes or no"}
        ]
        # Shuffle the question order
        random.shuffle(self.questions)

        # Score counter
        self.score = 0

        # Widgets
        self.label = QLabel(
            "In today’s landscape, a majority of applications are automated\n"
            "or accessed by bots. Our platform, however, maintains a strict\n"
            "policy against non-human interactions. As part of our security\n"
            "protocol, we require you to validate that you are indeed a\nhuman."
            " Kindly proceed with the verification.",
            self
        )
        self.button1 = QPushButton("Proceed", self)
        self.button2 = QPushButton("Cancel", self)
        self.lineEdit = QLineEdit(self)
        self.question_index = -1
        self.lineEdit.hide()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Time's is ticking🔽'")
        self.label.setGeometry(80, 100, 1000, 150)
        self.label.setStyleSheet("font-size: 25px; color: grey; font-family: sans-serif;")

        self.button1.setGeometry(150, 410, 170, 70)
        self.button2.setGeometry(500, 410, 170, 70)
        self.button1.setStyleSheet(
            "font-size: 30px; background-color: hsl(180, 38%, 17%); color: white; border-radius: 15px;"
        )
        self.button2.setStyleSheet(
            "font-size: 30px; background-color: hsl(180, 38%, 40%); color: white; border-radius: 15px;"
        )
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.time_label.setGeometry(230, 40, 300, 40)
        self.time_label.setStyleSheet("color: grey;"
                                      "font-size: 45px;"
                                      )

        self.button1.clicked.connect(self.on_click1)
        self.button2.clicked.connect(self.close_program)


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

    def on_click1(self):
        self.button1.setGeometry(150, 350, 500, 80)
        self.button1.setText("Loading..... please wait")
        self.label.setText("")
        self.button2.hide()
        self.lineEdit.hide()

        QTimer.singleShot(1500, self.start_questions)

    def close_program(self):
        self.label.setText("Goodbye 👋")
        self.label.setGeometry(250, 220, 500, 250)
        self.label.setStyleSheet("font-size: 50px; color: lightgreen; font-family: sans-serif;")
        self.button1.hide()
        self.button2.hide()
        self.lineEdit.hide()
        self.time_label.hide()
        QTimer.singleShot(2000, self.close)  # close after 3 sec
        
    def start_questions(self):
        self.question_index = 0
        self.show_question()

    def show_question(self):
        self.button2.hide()
        question = self.questions[self.question_index]
        self.label.setGeometry(150, 100, 1000, 100)
        self.label.setStyleSheet("font-size: 30px; color: lightgreen; font-weight: bold;")
        self.label.setText(question["q"])

        self.lineEdit.clear()
        self.lineEdit.setPlaceholderText(question["placeholder"])
        self.lineEdit.setGeometry(220, 250, 300, 50)
        self.lineEdit.setStyleSheet(
            "font-size: 25px; background-color: hsl(180, 38%, 47%); color: white;"
        )

        self.lineEdit.show()
        self.button1.show()
        self.button1.setText("Send")
        self.button1.setGeometry(270, 380, 200, 70)
        self.button1.setStyleSheet(
            "background-color: hsl(180, 38%, 17%); border-radius: 15px; color: white; font-size: 30px;"
        )

        try:
            self.button1.clicked.disconnect()
        except Exception:
            pass
        self.button1.clicked.connect(self.validate_answer)

    def validate_answer(self):
        user_input = self.lineEdit.text().strip().lower()
        correct_answers = self.questions[self.question_index]["answers"]

        if user_input in correct_answers:
            self.score += 1
            msg = random.choice(self.punchlines)
            self.label.setText(msg)
            self.label.setGeometry(150, 120, 1000, 380)
            self.label.setStyleSheet("font-size: 35px; color: lightgreen; font-weight: bold;")
            self.lineEdit.hide()
            self.button1.hide()
            QTimer.singleShot(2500, self.advance_or_finish)
        else:

            if user_input == "":
                self.label.setText("You did not write anything.")
            else:
                self.label.setText("Incorrect. Try again.")
            self.label.setStyleSheet("font-size: 30px; color: red; font-weight: bold;")
            self.label.setGeometry(200, 80, 650, 80)

            # 🔔 start blink animation
            self.blink_state = True
            self.blink_count = 0
            self.blink_timer = QTimer()
            self.blink_timer.timeout.connect(self.toggle_blink)
            self.blink_timer.start(1400)

            # blink speed
            self.shake_input()

            # ⏳ Re-show the same question after 2 seconds
            QTimer.singleShot(3500, self.show_question)

    def toggle_blink(self):
         #blink only up to 4 full cycles
        if self.blink_count >= 2:
            self.blink_timer.stop()
            self.label.setText("")
            self.label.setStyleSheet("font-size: 35px; color: lightgreen; font-weight: bold;")
            QTimer.singleShot(0, self.show_question)

            return


        if self.blink_state:
            self.label.setStyleSheet("font-size: 30px; color: red; font-weight: bold;")
            QApplication.beep()  # 🔔 play system beep
        else:
            self.label.setStyleSheet("font-size: 30px; color: transparent; font-weight: bold;")
        self.blink_state = not self.blink_state
        self.blink_count += 1

    def shake_input(self):
        from PyQt5.QtCore import QPropertyAnimation
        rect = self.lineEdit.geometry()
        self.anim = QPropertyAnimation(self.lineEdit, b"geometry")
        self.anim.setDuration(500)
        self.anim.setLoopCount(2)
        self.anim.setKeyValueAt(0, rect)
        self.anim.setKeyValueAt(0.25, rect.translated(-10, 0))
        self.anim.setKeyValueAt(0.5, rect.translated(10, 0))
        self.anim.setKeyValueAt(0.75, rect.translated(-10, 0))
        self.anim.setKeyValueAt(1, rect)
        self.anim.start()
        # 🔴 Add red border flash effect
        self.lineEdit.setStyleSheet(
            "font-size: 25px; background-color: hsl(180, 38%, 47%); "
            "color: white; border: 3px solid red; border-radius: 5px;"
        )
    def advance_or_finish(self):
        if self.question_index < len(self.questions) - 1:
            self.question_index += 1
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.label.setGeometry(100, 240, 800, 150)
        if self.score == len(self.questions):
            msg = f"Perfect! 🎉 You scored {self.score}/{len(self.questions)}\n{random.choice(self.punchlines)}"
        else:
            msg = f"Finished! ✅ You scored {self.score}/{len(self.questions)}"
        self.label.setText(msg)
        self.lineEdit.hide()
        self.button1.hide()
        self.time_label.hide()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
