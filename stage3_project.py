import sys
import time
import random
from PyQt5.QtCore import QTime, QTimer, Qt, QPoint, QEasingCurve
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QHBoxLayout, QWidget, QCheckBox
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtCore import QTimer, QPropertyAnimation
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout


def fade_in(check1):
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, 800, 700)
        self.setStyleSheet("background-color: hsl(124, 16%, 30%);")
        self.time_label = QLabel(self)
        self.label1 = QLabel(self)
        self.timer = QTimer()
        self.timer1 = QTimer()
        self.check1 = QCheckBox(self)
        self.check2 = QCheckBox(self)
        self.check3 = QCheckBox(self)
        self.label0 = QLabel(self)
        self.labelc = QLabel(self)
        # Widgets
        self.label = QLabel("We value your privacy and are committed to protecting "
                  "your\npersonal information. By using this application"
                  ", you agree that\nany data collected will be used"
                  " solely to improve your experience\nand enhance app"
                  " functionality. We do not sell, share, or\ndisclose"
                  " your information to third parties without your"
                  " consent.\nContinued use of the app means you accept"
                  " these terms and any\nfuture updates made to them. Click 'Got It' to" 
                  " continue or 'Cancel'\nto exit the application."
              ,
              self)

        # Punchlines
        self.punchlines = [
            "Correct✔\nYou are the password to unlock\n my happiness 🔑❤️.",
            "You are right✔\nEven AI cannot predict\nhow fine you are.",
            "Good✔\nIf love was an exam, you \n already score A+ without\n trying.",
            "That's correct✔\nYou shine more than my laptop\n screen when brightness is 100% ✨.",
            "Correct✔\nThe way you know me, it's clear\n that only you is fit to operate my\n heart system."
        ]

        # Questions (list of dicts for flexibility)
        self.questions = [
            {"q": "Who is y", "answers": ["robinson", "robin"], "placeholder": "Type his name here"},
            {"q": "How many elephant emojis do you\n see down here?\n  🐘🐇🐍🐘🦆🐤🐒🐘🐖🐘",
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
        self.label0 = QLabel(self)
        self.button0 = QPushButton("Got It", self)
        self.button00 = QPushButton("Cancel", self)

        self.button1 = QPushButton("Proceed", self)
        self.button2 = QPushButton("Cancel", self)
        self.lineEdit = QLineEdit(self)
        self.question_index = -1
        self.lineEdit.hide()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Time's is ticking🔽'")
        self.label.setGeometry(50, 130, 1000, 240)
        self.label1.setGeometry(0, 30, 700, 60)


        #self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Georgia", 28))
        #self.layout.addWidget(self.label1)
        # Word pool
        self.words = ["💖💖", "💖","🥰","💖" ]

        # Timer to trigger word change
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_magic_word)
        self.timer.start(30000)  # every 8 seconds


        # Keep references to animations
        self.animations = []

        # First call
        self.show_magic_word()

        self.label.setStyleSheet("font-size: 25px; color: grey; font-family: sans-serif;")

        self.button1.setGeometry(150, 450, 170, 70)
        self.button2.setGeometry(500, 450, 170, 70)
        self.button0.setGeometry(150, 450, 170, 70)
        self.button00.setGeometry(500, 450, 170, 70)
        self.button1.setStyleSheet("""
            QPushButton {
                font-size: 30px;
                background-color: hsl(180, 38%, 17%);
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: hsl(180, 38%, 19%);                
            }
        """)
        self.button2.setStyleSheet("""
                    QPushButton {
                        font-size: 30px;
                        background-color: hsl(180, 38%, 40%);
                        color: white;
                        border-radius: 15px;
                    }
                    QPushButton:hover {
                        background-color: hsl(180, 38%, 45%);                
                    }
                """)
        self.button0.setStyleSheet("""
                    QPushButton {
                        font-size: 30px;
                        background-color: hsl(180, 38%, 17%);
                        color: white;
                        border-radius: 15px;
                    }
                    QPushButton:hover {
                        background-color: hsl(180, 38%, 19%);                
                    }
                """)
        self.button00.setStyleSheet("""
                            QPushButton {
                              font-size: 30px;
                              background-color: hsl(180, 38%, 37%);
                              color: white;
                              border-radius: 15px;
                            }
                            QPushButton:hover {
                                background-color: hsl(180, 38%, 45%);                
                            }
                        """)

        # --- DO NOT call setLayout() on a QMainWindow ---
        # Keep using absolute geometry for everything (what your code currently does).
        # Ensure the time_label is parented and positioned manually:

        self.time_label.setParent(self)  # already the case, but explicit for clarity
        self.time_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.time_label.setGeometry(260, 560, 300, 50)
        self.time_label.setStyleSheet(
            "color: grey;"
            "font-size: 45px;"
        )

        self.button0.clicked.connect(self.shows)
        self.button00.clicked.connect(self.confirm_early_exit)



        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer1.timeout.connect(self.update_time)
        self.timer1.start(1000)
        self.update_time()
        self.button1.hide()
        self.button2.hide()

    def show_magic_word(self):
        word = random.choice(self.words)
        self.label1.setText(word)
        # Random color
        color = random.choice(["white", "yellow"]
)
        self.label1.setStyleSheet(f"color: {color};"
                                  "font-size: 40px;")

        # Fade animation
        opacity_effect = QGraphicsOpacityEffect()
        self.label1.setGraphicsEffect(opacity_effect)
        fade = QPropertyAnimation(opacity_effect, b"opacity")
        fade.setDuration(25000)
        fade.setStartValue(0)
        fade.setKeyValueAt(0.5, 1)
        fade.setEndValue(0)
        fade.start()

        # Slide animation
        slide = QPropertyAnimation(self.label1, b"pos")
        slide.setDuration(30000)
        slide.setEasingCurve(QEasingCurve.OutCubic)

        current_pos = self.label1.pos()
        width = self.width()
        y = current_pos.y()

        # Randomly decide: edge → center OR center → edge
        if random.choice([True, False]):
            # From edge → center
            if random.choice([True, False]):
                start = QPoint(-50, y) # from left
                end = QPoint(850, y)
            else:
                start = QPoint(800, y)  # from right
                end = QPoint(0, y)
        else:
            # From center → edge
            start = QPoint(250, y)
            if random.choice([True, False]):
                end = QPoint(1000, y)
            else:
                end = QPoint(0, y)

        slide.setStartValue(start)
        slide.setEndValue(end)
        slide.start()

        # Keep reference to avoid garbage collection
        self.animations = [fade, slide]

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


    #def on_process(self):
        #QTimer.singleShot(1500, self.on_click0)



    def shows(self):
        self.button0.setGeometry(150, 330, 500, 80)
        self.button0.setText("Loading..... chill kiasi mkuu😂")
        self.label.hide()
        self.button00.hide()
        self.button1.hide()
        self.button2.hide()
        self.lineEdit.hide()
        QTimer.singleShot(3000, lambda: (
        self.label.show(),
        self.label.setGeometry(40, 100, 800, 200),
        self.label.setText("In today’s landscape, a majority of applications are automated\n"
            "or accessed by bots. Our platform, however, maintains a strict\n"
            "policy against non-human interactions. As part of our security\n"
            "protocol, we require you to validate that you are indeed a\nhuman."
            " Kindly proceed with the verification."),
        self.button1.show(),
        self.button2.show(),
        self.button0.hide(),
        self.button00.hide()
        ))
        self.button1.clicked.connect(self.redirect)
        self.button2.clicked.connect(self.confirm_leaving)

    def redirect(self):
        self.label.hide()
        self.labelc.show()
        self.labelc.setGeometry(100, 130, 700, 50)
        self.labelc.setText("Wait while the server redirects you.😎")
        self.labelc.setStyleSheet("color: orange;"
                                  "font-size: 38px;")
        self.button1.hide()
        self.button2.hide()
        self.lineEdit.hide()
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
        QTimer.singleShot(3000, self.green_light)

    def green_light(self):
        self.labelc.setGeometry(100, 260, 700, 50)
        self.labelc.setText("Checking network configuration....")
        QTimer.singleShot(5000, self.lying)



    def lying(self):
        self.labelc.hide()
        self.label.show()
        self.button1.show()
        self.button1.setGeometry(120, 250, 600, 80)
        self.button1.setText("Checking if  is lying....")
        self.label.setText("Checking her mouth movement.")
        self.label.setGeometry(150, 350, 700, 50)
        self.label.setStyleSheet("color: orange;"
                                     "font-size: 20px;")

        self.button2.hide()
        self.lineEdit.hide()
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
        self.check1.setGeometry(250, 400, 800, 46)
        self.check2.setGeometry(250, 438, 800, 44)
        self.check3.setGeometry(250, 468, 800, 46)
        limit = 50
        user = 49
        QTimer.singleShot(3000, lambda: (
            self.check1.show(),
            self.button1.setGeometry(120, 250, 600, 80),
            fade_in(self.check1),
            self.check1.setText("Confirming her mouth movement..."),
            self.check1.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check1.setChecked(True) if user >= limit else self.check1.setChecked(False),),
        ))

        QTimer.singleShot(8000, lambda: (
            self.check2.show(),
            self.button1.setGeometry(120, 250, 600, 80),
            fade_in(self.check2),
            self.check2.setText("Checking to see her articulation..."),
            self.check2.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check2.setChecked(True))
        ))
        QTimer.singleShot(13000, lambda: (
            self.check3.show(),
            self.button1.setGeometry(120, 250, 600, 80),
            fade_in(self.check1),
            self.check3.setText("Checking her eye contact..."),

            self.check3.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check3.setChecked(True))
        ))

        self.label.setGeometry(150, 350, 700, 50)
        self.label.setStyleSheet("color: orange; font-size: 20px;")


        QTimer.singleShot(18000, self.cheating)


    def cheating(self):
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
        self.button1.setGeometry(120, 250, 600, 80)
        self.button1.setText("Checking if  is cheating....")
        self.label.setText("Checking her phone.")
        self.label.setGeometry(150, 350, 700, 50)
        self.label.setStyleSheet("color: orange;"
                                 "font-size: 20px;")
        self.button2.hide()
        self.lineEdit.hide()
        QTimer.singleShot(3000, lambda: (
            self.check1.show(),
            fade_in(self.check1),
            self.check1.setText("Confirming WhatsApp messages from her phone..."),
            self.check1.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check1.setChecked(True))
        ))

        QTimer.singleShot(8000, lambda: (
            self.check2.show(),
            fade_in(self.check2),
            self.check2.setText("Confirming Facebook chats..."),
            self.check2.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check2.setChecked(True))
        ))

        QTimer.singleShot(13000, lambda: (
            self.check3.show(),
            fade_in(self.check1),
            self.check3.setText("Checking inbox/outbox chats on her phone..."),
            self.check3.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check3.setChecked(True))
        ))

        QTimer.singleShot(18000, self.checking_her_heart)


    def checking_her_heart(self):
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
        self.button1.setGeometry(120, 250, 600, 80)
        self.button1.setText("Scrutinising  heart.....")
        self.label.setText("Checking her male friends.")
        self.label.setGeometry(150, 350, 700, 50)
        self.label.setStyleSheet("color: orange;"
                                 "font-size: 20px;")

        self.button2.hide()
        self.lineEdit.hide()
        QTimer.singleShot(3000, lambda: (
            self.check1.show(),
            fade_in(self.check1),
            self.check1.setText("Confirming who she talked to awhile ago..."),
            self.check1.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check1.setChecked(True))
        ))

        QTimer.singleShot(8000, lambda: (
            self.check2.show(),
            fade_in(self.check2),
            self.check2.setText("Analysing what they talked about ..."),
            self.check2.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check2.setChecked(True))
        ))

        QTimer.singleShot(12000, lambda: (
            self.check3.show(),
            fade_in(self.check1),
            self.check3.setText("Checking any sensitive interaction with her..."),
            self.check3.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check3.setChecked(True))
        ))

        QTimer.singleShot(16000, self.process_finished)


    def process_finished(self):
        self.label.clear()
        self.button1.clicked.disconnect()
        self.label.setGeometry(50, 150, 900, 180)
        self.button1.show()
        self.button1.setText("Okay")
        self.button1.setGeometry(310, 420, 150, 65)
        self.label.setText("We finished doing our analysis and we\ndid not"
                           " find any cases of cheating.\nProceed to answer the questions that\nfollow.")
        self.label.setStyleSheet("color: orange;"
                                 "font-size: 40px;")
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
        self.button2.hide()
        self.lineEdit.hide()
        self.button1.clicked.connect(self.on_click1)

    def on_click1(self):
        self.button1.clicked.disconnect()
        self.button0.hide()
        self.button1.setGeometry(150, 350, 500, 80)
        self.button1.setText("Loading..... please wait")
        self.label.setText("")
        self.button2.hide()
        self.lineEdit.hide()

        QTimer.singleShot(2000, self.start_questions)  # close after 3 sec

    def confirm_leaving(self):
        # Create a semi-transparent background box
        QApplication.beep()
        self.label.hide()
        self.button0.hide()
        self.button00.hide()
        self.button1.hide()
        self.button2.hide()
        self.popup = QWidget(self)
        self.popup.setGeometry(210, 200, 400, 200)
        self.popup.setStyleSheet("""
            background-color: grey;
            border-radius: 20px;
            border: 2px solid grey;
        """)
        self.popup.show()

        # The question label
        self.popup_label = QLabel("Are you sure you want to\nleave app?", self.popup)
        self.popup_label.setGeometry(-110, 30, 600, 90)
        self.popup_label.setStyleSheet("""
            color: white;
            font-size: 23px;
            font-weight: bold;
        """)
        self.popup_label.setAlignment(Qt.AlignCenter)
        self.popup_label.show()

        # "No" button
        self.no_button = QPushButton("No", self.popup)
        self.no_button.setGeometry(60, 140, 110, 50)
        self.no_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border-radius: 12px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        self.no_button.clicked.connect(self.cancel_exit)
        self.no_button.show()

        # "Confirm" button
        self.confirm_button = QPushButton("Confirm", self.popup)
        self.confirm_button.setGeometry(240, 140, 110, 50)
        self.confirm_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 12px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        self.confirm_button.clicked.connect(self.close_program)
        self.confirm_button.show()

    def cancel_exit(self):
        self.popup.hide()
        self.redirect()  # return to normal flow


    def confirm_early_exit(self):
        # Create a semi-transparent background box
        QApplication.beep()
        self.label.hide()
        self.button0.hide()
        self.button00.hide()
        self.button1.hide()
        self.button2.hide()
        self.popup = QWidget(self)
        self.popup.setGeometry(210, 200, 400, 200)
        self.popup.setStyleSheet("""
                    background-color: grey;
                    border-radius: 20px;
                    border: 2px solid grey;
                """)
        self.popup.show()
        # The question label So fast?
        self.popup_label = QLabel("So fast?🙄 Are you sure you\n want to leave app?" , self.popup)
        self.popup_label.setGeometry(-100, 30, 600, 90)
        self.popup_label.setStyleSheet("""
                    color: white;
                    font-size: 23px;
                    font-weight: bold;
                """)
        self.popup_label.setAlignment(Qt.AlignCenter)
        self.popup_label.show()

        # "No" button
        self.no_button = QPushButton("No", self.popup)
        self.no_button.setGeometry(60, 140, 110, 50)
        self.no_button.setStyleSheet("""
                    QPushButton {
                        background-color: #2ecc71;
                        color: white;
                        border-radius: 12px;
                        font-size: 21px;
                    }
                    QPushButton:hover {
                        background-color: #27ae60;
                    }
                """)
        self.no_button.clicked.connect(self.on_click0)
        self.no_button.show()

        # "Confirm" button
        self.confirm_button = QPushButton("Confirm", self.popup)
        self.confirm_button.setGeometry(240, 140, 110, 50)
        self.confirm_button.setStyleSheet("""
                    QPushButton {
                        background-color: #e74c3c;
                        color: white;
                        border-radius: 12px;
                        font-size: 21px;
                    }
                    QPushButton:hover {
                        background-color: #c0392b;
                    }
                """)
        self.confirm_button.clicked.connect(self.close_program)
        self.confirm_button.show()

    def close_program0(self):
        self.label.setText("You left too soon😏")
        self.label.setGeometry(160, 220, 500, 250)
        self.label.setStyleSheet("font-size: 50px; color: lightgreen; font-family: sans-serif;")
        self.button0.hide()
        self.button00.hide()
        self.lineEdit.hide()
        self.time_label.hide()
        QTimer.singleShot(4000, self.close)  # close after 3 sec


    def close_program(self):
        self.label.show()
        self.label.setText("Goodbye 👋")
        self.label.setGeometry(250, 220, 500, 250)
        self.label.setStyleSheet("font-size: 50px; color: lightgreen; font-family: sans-serif;")
        self.button1.hide()
        self.button2.hide()
        self.lineEdit.hide()
        self.time_label.hide()
        self.popup.hide()
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
        self.button1.setText("Submit")
        self.button1.setGeometry(270, 380, 200, 70)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: hsl(180, 38%, 17%);
                border-radius: 15px;
                color: white;
                font-size: 30px;
            }
            QPushButton:hover {
                background-color: hsl(180, 38%, 20%);                
            }
        """)

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

            # ⏳ Re-show the same question after 3.5 seconds
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
