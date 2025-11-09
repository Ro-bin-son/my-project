import sys
import time
import random
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QGraphicsOpacityEffect

from PyQt5.QtCore import QTime, QTimer, Qt, QPoint, QEasingCurve
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QHBoxLayout, QWidget, QCheckBox
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtCore import QTimer, QPropertyAnimation
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout
import animation


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1180, 90, 670, 840)
        self.label = QLabel(self)
        self.intro_label = QLabel(self)
        self.instruction_label = QLabel(self)
        self.instruction_label = QLabel("Choose your attempts (50 – 100) and press\n‘Record’ to record and start Game", self)
        self.creator_label = QLabel("Developed by Robin",self)
        self.maximum_attempts_label = QLabel("Selected\nAttempts:", self)
        self.attempts_so_far_label = QLabel("Attempts\nUsed:", self)
        self.remaining_attempts_label = QLabel("Attempts\nRemaining:", self)
        self.maximum_attempts_button = QPushButton("", self)
        self.attempts_so_far_button = QPushButton("", self)
        self.remaining_attempts_button = QPushButton("", self)
        self.record_button = QPushButton("Record", self)
        self.popup = QWidget(self)
        self.popup_label = QLabel(self)
        self.manual_mode_label = QLabel(self)
        self.automatic_mode_label = QLabel(self)
        self.no_button =QPushButton(self)
        self.confirm_button =QPushButton(self)
        self.manual_button =QPushButton(self)
        self.automatic_button = QPushButton(self)
        self.okay_button = QPushButton("Okay", self)
        self.num_of_matched_buttons = QPushButton(self)
        self.num_of_matched_buttonsL = QPushButton(self)
        self.num_of_matched_label = QLabel(self)
        self.num_of_matched_labelL = QLabel(self)
        self.all_matched_label = QLabel(self)
        self.all_matched_button =QPushButton(self)
        self.prize_label = QLabel(self)
        self.prize_button = QPushButton(self)
        self.loading_button = QPushButton(self)
        self.loading_button1 = QPushButton(self)
        self.developers_wallet_label = QLabel(self)
        self.developers_wallet_button = QPushButton(self)
        self.total_users_button = QPushButton(self)
        self.total_users_label = QLabel(self)
        self.total_amount_button = QPushButton(self)
        self.total_amount_label = QLabel(self)
        self.amount_cashed_out_label = QLabel(self)
        self.amount_cashed_out_button = QPushButton(self)
        self.users_remaining_button = QPushButton(self)
        self.users_remaining_label = QLabel(self)



        self.check1 = QCheckBox(self)
        self.check2 = QCheckBox(self)
        self.check3 = QCheckBox(self)
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)
        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.proceed_button = QPushButton("Proceed", self)
        self.cancel_button = QPushButton("Cancel", self)
        self.lineEdit = QLineEdit(self)
        self.credentials_label = QLabel(self)
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.line_edit1_label = QLabel("Your name:", self)
        self.line_edit2_label = QLabel("Your password:", self)
        self.allow_button = QPushButton(self)
        self.matched_buttons = 0
        self.matched_buttonsL = 0
        self.all_matched = 0
        self.rating_label = QLabel(self)
        self.rating_button = QPushButton(self)
        self.maximum_attempts = 0
        self.attempts_used = 0
        self.remaining_attempts = 0
        self.number_of_rounds = 0
        self.automation_timer = QTimer(self)
        self.automation_timer.timeout.connect(self.automatic_click)

        self.initUI()


    def initUI(self):
        self.total_users_button.hide()
        self.total_users_label.hide()
        self.total_amount_button.hide()
        self.total_amount_label.hide()
        self.amount_cashed_out_label.hide()
        self.amount_cashed_out_button.hide()
        self.users_remaining_button.hide()
        self.users_remaining_label.hide()

        self.loading_button.hide()
        self.loading_button1.hide()
        self.developers_wallet_button.hide()
        self.developers_wallet_label.hide()
        self.prize_label.hide()
        self.prize_button.hide()
        self.rating_label.hide()
        self.rating_button.hide()
        self.num_of_matched_labelL.hide()
        self.num_of_matched_buttonsL.hide()
        self.num_of_matched_label.hide()
        self.num_of_matched_buttons.hide()
        self.all_matched_label.hide()
        self.all_matched_button.hide()
        self.line_edit1_label.hide()
        self.line_edit2_label.hide()
        self.allow_button.hide()
        credentials =[self.credentials_label, self.line_edit1, self.line_edit2]
        for field in credentials:
            field.hide()
        mode_labels = [self.manual_mode_label, self.automatic_mode_label]
        for label in mode_labels:
            label.hide()
        for w in (self.check1, self.check2, self.check3, self.okay_button):
            w.hide()
        self.hide_staffs()
        self.setWindowTitle("HIGH SPEED SEEK GAME💀💀")
        self.label.setGeometry(115, 10, 500, 55)
        self.instruction_label.setGeometry(215, 10, 500, 55)
        self.creator_label.setGeometry(520, 790, 500, 55)
        self.proceed_button.setGeometry(130, 450, 130, 50)
        self.cancel_button.setGeometry(410, 450, 130, 50)
        self.maximum_attempts_button.setGeometry(35, 230, 60, 27)
        self.attempts_so_far_button.setGeometry(200, 230, 60, 27)
        self.remaining_attempts_button.setGeometry(365, 230, 60, 27)
        self.maximum_attempts_label.setGeometry(25, 180, 90, 45)
        self.attempts_so_far_label.setGeometry(189, 180, 90, 42)
        self.remaining_attempts_label.setGeometry(355, 180, 90, 42)
        self.intro_label.setGeometry(40, 40, 800, 300)

        self.proceed_button.setStyleSheet("font-size: 25px;" "color: grey;" "background-color: hsl(180, 38%, 17%)")

        self.cancel_button.setStyleSheet("font-size: 25px;" "color: grey;" "background-color: hsl(180, 38%, 29%)")


        self.intro_label.setStyleSheet("font-size: 28px;" "color: grey;")
        self.creator_label.setStyleSheet("font-size: 14px;" "color: grey;")

        self.instruction_label.setStyleSheet("font-size: 20px;" "color: white;")

        self.maximum_attempts_label.setStyleSheet("font-size: 17px;"  "color: grey;")

        self.attempts_so_far_label.setStyleSheet("font-size: 17px;"  "color: grey;")

        self.remaining_attempts_label.setStyleSheet("font-size: 17px;"  "color: grey;")
        self.maximum_attempts_button.setStyleSheet("font-size: 20px;"   "color: grey;")
        self.remaining_attempts_button.setStyleSheet("font-size: 20px;"  "color: grey;")
        self.attempts_so_far_button.setStyleSheet("font-size: 20px;" "color: grey;")

        self.lineEdit.setGeometry(210, 70, 250, 40)
        self.lineEdit.setPlaceholderText("Type your number here (1 - 100)")
        self.lineEdit.setStyleSheet("font-size:16px;"  "background-color: grey;"   "border-radius: 1px;" "font-family:sans-serif;"
                                    )

        self.button1.setGeometry(95, 365, 90, 190)
        self.button2.setGeometry(275, 365, 90, 190)
        self.button3.setGeometry(455, 365, 90, 190)
        self.button4.setGeometry(95, 590, 90, 190)
        self.button5.setGeometry(275, 590, 90, 190)
        self.button6.setGeometry(455, 590, 90, 190)
        self.record_button.setGeometry(275, 130, 110, 40)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        self.button4.setObjectName("button4")
        self.button5.setObjectName("button5")
        self.button6.setObjectName("button6")
        self.record_button.setObjectName("record_button")

        self.setStyleSheet("""QMainWindow {
        
                               background-color: hsl(0, 0%, 25%);
                                 }
                               QPushButton {
                               font-size: 50px; font-family: arial; border: 2px solid; border-radius: 8px;
                               }
                             QPushButton#button1 {
                                   background-color: hsl(240, 50%, 34%);
                                   }
                             QPushButton#button2 {
                                   background-color: hsl(300, 50%, 34%);
                                   }
                             QPushButton#button3 {
                                   background-color: hsl(0, 50%, 25%);  
                                   }
                             QPushButton#button4 {
                                   background-color: hsl(120, 50%, 25%);   
                                   }
                             QPushButton#button5 {
                                   background-color: hsl(40, 50%, 25%);  
                                   }
                             QPushButton#button6 {
                                   background-color: hsl(270, 50%, 25%);  
                                   }
                             QPushButton#record_button{
                                   background-color: hsl(180, 38%, 17%);  font-size: 16px; border-style: solid; border-radius: 10px;
                                   color: white;
                                   }       
                             
                             QPushButton#button1:hover {
                                   background-color: hsl(240, 50%, 38%);
                                   }
                                   
                             QPushButton#button2:hover {
                                   background-color: hsl(300, 50%, 38%);
                                   }
                             QPushButton#button3:hover {
                                   background-color: hsl(0, 50%, 30%);
                                   }
                             QPushButton#button4:hover {
                                   background-color: hsl(120, 50%, 28%);
                                   }
                             QPushButton#button5:hover {
                                   background-color: hsl(40, 50%, 30%);
                                   }
                             QPushButton#button6:hover {
                                   background-color: hsl(270, 50%, 30%);
                                   } 
                             QPushButton#record_button:hover {
                                   background-color: hsl(180, 38%, 20%);
                                   }                    
                             }
                               """)
        # initial state
        self.maximum_attempts = 0
        self.attempts_used = 0
        self.remaining_attempts = 0
        self.automation_timer = QTimer(self)
        self.automation_timer.timeout.connect(self.automatic_click)





        # connect main navigation safely (disconnect first)
        try:
            self.proceed_button.clicked.disconnect()
        except Exception:
            pass
        self.proceed_button.clicked.connect(self.safe_instructions)

        try:
            self.cancel_button.clicked.disconnect()
        except Exception:
            pass
        self.cancel_button.clicked.connect(self.cancel_stage)

        # prepare mode button connections (but hide them until used)
        self.manual_button.clicked.connect(self.arranging_mechanics)
        self.intro()

        # ---------- safe wrappers that catch exceptions ----------
    def safe_instructions(self):
        try:
            self.allow_button.clicked.disconnect()

        except Exception:
            pass
        self.instructions()


    def safe_mode_selection(self):
        try:
            self.mode_selection()

        except Exception:
            pass

    def intro(self):
        self.manual_button.hide()
        self.automatic_button.hide()
        self.confirm_button.hide()
        self.no_button.hide()
        self.cancel_button.show()
        self.creator_label.setGeometry(520, 810, 150, 30)
        self.intro_label.setGeometry(40, 40, 800, 300)
        self.intro_label.setStyleSheet("font-size: 28px;" "color: grey;")

        self.intro_label.setText("Welcome to a game powered by probability,\nprecision, and pure machine intelligence."
                                 " Every\nmatch reveals a pattern."
                                 " You are about to enter\na live environment where results are recorded in\nreal time."
                                 " Click 'Proceed' to read instructions on\nhow to play or 'Cancel' to exit game.")
        self.hide_staffs()
        # ensure proceed is connected to the safe wrapper (no duplicates)
        #try:
            #self.proceed_button.clicked.disconnect()
        #except Exception:
            #pass
        #self.proceed_button.clicked.connect(self.entry_passkey_layout)
        self.proceed_button.clicked.connect(self.clicking)

    def entry_passkey_layout(self):
        self.line_edit1_label.show()
        self.line_edit2_label.show()
        self.proceed_button.hide()
        self.cancel_button.hide()
        self.allow_button.show()
        self.intro_label.hide()
        credentials = [self.credentials_label, self.line_edit1, self.line_edit2]
        for field in credentials:
            field.show()
        self.credentials_label.setText("Please fill out the following fields:")
        self.credentials_label.setStyleSheet("font-size: 24px;"
                                             "color: white;")
        self.line_edit1.setPlaceholderText("Enter your name here")
        self.line_edit1.setStyleSheet("font-size: 16px;"
                                      "color: white;"
                                      "background-color: black;")

        self.line_edit2.setPlaceholderText("Enter your password here")
        self.line_edit2.setStyleSheet("font-size: 16px;"
                                      "color: white;"
                                      "background-color: black;")


        self.allow_button.setText("Send")
        self.allow_button.setStyleSheet("font-size: 22px;"
                                      "color: white;"
                                      "background-color: green;")
        self.line_edit1_label.setStyleSheet("font-size: 17px;"
                                            "color: white;")
        self.line_edit2_label.setStyleSheet("font-size: 17px;"
                                            "color: white;")

        self.credentials_label.setGeometry(100, 40, 400, 40)
        self.line_edit1.setGeometry(140, 130, 400, 40)
        self.line_edit2.setGeometry(140, 230, 400, 40)
        self.allow_button.setGeometry(260, 450, 110, 50)
        self.line_edit1_label.setGeometry(140, 100, 110, 30)
        self.line_edit2_label.setGeometry(140, 200, 110, 30)
        self.clicking()


    def clicking(self):
        # ✅ IMPORTANT: now connect record_button here
        try:
            self.allow_button.clicked.disconnect()
        except:
            pass
        #self.allow_button.clicked.connect(self.verifier)  # ✅ Now recording runs ONLY after user clicks
        self.allow_button.clicked.connect(self.safe_instructions)  # ✅ Now recording runs ONLY after user clicks



    def verifier(self):
        name = self.line_edit1.text().strip()
        password = self.line_edit2.text().strip()
        # List of fields and their labels
        fields = [
            (self.line_edit1, self.line_edit1_label, name, "Name is required"),
            (self.line_edit2, self.line_edit2_label, password, "Password is required"),
        ]
        # Track if everything is valid
        all_valid = True

        for field, label, value, message in fields:
            if value == "":
                label.setStyleSheet("color: red;")
                label.setText(message)
                self.shaking(field)
                all_valid = False
            else:
                pass

        # If everything is valid, you can proceed here:
        if all_valid:
            self.allow_button.clicked.connect(self.safe_instructions)



    def shaking(self, widget):
        ### 1️⃣ SHAKE EFFECT
            rect = widget.geometry()
            animation = QPropertyAnimation(widget, b"geometry")
            animation.setDuration(400)
            animation.setLoopCount(1)
            animation.setKeyValueAt(0, rect)
            animation.setKeyValueAt(0.25, rect.translated(-5, 0))
            animation.setKeyValueAt(0.5, rect.translated(5, 0))
            animation.setKeyValueAt(0.75, rect.translated(-5, 0))
            animation.setKeyValueAt(1, rect)
            animation.start()
            # ✅ Keep reference alive
            if not hasattr(self, 'animations'):
                self.animations = []
            self.animations.append(animation)

    def instructions(self):
        self.credentials_label.hide()
        self.allow_button.hide()
        self.line_edit1_label.hide()
        self.line_edit2_label.hide()
        self.line_edit1.hide()
        self.line_edit2.hide()
        self.intro_label.show()
        self.proceed_button.show()
        self.cancel_button.show()
        self.intro_label.setStyleSheet("font-size: 20px;" "color: grey;")

        self.proceed_button.setText("Okay")
        self.proceed_button.setGeometry(130, 700, 130, 50)
        self.cancel_button.setGeometry(410, 700, 130, 50)
        self.intro_label.setGeometry(50, 25, 800, 660)
        self.intro_label.setText("1. You will choose your Mode\n       Manual Mode: You control the card draws one step at a time.\n"
                                   "       Automatic Mode: The machine runs rapidly on its own as you\n                                 "
                                  "observe.\n\n"
                                 "2. Enter Your Attempts\n       This is the total number of rounds the cards will be drawn.\n"
                                "       In Manual Mode, the number you will select is smaller (slower\n       gameplay, full control) while"
                                 " in Automatic Mode, the number is\n       larger (fast, machine-driven simulation).\n\n"
                                  "3. Card Matching Objective\n       Each round, six cards will display random numbers."
                                   " You are\n       trying to get matching numbers across multiple cards in the\n       same round."
                                   " Each successful match increases your score.\n\n"
                               "4. Winning Logic\n      The more matches you get before attempts run out, the higher\n      your success rate."
                                     " In Automatic Mode, results appear rapidly,\n      and statistics update in real time.\n\n"
                                     "5. Stay Sharp\n      The game is based on probability and streaks."
                                     " Matching patterns\n      may appear suddenly—especially during fast automatic mode!\n\n"
                                     "6. Your Goal\n      Observe how randomness behaves.")

        # connect proceed to mode selection safely
        try:
            self.proceed_button.clicked.disconnect()
        except Exception:
            pass
        self.proceed_button.clicked.connect(self.safe_mode_selection)

        # ensure cancel goes to cancel_stage
        try:
            self.cancel_button.clicked.disconnect()
        except Exception:
            pass
        self.cancel_button.clicked.connect(self.cancel_stage)

    def mode_selection(self):
        self.okay_button.hide()
        self.manual_button.show()
        self.automatic_button.show()
        self.proceed_button.hide()
        self.cancel_button.hide()
        self.intro_label.setText("Select to choose 'Manual' or 'Automatic'\nmode.")
        self.intro_label.setStyleSheet("font-size: 26px;"
                                       "color: white;")
        self.manual_button.setStyleSheet("font-size: 26px;"
                                         "color: white;"
                                         "background-color: hsl(30, 100%, 45%);")
        self.automatic_button.setStyleSheet("font-size: 26px;"
                                            "color: white;"
                                            "background-color: hsl(0, 100%, 34%);")
        self.intro_label.setGeometry(60, 60, 800, 70)
        self.manual_button.setText("Manual")
        self.automatic_button.setText("Automatic")
        self.manual_button.setGeometry(90, 350, 160, 50)
        self.automatic_button.setGeometry(410, 350, 160, 50)

        # make sure connections are not stacked
        try:
            self.manual_button.clicked.disconnect()
        except Exception:
            pass
        self.manual_button.clicked.connect(self.technicalities)

        try:
            self.automatic_button.clicked.disconnect()
        except Exception:
            pass
        #self.automatic_button.clicked.connect(self.production)
        self.automatic_button.clicked.connect(self.automatic_mode_layout)


    def technicalities(self):
        self.okay_button.show()
        self.manual_button.hide()
        self.automatic_button.hide()
        self.intro_label.setGeometry(60, 60, 800, 180)
        self.okay_button.setText("Okay")
        self.okay_button.setGeometry(280, 380, 100, 45)
        self.okay_button.setStyleSheet("font-size: 24px;"
                                       "color: white;"
                                       "background-color: red;")
        self.intro_label.setText("We are experiencing some technicalities on manual\nsystems. Our developers are working"
                                 " on it to restore\nits full operation. We will notify you"
                                 " once it is solved.\nMeanwhile, you can play in Automatic mode by\nclicking 'Automatic' button. Sorry for inconveniences\ncaused.")
        self.intro_label.setStyleSheet("color: orange;"
                                       "font-size: 25px;")

        try:
            self.okay_button.clicked.disconnect()
        except:
            pass
        self.okay_button.clicked.connect(self.mode_selection)


    def arranging_mechanics(self):
        try:
            self.automatic_button.clicked.disconnect()
        except Exception:
            pass
        self.manual_mode_label.show()
        self.hide_staffs()
        self.manual_button.hide()
        self.automatic_button.hide()
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
        self.check1.setGeometry(180, 260, 800, 46)
        self.check2.setGeometry(180, 300, 800, 44)
        self.check3.setGeometry(180, 340, 800, 46)
        self.intro_label.setText("Arranging Game Mechanics")
        self.intro_label.setGeometry(150, 200, 700, 50)
        self.intro_label.setStyleSheet("color: orange;"
                                       "font-size: 25px;")
        self.manual_mode_label.setStyleSheet("color: orange;")
        self.manual_mode_label.setText("Manual Mode")
        self.manual_mode_label.setGeometry(40, 30, 100, 30)
        self.check1.show(),
        self.check1.setText("Initializing button responsiveness....."),
        self.check1.setChecked(False),
        QTimer.singleShot(3000, lambda: self.check1.setChecked(False))

        QTimer.singleShot(8000, lambda: (
            self.check2.show(),
            self.check2.setText("Checking game engine configurations...."),
            self.check2.setChecked(False),
            QTimer.singleShot(3000, lambda: self.check2.setChecked(True))
        ))

        QTimer.singleShot(12000, lambda: (
            self.check3.show(),
            self.check3.setText("Initializing scores before game time..."),
            self.check3.setChecked(False),
            QTimer.singleShot(2000, lambda: self.check3.setChecked(False))

        ))
        try:
            self.record_button.clicked.disconnect()
        except Exception:
            pass
        QTimer.singleShot(15000, self.show_user_input_stage)



    def show_user_input_stage(self):
        self.num_of_matched_buttons.show()
        self.num_of_matched_label.show()
        self.num_of_matched_label.setGeometry(500, 180, 150, 42)
        self.num_of_matched_buttons.setGeometry(530, 230, 45, 27)
        self.num_of_matched_label.setStyleSheet("font-size: 17px;"
                                                "color: green;")
        self.num_of_matched_buttons.setStyleSheet("background-color: orange;"
                                                  "font-size: 19px;"
                                                  "color: black;")
        self.num_of_matched_label.setText("Number of times\nnumbers matchedU:")
        self.manual_mode_label.setGeometry(20, 75, 100, 30)
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
        self.show_staffs()
        self.intro_label.hide()
        self.instruction_label.show()
        self.instruction_label.setText("Enter attempts (50-100) then click 'Record' and\nstart game")
        # ✅ IMPORTANT: now connect record_button here
        try:
            self.record_button.clicked.disconnect()
        except:
            pass
        self.record_button.clicked.connect(self.recording)  # ✅ Now recording runs ONLY after user clicks


    def automatic_mode_layout(self):
        try:
            self.record_button.clicked.disconnect()
        except:
            pass
        try:
            self.manual_button.clicked.disconnect()
        except:
            pass
        self.total_users_button.show()
        self.total_users_label.show()
        self.total_amount_button.show()
        self.total_amount_label.show()
        self.amount_cashed_out_label.show()
        self.amount_cashed_out_button.show()
        self.users_remaining_button.show()
        self.users_remaining_label.show()
        self.developers_wallet_button.show()
        self.developers_wallet_label.show()
        self.rating_button.show()
        self.rating_label.show()
        self.prize_label.show()
        self.prize_button.show()
        self.num_of_matched_labelL.show()
        self.num_of_matched_buttonsL.show()
        self.num_of_matched_label.show()
        self.all_matched_label.show()
        self.all_matched_button.show()
        self.num_of_matched_buttons.show()
        self.num_of_matched_buttons.setText("0")
        self.num_of_matched_buttonsL.setText("0")
        self.all_matched_button.setText("0")
        self.prize_label.setText("Prize:")

        self.rating_label.setText("Status:")
        self.num_of_matched_labelL.setText("Lower matched(L):")
        self.num_of_matched_label.setText("Upper matched(U):")
        self.all_matched_label.setText("All numbers matched:")
        self.developers_wallet_label.setText("Dev. Balance(Ksh):")
        self.developers_wallet_button.setText("0.00")
        self.total_amount_label.setText("Total Amount(Ksh):")
        self.total_users_label.setText("Total Users:")
        self.users_remaining_label.setText("Active Users:")
        self.amount_cashed_out_label.setText("Amount Cashed Out:")

        self.intro_label.hide()
        self.total_users_label.setGeometry(470, 80, 150, 30)
        self.total_users_button.setGeometry(470, 110, 80, 25)

        self.users_remaining_label.setGeometry(570, 80, 150, 30)
        self.users_remaining_button.setGeometry(570, 110, 80, 25)
        self.developers_wallet_button.setGeometry(520, 40, 150, 30)
        self.developers_wallet_label.setGeometry(520, 0, 150, 50)
        self.total_amount_button.setGeometry(10, 50, 150, 30)
        self.total_amount_label.setGeometry(10, 10, 150, 50)

        self.amount_cashed_out_button.setGeometry(10, 130, 150, 30)
        self.amount_cashed_out_label.setGeometry(10, 100, 150, 30)

        self.prize_label.setGeometry(225, 290, 100, 30)
        self.prize_button.setGeometry(300, 298, 125, 23)
        self.rating_label.setGeometry(5, 290, 100, 30)
        self.rating_button.setGeometry(90, 298, 125, 23)
        self.num_of_matched_labelL.setGeometry(500, 210, 165, 42)
        self.num_of_matched_buttonsL.setGeometry(540, 250, 55, 27)
        self.num_of_matched_label.setGeometry(500, 140, 165, 42)
        self.num_of_matched_buttons.setGeometry(540, 180, 55, 27)
        self.all_matched_button.setGeometry(540, 320, 55, 27)
        self.all_matched_label.setGeometry(500, 280, 165, 42)

        self.prize_button.setText("0.00")

        self.developers_wallet_button.setStyleSheet("background-color: white;"
                                        "font-size: 22px;"
                                        "color: black;"
                                        "border-radius: 10px;")
        self.developers_wallet_label.setStyleSheet("font-size: 16px;"                                                   
                                                 "color: green;")
        self.total_amount_button.setStyleSheet("background-color: white;"
                                                    "font-size: 22px;"
                                                    "color: black;"
                                                    "border-radius: 10px;")
        self.total_amount_label.setStyleSheet("font-size: 16px;"
                                                   "color: green;")
        self.amount_cashed_out_button.setStyleSheet("background-color: white;"
                                               "font-size: 22px;"
                                               "color: black;"
                                               "border-radius: 10px;")
        self.amount_cashed_out_label.setStyleSheet("font-size: 16px;"
                                              "color: green;")

        self.total_users_button.setStyleSheet("background-color: white;"
                                               "font-size: 22px;"
                                               "color: black;"
                                               "border-radius: 10px;")
        self.total_users_label.setStyleSheet("font-size: 16px;"
                                              "color: green;")
        self.users_remaining_button.setStyleSheet("background-color: white;"
                                               "font-size: 22px;"
                                               "color: black;"
                                               "border-radius: 10px;")
        self.users_remaining_label.setStyleSheet("font-size: 16px;"
                                              "color: green;")

        self.prize_button.setStyleSheet("background-color: white;"
                                        "font-size: 22px;")
        self.prize_label.setStyleSheet("font-size: 22px;"
                                        "color: green;")
        self.rating_button.setStyleSheet("background-color: white;")

        self.rating_label.setStyleSheet("font-size: 22px;"
                                        "color: green;")

        self.num_of_matched_label.setStyleSheet("font-size: 17px;"
                                                "color: green;")

        self.num_of_matched_buttons.setStyleSheet("background-color: orange;"
                                                  "font-size: 19px;"
                                                  "color: black;")
        self.num_of_matched_labelL.setStyleSheet("font-size: 17px;"
                                                "color: green;")
        self.num_of_matched_buttonsL.setStyleSheet("background-color: orange;"
                                                  "font-size: 19px;"
                                                  "color: black;")
        self.all_matched_label.setStyleSheet("font-size: 17px;"
                                                 "color: green;")
        self.all_matched_button.setStyleSheet("background-color: orange;"
                                                   "font-size: 19px;"
                                                   "color: black;")

        self.automatic_mode_label.show()
        self.automatic_button.hide()
        self.manual_button.hide()
        self.show_staffs()
        self.lineEdit.hide()
        self.instruction_label.setText("Click 'Enter' to get into Game")
        self.record_button.setText("Enter")
        self.record_button.setStyleSheet("font-size: 22px;")
        self.automatic_mode_label.setText("Automatic Mode")
        self.automatic_mode_label.setGeometry(300, 0, 100, 30)
        self.automatic_mode_label.setStyleSheet("color: orange;")
        self.maximum_attempts_label.setText("Machine\nAttempts:")

        try:
            self.record_button.clicked.disconnect()
        except:
            pass
        self.record_button.clicked.connect(self.machine_attempts_picking)


    def machine_attempts_picking(self):
        self.instruction_label.show()
        self.instruction_label.setText("Please wait......")
        self.record_button.hide()
        self.instruction_label.setGeometry(200, 20, 700, 40)
        self.instruction_label.setStyleSheet("font-size: 24px;"
                                             "color: orange;")

        robot_number = random.randint(30000,45000)
        robot_str = str(robot_number)
        length = len(robot_str)
        self.maximum_attempts = robot_number
        self.remaining_attempts = robot_number
        self.attempts_used = 0

        QTimer.singleShot(2500, lambda: (
            self.users_update(),

            self.update_automated_attempts_display(),
            self.instruction_label.setStyleSheet("font-size: 24px;"                                                 
                                                 "color: orange;"),
            QTimer.singleShot(0, self.start_automatic_prep)


        ))
        try:
            self.record_button.clicked.disconnect()
        except:
            pass


    def start_automatic_prep(self):
        self.loading_button.show()
        self.loading_button1.show()
        self.loading_button1.setGeometry(235, 110, 110, 20)
        self.loading_button.setGeometry(320, 110, 120, 20)

        self.loading_button1.setStyleSheet("background-color: black;"
                                          "border-radius: 10px;"
                                          )

        self.loading_button.setStyleSheet("background-color: black;"
                                           "border-radius: 10px;")
        QTimer.singleShot(2000, lambda: (
            self.loading_button1.setStyleSheet("background-color: red;"),
        ))
        QTimer.singleShot(4000, lambda: (
            self.loading_button.hide(),
            self.loading_button1.setGeometry(235, 110, 205, 20),
            self.loading_button1.setStyleSheet("background-color: red;"),
        ))

        self.instruction_label.setText("Waiting for next round....")
        self.instruction_label.setStyleSheet("font-size: 24px;"
                                             "color: red;")
        self.record_button.hide()
        QTimer.singleShot(7000, lambda: (QTimer.singleShot(0, self.start_automation)))

    def start_automation(self):
        self.automation_timer.start(1)

    def automatic_click(self):
        self.instruction_label.setGeometry(180, 20, 700, 50)
        self.instruction_label.setStyleSheet("color: white;"
                                             "font-size: 25px;")
        self.instruction_label.setText("Automation in progress....")
        random_codes = ["1", "2", "3", "4", "5", "6"]
        cards = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6]
        for card in cards:
            card.setText(random.choice(random_codes))

        # Deduct an attempt
        if self.remaining_attempts > 0:
                self.attempts_used += 1
                self.remaining_attempts -= 1
                self.update_automated_attempts_display()
                self.prize_determinant()
                self.prize_layout_display()
                self.update_user_card()
                self.loading_button1.hide()

        elif self.remaining_attempts == 0:
            self.automation_timer.stop()
            self.instruction_label.setText("Automation Complete")
            self.instruction_label.setStyleSheet("color: white; font-size: 32px;")
            QTimer.singleShot(0, self.reset)




    def update_user_card(self):
        number1 = self.button1.text().strip()
        number2 = self.button2.text().strip()
        number3 = self.button3.text().strip()
        number4 = self.button4.text().strip()
        number5 = self.button5.text().strip()
        number6 = self.button6.text().strip()
        if number1 == number2 == number3:
            self.matched_buttons += 1
            self.num_of_matched_buttons.setText(str(self.matched_buttons))

        if number4 == number5 == number6:
            self.matched_buttonsL += 1
            self.num_of_matched_buttonsL.setText(str(self.matched_buttonsL))

        if number1 == number2 == number3 == number4 == number5 == number6:
            self.all_matched += 1
            self.all_matched_button.setText(str(self.all_matched))
            self.pause2()



    def prize_determinant(self):
        try:
            v1 = int(self.num_of_matched_buttonsL.text().strip() or 0)
            v2 = int(self.num_of_matched_buttons.text().strip() or 0)
            v3 = float(self.total_amount_button.text().replace(",", "").strip() or 0)
            v4 = float(self.amount_cashed_out_button.text().replace(",", "").strip() or 0)
            v5 = float(self.developers_wallet_button.text().replace(",", "").strip() or 0)

            x1 = self.button1.text().strip()
            x2 = self.button2.text().strip()
            x3 = self.button3.text().strip()
            x4 = self.button4.text().strip()
            x5 = self.button5.text().strip()
            x6 = self.button6.text().strip()

            if x1 == x2 == x3 == x4 == x5 == x6:
                new_tot = float(self.prize_button.text().strip() or 0)
                if x1 == "1":
                    try:
                        total = (new_tot + (v1 + (v2 + 1))) * 0.008
                    except Exception as e:
                        print(e)

                elif x1 == "3":
                    total = (new_tot + (v1 + (v2 + 1))) * 0.007

                elif x1 == "2":
                    total = (new_tot + (v1 + (v2 + 1))) * 0.005

                elif x1 == "4":
                    total = (new_tot + (v1 + (v2 + 1)) + 250) * 0.009

                elif x1 == "5":
                    total = new_tot - new_tot
                    self.prize_button.setText(f"{total:.2f}")

                self.prize_button.setText(f"{total:.2f}") if total < 0 else self.prize_button.setText(
                    f"+{total:.2f}")

                if x1 == "6":
                    self.trigger_liquidation()


            elif ((x1 == x2 == x3) or (x4 == x5 == x6)) and not (x1 == x2 == x3 == x4 == x5 == x6):
                prize_value = float(self.prize_button.text().strip() or 0)
                if x1 in ["1", "3"]:
                    total = prize_value - 3

                elif x1 == "6":
                    total = prize_value + 1

                elif x1 == "2":
                    total = prize_value + 0.01

                elif x1 in ["4", "5"]:
                    total = prize_value  # no change

                # ✅ single place to update the UI
                self.prize_button.setText(f"{total:.2f}" if total < 0 else f"+{total:.2f}")

            try:
                prize_value = float(self.prize_button.text().strip() or 0)
                all_cards = int(self.all_matched_button.text().strip() or 0)
                if (prize_value <= -500 and all_cards <= 3) or (prize_value <= -700 and  all_cards <= 6) :
                    self.trigger_liquidation()



            except ValueError as e:
                print(e)

        except:
            pass

    def reset_r(self):
        self.rating_button.setText("")



    def trigger_liquidation(self):
        self.automation_timer.stop()
        self.status_layout_display()
        self.instruction_label.setText("Liquidated")
        self.instruction_label.setGeometry(245, 100, 110, 35)
        self.instruction_label.setStyleSheet("""
            background-color: red;
            font-size: 24px;
            color: white;
            border-radius: 10px;
        """)
        QTimer.singleShot(3000, self.reset)
        return


    def prize_layout_display(self):
        xx = float(self.prize_button.text().strip())
        if xx < 0:
            self.prize_button.setStyleSheet("background-color: white;"
                                            "font-size: 22px;"
                                            "color: red;"
                                            "border-radius: 10px;")
        elif xx == 0:
            self.prize_button.setStyleSheet("background-color: white;"
                                            "font-size: 22px;"
                                            "color: black;"
                                            "border-radius: 10px;")

        else:
            self.prize_button.setStyleSheet("background-color: white;"
                                            "font-size: 22px;"
                                            "color: blue;"
                                            "border-radius: 10px;")

    def status_layout_display(self):
        """Handle liquidation or all-6 triggers safely."""
        try:
            vv = float(self.total_amount_button.text().replace(",", "").strip() or 0)
            zz = int(self.all_matched_button.text().replace(",", "").strip() or 0)
            xx = float(self.prize_button.text().replace(",", "").strip() or 0)
            m = float(self.developers_wallet_button.text().replace(",", "").strip() or 0)
            zzz = self.button1.text().strip()

            # Prevent double trigger in one pause
            if hasattr(self, "_triggered") and self._triggered:
                return
            self._triggered = True  # mark as triggered

            # 💀 Case 1: Liquidation when prize negative threshold reached
            if xx <= -500 and zz <= 6:
                cc = vv + m
                self.developers_wallet_button.setText(f"{cc:,.2f}")
                print("⚠️ Liquidation triggered (negative prize)")
                self.liquidation_type = "LOSS"

            # 💰 Case 2: All cards are '6' and prize still positive — special payout
            elif zzz == "6" and xx > 0 and zz <= 6:
                cc = vv + m
                self.developers_wallet_button.setText(f"{cc:,.2f}")
                print("💰 Jackpot! All cards = 6 trigger")
                self.liquidation_type = "JACKPOT"

        except Exception as e:
            print("Status layout error:", e)

    def reset(self):
        self.instruction_label.hide()

        def do_reset():

            self.instruction_label.setGeometry(200, 20, 700, 40 )
            self.instruction_label.setStyleSheet("font-size: 24px;"
                                                 "color: orange;")

            self.instruction_label.setText("Please wait......")
            # ✅ Reset internal game variables
            self.remaining_attempts = 0
            self.attempts_used = 0
            self.matched_buttons = 0
            self.matched_buttonsL = 0
            self.all_matched = 0
            self.total_amount_button.setText("0")
            self.total_users_button.setText("0")
            self.users_remaining_button.setText("0")
            self.amount_cashed_out_button.setText("0.00")

            # ✅ Reset UI values (everything except wallet)
            self.remaining_attempts_button.setText("0")
            self.num_of_matched_buttonsL.setText("0")
            self.num_of_matched_buttons.setText("0")
            self.all_matched_button.setText("0")
            self.attempts_so_far_button.setText("0")
            self.maximum_attempts_button.setText("0")

            self.prize_button.setText("0.00")
            self.prize_button.setStyleSheet("color: black;"
                                            "background-color: white;"
                                            "font-size: 22px;")
            self.rating_button.setText("")

            # ✅ CARD BUTTONS RESET
            for btn in [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6]:
                btn.setText("")
            QTimer.singleShot(2000, after_reset)

        def after_reset():
            self.record_button.hide()
            QTimer.singleShot(1500, self.machine_attempts_picking)

        QTimer.singleShot(0, do_reset)

    def pause2(self):
        """Pause automation safely, trigger logic, and resume after checks."""
        x_vals = [self.button1.text().strip(), self.button2.text().strip(),
                  self.button3.text().strip(), self.button4.text().strip(),
                  self.button5.text().strip(), self.button6.text().strip()]

        all_six = all(x == "6" for x in x_vals)

        self.instruction_label.setGeometry(230, 80, 700, 50)
        self.instruction_label.setStyleSheet("color: red; font-size: 25px;")
        self.automation_timer.stop()

        if all_six:
            self.instruction_label.setText("💥 All cards are 6 — Jackpot Triggered!")
        else:
            self.instruction_label.setText("Automation paused.")

        # Reset flags
        self._triggered = False
        self.liquidation_type = None

        # Perform safe updates
        self.prize_determinant()
        self.status_layout_display()
        QTimer.singleShot(200, self.reducing_users)

        # Resume smoothly
        QTimer.singleShot(4500, lambda: (
            self.automation_timer.start(1),
            self.reset_r(),
        ))

    def users_update(self):
        amount = random.choice([10, 20, 40, 50, 100, 200, 400, 500, 1000])
        players = random.choice([500, 800, 1000, 2000, 3000])
        tot_amount = amount * players
        self.total_users_button.setText(str(f"{players:,.0f}"))
        self.total_amount_button.setText(str(f"{tot_amount:,.0f}"))

    def reducing_users(self):
        """Reduce users gradually and handle balance logic properly."""
        try:
            total_users = int(self.total_users_button.text().replace(",", "").strip() or 0)
            users_remaining = int(self.users_remaining_button.text().replace(",", "").strip() or 0)
            amount = float(self.rating_button.text().replace(",", "").strip() or 0)
            prize_text = float(self.prize_button.text().replace(",", "").replace("+", "").strip() or 0)
            dev_wallet = float(self.developers_wallet_button.text().replace(",", "").strip() or 0)

            # Random batch of users leaving
            if users_remaining > 0:
                users_cashed_out = random.randint(1, max(1, users_remaining // 2))
                new_remaining = max(0, users_remaining - users_cashed_out)
                self.users_remaining_button.setText(f"{new_remaining:,.0f}")
            else:
                new_remaining = 0

            # 💰 When all users are done or timer ends:
            if new_remaining == 0:
                if prize_text > 0:
                    # Remaining users' money goes to wallet
                    added = total_users * amount
                    total = dev_wallet + added
                    self.developers_wallet_button.setText(f"{total:,.2f}")
                    print(f"🏁 Round ended — {added:,.2f} added to dev wallet")

            # 💀 If jackpot or liquidation triggered earlier
            elif getattr(self, "liquidation_type", None) in ["LOSS", "JACKPOT"]:
                # handled already by status_layout_display
                pass

        except Exception as e:
            print("Reducing() error:", e)

    def update_automated_attempts_display(self):
        self.maximum_attempts_button.setText(str(self.maximum_attempts))
        self.attempts_so_far_button.setText(str(self.attempts_used))
        self.remaining_attempts_button.setText(str(self.remaining_attempts))
        self.num_of_matched_buttons.setText(str(self.matched_buttons))
        self.num_of_matched_buttonsL.setText(str(self.matched_buttonsL))
        self.all_matched_button.setText(str(self.all_matched))



    def automation_progress(self):
        # BLINKING EFFECT
        self.anim_blink = QPropertyAnimation(self.instruction_label, b"opacity")
        effect = QGraphicsOpacityEffect(self.instruction_label)
        self.instruction_label.setGraphicsEffect(effect)

        self.anim_blink.setTargetObject(effect)
        self.anim_blink.setDuration(1300)  # Total blink cycle duration
        self.anim_blink.setLoopCount(8)  # Number of blinks
        self.anim_blink.setStartValue(1.0)  # Fully visible
        self.anim_blink.setKeyValueAt(0.5, 0.0)  # Fully invisible in the middle
        self.anim_blink.setEndValue(2.0)  # Back to visible
        self.anim_blink.start()


    def hide_staffs(self):
        cards = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6]
        for card in cards:
            card.hide()
        self.lineEdit.hide()
        self.label.hide()
        self.instruction_label.hide()
        self.record_button.hide()
        attempt_buttons = [self.maximum_attempts_button, self.remaining_attempts_button, self.attempts_so_far_button]
        for attempt_button in attempt_buttons:
            attempt_button.hide()
        attempt_labels = [self.maximum_attempts_label, self.remaining_attempts_label, self.attempts_so_far_label]
        for attempt_label in attempt_labels:
            attempt_label.hide()

    def show_staffs(self):
            cards = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6]
            for card in cards:
                card.show()
            self.lineEdit.show()
            self.label.show()
            self.instruction_label.show()
            self.record_button.show()
            attempt_buttons = [self.maximum_attempts_button, self.remaining_attempts_button,
                               self.attempts_so_far_button]
            for attempt_button in attempt_buttons:
                attempt_button.show()
            attempt_labels = [self.maximum_attempts_label, self.remaining_attempts_label, self.attempts_so_far_label]
            for attempt_label in attempt_labels:
                attempt_label.show()

    def recording(self):
        number = self.lineEdit.text().strip()
        if number == "":
            #QApplication.beep()
            self.shaking_effect()
            self.instruction_label.hide()
            self.label.show(),
            self.label.setText("You did not enter anything.")
            self.label.setStyleSheet("color: red;"
                                     "font-size: 22px;")
            QTimer.singleShot(2000, lambda: (
                self.instruction_label.show(),
                self.label.hide(),
            ))


            return  # Stop here so no further code runs

        try:
            sender = int(number)
        except ValueError:
            #QApplication.beep()
            self.shaking_effect()
            self.instruction_label.hide()
            self.label.show()
            self.label.setText("Please enter a valid number.")
            self.label.setStyleSheet("color: red;"
                                     "font-size: 22px;")
            QTimer.singleShot(2000, lambda: (
                self.instruction_label.show(),
                self.lineEdit.setText(""),
                self.label.hide(),
            ))
            return

        if sender > 100 and sender != 666:
            #QApplication.beep()
            self.shaking_effect()
            self.instruction_label.hide()
            self.label.show()
            self.label.setText("Attempts cannot be more than 100.")
            self.label.setStyleSheet("color: red;"
                                     "font-size: 22px;")
            QTimer.singleShot(2000, lambda: (
                self.instruction_label.show(),
                self.lineEdit.setText(""),
                self.label.hide(),
            ))
        elif sender > 100 and sender == 666:
            #QApplication.beep()
            self.shaking_effect2()
            self.blinking_effect2()
            self.instruction_label.hide()
            self.label.show()
            self.label.setText("That number is strange💀💀💀")
            self.label.setStyleSheet("color: red;"
                                     "font-size: 22px;")
            QTimer.singleShot(2000, lambda: (
                self.instruction_label.show(),
                self.lineEdit.setText(""),
                self.label.hide(),
            ))


        else:
            if sender < 50:
                #QApplication.beep()
                self.shaking_effect()
                self.instruction_label.hide()
                self.label.show()
                self.label.setText("Attempts cannot be less than 50.")
                self.label.setStyleSheet("color: red;"
                                         "font-size: 22px;")
                QTimer.singleShot(2000, lambda: (
                    self.instruction_label.show(),
                    self.lineEdit.setText(""),
                    self.label.hide(),
                ))

            elif 50 <= sender <= 100:
                self.maximum_attempts = sender
                self.remaining_attempts = sender
                self.attempts_used = 0
                self.matched_buttons = 0
                self.update_attempts_display()
                self.start_card()


    def manual_match_count(self):
        num1 = self.button1.text().strip()
        num2 = self.button2.text().strip()
        num3 = self.button3.text().strip()
        if (num1 == num2 == num3) and (num1 !="" and num2 !="" and num3 !=""):
            self.matched_buttons += 1
            self.update_attempts_display()
            QApplication.beep()
        else:
            pass

    def update_attempts_display(self):
        self.maximum_attempts_button.setText(str(self.maximum_attempts))
        self.attempts_so_far_button.setText(str(self.attempts_used))
        self.remaining_attempts_button.setText(str(self.remaining_attempts))
        self.num_of_matched_buttons.setText(str(self.matched_buttons))

    def brain(self):
        self.label.hide()
        self.instruction_label.show()
        random_codes = ["1", "2", "3", "4", "5", "6"]
        cards = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6]
        for card in cards:
            card.setText(random.choice(random_codes))
        self.decrement_attempts()


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

    def shaking_effect2(self):
        ### 1️⃣ SHAKE EFFECT
        rect = self.label.geometry()
        self.anim_shake = QPropertyAnimation(self.label, b"geometry")
        self.anim_shake.setDuration(900)
        self.anim_shake.setLoopCount(6)
        self.anim_shake.setKeyValueAt(0, rect)
        self.anim_shake.setKeyValueAt(0.25, rect.translated(-15, 0))
        self.anim_shake.setKeyValueAt(0.5, rect.translated(5, 0))
        self.anim_shake.setKeyValueAt(0.75, rect.translated(-15, 0))
        self.anim_shake.setKeyValueAt(1, rect)
        self.anim_shake.start()

    def blinking_effect2(self):
        # BLINKING EFFECT
        self.anim_blink = QPropertyAnimation(self.label, b"opacity")
        effect = QGraphicsOpacityEffect(self.label)
        self.label.setGraphicsEffect(effect)

        self.anim_blink.setTargetObject(effect)
        self.anim_blink.setDuration(1300)  # Total blink cycle duration
        self.anim_blink.setLoopCount(4)  # Number of blinks
        self.anim_blink.setStartValue(1.0)  # Fully visible
        self.anim_blink.setKeyValueAt(0.5, 0.0)  # Fully invisible in the middle
        self.anim_blink.setEndValue(2.0)  # Back to visible
        self.anim_blink.start()



    def start_card(self):
        self.label.show()
        self.lineEdit.hide()
        self.label.setText("Recorded")
        self.label.setStyleSheet("color: red;"
                                "font-size: 24px;")
        self.record_button.hide()
        self.instruction_label.hide()

        QTimer.singleShot(1500, lambda: ( self.label.hide(),
                                          self.record_button.show(),
                                          self.instruction_label.show(),
                                          self.record_button.setText("Reshuffle"),
                                          self.record_button.setStyleSheet("color: white;"
                                                                          "font-size: 20px;"
                                                                           "background-color: hsl(40, 50%, 40%);"),
                                          self.instruction_label.setText(
                                              "Click the reshuffle button until either 3 upper\n"
                                              "or lower cards match in numbers across."),
                                          self.instruction_label.setStyleSheet("color: white;"
                                                                  "font-size: 24px;")))
        try:
            self.record_button.clicked.disconnect()
        except:
            pass
        self.record_button.clicked.connect(self.brain)


    def decrement_attempts(self):
        # Initialize on first run after pressing Start
        self.record_button.setText("Reshuffle")
        if self.maximum_attempts == 0:
            try:
                self.maximum_attempts = int(self.lineEdit.text().strip())
            except:
                self.label.setText("Invalid number!")
                return

            self.remaining_attempts = self.maximum_attempts
            self.attempts_used = 0
            self.update_attempts_display()

        # Deduct an attempt
        if self.remaining_attempts > 0:
            self.attempts_used += 1
            self.remaining_attempts -= 1
            self.update_attempts_display()
        else:
            #QApplication.beep()
            self.shaking_effect2()
            self.instruction_label.show()
            self.label.hide()
            self.blinking_effect2()
            QTimer.singleShot(0, lambda: (
                self.instruction_label.setText("Game Over💀💀"),
                self.instruction_label.setStyleSheet("color: red;"
                                                     "font-size: 30px;"),
                QTimer.singleShot(2500, lambda: (self.instruction_label.setText("Click ,'review' button to check integrity\nof the game"),
                                  self.instruction_label.setStyleSheet("color: white;"
                                                                       "font-size: 25px;"),
            ))))

            self.instruction_label.setGeometry(150, 10, 500, 60)
            self.record_button.setEnabled(False) # Stop the game
            self.record_button.setStyleSheet("background-color: black;"
                                             "font-size: 21px;")
            self.record_button.setText("Finished")

    def reset_attempts(self):
        self.attempts_used = 0
        self.remaining_attempts = self.maximum_attempts
        self.update_attempts_display()




    def cancel_stage(self):
        self.intro_label.hide()
        try:
            self.proceed_button.clicked.disconnect()
        except Exception:
            pass
        try:
            self.cancel_button.clicked.disconnect()
        except Exception:
            pass
        self.intro_label.hide()
        entry1_buttons = [self.proceed_button, self.cancel_button]
        for button in entry1_buttons:
            button.hide()
        self.popup = QWidget(self)
        self.popup.setGeometry(130, 200, 400, 200)
        self.popup.setStyleSheet("""
                    background-color: grey;
                    border-radius: 20px;
                    border: 2px solid grey;
                """)
        self.popup.show()

        # The question label
        self.popup_label = QLabel("So fast😲? Are you sure\n you want to quit game?", self.popup)
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
        self.no_button.clicked.connect(self.redirect)
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
        self.confirm_button.clicked.connect(self.exit_game)
        self.confirm_button.show()




    def exit_game(self):
        self.popup.hide()
        self.intro_label.show()
        self.intro_label.setText("That was soo soon😏")
        self.intro_label.setGeometry(130, 220, 500, 250)
        self.intro_label.setStyleSheet("font-size: 40px; color: lightgreen; font-family: sans-serif;")
        QTimer.singleShot(2000, self.close)  # close after 3 sec

    def redirect(self):
        self.popup.hide()
        self.intro_label.show()
        self.intro_label.setGeometry(60, 220, 600, 400)
        self.intro_label.setText("Wait while the server redirects you.\n\n\n\n           redirecting.....")
        self.intro_label.setStyleSheet("color: orange;"
                                  "font-size: 32px;")
        QTimer.singleShot(3000, self.instructions)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
