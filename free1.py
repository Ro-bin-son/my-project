import sys
import time
import random
from itertools import count

from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from typing import List, Dict, Any

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
        self.home_layout_label = QLabel(self)
        self.sign_in_layout_button = QPushButton(self)
        self.sign_out_layout_button = QPushButton(self)
        self.creator_label = QLabel("Founder & Developer, Robin", self)
        self.record_button = QPushButton("Record", self)
        self.popup = QWidget(self)
        self.popup_label = QLabel(self)
        self.automatic_mode_label = QLabel(self)
        self.no_button = QPushButton(self)
        self.confirm_button = QPushButton(self)
        self.automatic_button = QPushButton(self)
        self.okay_button = QPushButton("Okay", self)
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
        self.sign_up_label = QLabel(self)
        self.sign_up_button = QPushButton(self)
        self.multiplier_label = QLabel(self)
        self.error_label = QLabel(self)
        self.check1 = QCheckBox(self)
        self.check2 = QCheckBox(self)
        self.check3 = QCheckBox(self)
        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)
        self.line3 = QLineEdit(self)
        self.line4 = QLineEdit(self)
        self.line5 = QLineEdit(self)
        self.line6 = QLineEdit(self)

        self.flex1 = QPushButton(self)
        self.flex2 = QPushButton(self)
        self.flex3 = QPushButton(self)
        self.flex4 = QPushButton(self)
        self.flex5 = QPushButton(self)
        self.flex6 = QPushButton(self)
        self.flex7 = QPushButton(self)
        self.flex8 = QPushButton(self)
        self.flex9 = QPushButton(self)
        self.flex10 = QPushButton(self)
        self.flex11 = QPushButton(self)
        self.flex12 = QPushButton(self)
        self.flex13 = QPushButton(self)
        self.flex14 = QPushButton(self)
        self.flex15 = QPushButton(self)
        self.flex16 = QPushButton(self)
        self.flex17 = QPushButton(self)
        self.flex18 = QPushButton(self)
        self.flex19 = QPushButton(self)
        self.flex20 = QPushButton(self)
        self.flex21 = QPushButton(self)
        self.flex22 = QPushButton(self)
        self.flex23 = QPushButton(self)
        self.flex24 = QPushButton(self)
        self.flex25 = QPushButton(self)
        self.flex26 = QPushButton(self)
        self.flex27 = QPushButton(self)
        self.flex28 = QPushButton(self)
        self.flex29 = QPushButton(self)
        self.flex30 = QPushButton(self)
        self.flex31 = QPushButton(self)
        self.flex32 = QPushButton(self)
        self.flex33 = QPushButton(self)
        self.flex34 = QPushButton(self)
        self.flex35 = QPushButton(self)
        self.flex36 = QPushButton(self)
        self.flex37 = QPushButton(self)
        self.flex38 = QPushButton(self)
        self.flex39 = QPushButton(self)
        self.flex40 = QPushButton(self)
        self.flex41 = QPushButton(self)
        self.flex42 = QPushButton(self)
        self.flex43 = QPushButton(self)
        self.flex44 = QPushButton(self)
        self.flex45 = QPushButton(self)
        self.flex46 = QPushButton(self)
        self.flex47 = QPushButton(self)
        self.flex48 = QPushButton(self)
        self.flex49 = QPushButton(self)
        self.flex50 = QPushButton(self)
        self.flex51 = QPushButton(self)
        self.flex52 = QPushButton(self)
        self.flex53 = QPushButton(self)
        self.flex54 = QPushButton(self)
        self.flex55 = QPushButton(self)
        self.flex56 = QPushButton(self)
        self.flex57 = QPushButton(self)
        self.flex58 = QPushButton(self)
        self.flex59 = QPushButton(self)
        self.flex60 = QPushButton(self)
        self.flex61 = QPushButton(self)
        self.flex62 = QPushButton(self)
        self.flex63 = QPushButton(self)
        self.flex64 = QPushButton(self)
        self.flexes = [self.flex1,self.flex2,self.flex3,self.flex4,self.flex5,self.flex6,self.flex7,
                       self.flex8,self.flex9,self.flex10,self.flex11,self.flex12,self.flex13,self.flex14,
                       self.flex15,self.flex16,self.flex17,self.flex18,self.flex19,self.flex20,self.flex21,
                       self.flex22,self.flex23,self.flex24,self.flex25,self.flex26,self.flex27,self.flex28,
                       self.flex29,self.flex30,self.flex31,self.flex32, self.flex33, self.flex34, self.flex35,
                       self.flex36, self.flex37, self.flex38, self.flex39, self.flex40, self.flex41, self.flex42,
                       self.flex43, self.flex44, self.flex45, self.flex46, self.flex47, self.flex48, self.flex49,
                       self.flex50, self.flex51, self.flex52, self.flex53, self.flex54, self.flex55, self.flex56,
                       self.flex57, self.flex58, self.flex59, self.flex60, self.flex61, self.flex62, self.flex63,
                       self.flex64
                       ]

        self.proceed_button = QPushButton("Proceed", self)
        self.cancel_button = QPushButton("Cancel", self)
        self.lineEdit = QLineEdit(self)
        self.credentials_label = QLabel(self)
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.line_edit1_label = QLabel("User name:", self)
        self.line_edit2_label = QLabel("Password:", self)
        self.allow_button = QPushButton(self)
        self.rating_label = QLabel(self)
        self.rating_button = QPushButton(self)
        self.contact_count = 0
        self.disjoint_count = 0
        self.contact_total = 0
        self.tapped = []
        self.collected_wins = []
        self.extra_cost = 0
        self.current_value = 1.00
        self.rounds = 0
        self.days = 0
        self.constant_output = 640
        self.stop_value = round(random.uniform(1.00, 2000.00), 2)
        self.automation_timer = QTimer(self)
        self.automation_timer.timeout.connect(self.prize_determinant)
        self.initUI()


    def initUI(self):
        for flex in self.flexes:
            flex.hide()
        lines = [self.line1, self.line2, self.line3, self.line4, self.line5, self.line6]
        for line in lines:
            line.hide()
        self.error_label.hide()
        self.multiplier_label.hide()
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
        self.line_edit1_label.hide()
        self.line_edit2_label.hide()
        self.allow_button.hide()
        credentials = [self.credentials_label, self.line_edit1, self.line_edit2]
        for field in credentials:
            field.hide()
        mode_labels = [self.automatic_mode_label]
        for label in mode_labels:
            label.hide()
        for w in (self.check1, self.check2, self.check3, self.okay_button):
            w.hide()
        self.hide_staffs()
        self.setWindowTitle("HIGH SPEED SIMULATION SOFTWARE💀💀")
        self.label.setGeometry(115, 10, 500, 55)
        self.instruction_label.setGeometry(215, 10, 500, 55)
        self.creator_label.setGeometry(485, 790, 500, 55)
        self.proceed_button.setGeometry(130, 450, 130, 50)
        self.cancel_button.setGeometry(410, 450, 130, 50)
        self.intro_label.setGeometry(40, 40, 800, 300)
        self.flex1.setGeometry(40, 365, 70, 27), self.flex2.setGeometry(113, 365, 70, 27), self.flex3.setGeometry(188, 365, 70, 27)
        self.flex4.setGeometry(263, 365, 70, 27), self.flex5.setGeometry(338, 365, 70, 27),self.flex6.setGeometry(413, 365, 70, 27)
        self.flex7.setGeometry(488, 365, 70, 27),self.flex8.setGeometry(563, 365, 70, 27)
        self.flex9.setGeometry(40, 395, 70, 27), self.flex10.setGeometry(113, 395, 70, 27), self.flex11.setGeometry(188, 395, 70, 27)
        self.flex12.setGeometry(263, 395, 70, 27), self.flex13.setGeometry(338, 395, 70, 27), self.flex14.setGeometry(413, 395, 70, 27)
        self.flex15.setGeometry(488, 395, 70, 27), self.flex16.setGeometry(563, 395, 70, 27)
        self.flex17.setGeometry(40, 425, 70, 27), self.flex18.setGeometry(113, 425, 70, 27), self.flex19.setGeometry(188, 425, 70, 27)
        self.flex20.setGeometry(263, 425, 70, 27), self.flex21.setGeometry(338, 425, 70, 27), self.flex22.setGeometry(413, 425, 70, 27)
        self.flex23.setGeometry(488, 425, 70, 27), self.flex24.setGeometry(563, 425, 70, 27)
        self.flex25.setGeometry(40, 455, 70, 27), self.flex26.setGeometry(113, 455, 70, 27), self.flex27.setGeometry(188, 455, 70, 27)
        self.flex28.setGeometry(263, 455, 70, 27), self.flex29.setGeometry(338, 455, 70, 27), self.flex30.setGeometry(413, 455, 70, 27)
        self.flex31.setGeometry(488, 455, 70, 27), self.flex32.setGeometry(563, 455, 70, 27)
        self.flex33.setGeometry(40, 485, 70, 27), self.flex34.setGeometry(113, 485, 70, 27), self.flex35.setGeometry(188, 485, 70, 27)
        self.flex36.setGeometry(263, 485, 70, 27), self.flex37.setGeometry(338, 485, 70, 27), self.flex38.setGeometry(413, 485, 70, 27)
        self.flex39.setGeometry(488, 485, 70, 27), self.flex40.setGeometry(563, 485, 70, 27)
        self.flex41.setGeometry(40, 515, 70, 27), self.flex42.setGeometry(113, 515, 70, 27), self.flex43.setGeometry(188, 515, 70, 27)
        self.flex44.setGeometry(263, 515, 70, 27), self.flex45.setGeometry(338, 515, 70, 27), self.flex46.setGeometry(413, 515, 70, 27)
        self.flex47.setGeometry(488, 515, 70, 27), self.flex48.setGeometry(563, 515, 70, 27)
        self.flex49.setGeometry(40, 545, 70, 27), self.flex50.setGeometry(113, 545, 70, 27), self.flex51.setGeometry(188, 545, 70, 27)
        self.flex52.setGeometry(263, 545, 70, 27), self.flex53.setGeometry(338, 545, 70, 27), self.flex54.setGeometry(413, 545, 70, 27)
        self.flex55.setGeometry(488, 545, 70, 27), self.flex56.setGeometry(563, 545, 70, 27)
        self.flex57.setGeometry(40, 575, 70, 27), self.flex58.setGeometry(113, 575, 70, 27), self.flex59.setGeometry(188, 575, 70, 27)
        self.flex60.setGeometry(263, 575, 70, 27), self.flex61.setGeometry(338, 575, 70, 27), self.flex62.setGeometry(413, 575, 70, 27)
        self.flex63.setGeometry(488, 575, 70, 27), self.flex64.setGeometry(563, 575, 70, 27)
        for flex in self.flexes:
            flex.setStyleSheet("background-color: red;"
                               "font-size: 17px;")
            flex.setText("")
        self.proceed_button.setStyleSheet("font-size: 25px;" "color: grey;" "background-color: hsl(180, 38%, 17%)")

        self.cancel_button.setStyleSheet("font-size: 25px;" "color: grey;" "background-color: hsl(180, 38%, 29%)")

        self.intro_label.setStyleSheet("font-size: 28px;" "color: grey;")
        self.creator_label.setStyleSheet("font-size: 14px;" "color: grey;")

        self.instruction_label.setStyleSheet("font-size: 20px;" "color: white;")

        self.lineEdit.setGeometry(210, 70, 250, 40)
        self.lineEdit.setPlaceholderText("Type your number here (1 - 100)")
        self.lineEdit.setStyleSheet(
            "font-size:16px;"  "background-color: grey;"   "border-radius: 1px;" "font-family:sans-serif;"
            )


        self.record_button.setGeometry(275, 130, 110, 40)
        self.record_button.setObjectName("record_button")

        self.setStyleSheet("""QMainWindow {

                                       background-color: hsl(0, 0%, 25%);
                                         }
                                       QPushButton {
                                       font-size: 50px; font-family: arial; border: 2px solid; border-radius: 8px;
                                       }
                                     
                                     QPushButton#record_button{
                                           background-color: hsl(180, 38%, 17%);  font-size: 16px; border-style: solid; border-radius: 10px;
                                           color: white;
                                           }

                                     QPushButton#record_button:hover {
                                           background-color: hsl(180, 38%, 20%);
                                           }                    
                                     }
                                       """)


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
        self.entry_passkey_layout()

        # ---------- safe wrappers that catch exceptions ----------

    def safe_instructions(self):
        try:
            self.allow_button.clicked.disconnect()
        except Exception:
            pass
        self.instructions()

    def safe_mode_selection(self):
        try:
            self.arranging_mechanics()
        except Exception:
            pass

    def entry_passkey_layout(self):
        self.line_edit1_label.hide()
        self.line_edit2_label.hide()
        self.proceed_button.hide()
        self.cancel_button.hide()
        self.allow_button.hide()
        self.intro_label.hide()
        self.automatic_button.hide()
        self.confirm_button.hide()
        self.no_button.hide()
        self.cancel_button.hide()
        self.home_layout_label.show()
        self.sign_in_layout_button.hide()
        self.sign_out_layout_button.show()
        self.line_edit1_label.show()
        self.line_edit2_label.show()
        self.proceed_button.hide()
        self.cancel_button.hide()
        self.allow_button.show()
        self.intro_label.hide()
        credentials = [self.credentials_label, self.line_edit1, self.line_edit2]
        for field in credentials:
            field.show()

        self.credentials_label.setStyleSheet("font-size: 24px;"
                                             "color: grey;")

        self.line_edit1.setPlaceholderText("Enter your user name")
        self.line_edit1.setStyleSheet("font-size: 16px;"
                                      "color: black;"
                                      "background-color: white;")

        self.line_edit2.setPlaceholderText("Enter your password")
        self.line_edit2.setStyleSheet("font-size: 16px;"
                                      "color: black;"
                                      "background-color: white;")

        self.allow_button.setText("Sign in")
        self.home_layout_label.setText("Sign in to your account\n to continue.")
        self.sign_up_label.setText("Don't have an account?")
        self.sign_up_button.setText("Sign up")
        self.sign_up_button.setStyleSheet("font-size: 22px;"
                                        "color: white;"
                                        "background-color: #008fcc;")
        self.sign_up_label.setStyleSheet("font-size: 22px;"
                                          "color: white;"
                                          )

        self.allow_button.setStyleSheet("font-size: 22px;"
                                        "color: white;"
                                        "background-color: #008fcc;")

        self.line_edit1_label.setStyleSheet("font-size: 17px;"
                                            "color: white;")
        self.line_edit2_label.setStyleSheet("font-size: 17px;"
                                            "color: white;")
        self.home_layout_label.setGeometry(150, 20, 800, 80)
        self.home_layout_label.setStyleSheet("font-size: 35px;" "color: grey;")
        self.sign_in_layout_button.setStyleSheet("font-size: 25px;"
                                                 "Background-color: #008fcc;"
                                                 "color: white")

        self.sign_out_layout_button.setStyleSheet("font-size: 25px;"
                                                  "Background-color: grey;"
                                                  "color: white")
        self.sign_out_layout_button.setText("Cancel")

        self.sign_up_label.setGeometry(140, 490, 500, 50)
        self.sign_out_layout_button.setGeometry(380, 400, 120, 50)
        self.sign_up_button.setGeometry(380, 490, 120, 50)
        self.allow_button.setGeometry(160, 400, 120, 50)

        self.line_edit1.setGeometry(140, 200, 400, 40)
        self.line_edit2.setGeometry(140, 300, 400, 40)
        self.line_edit1_label.setGeometry(140, 170, 150, 30)
        self.line_edit2_label.setGeometry(140, 270, 150, 30)
        try:
            self.allow_button.clicked.disconnect()
        except Exception:
            pass
        self.allow_button.clicked.connect(self.verifier)
        try:
            self.sign_out_layout_button.clicked.disconnect()
        except Exception:
            pass
        self.sign_out_layout_button.clicked.connect(self.exit_game2)
        try:
            self.sign_up_button.clicked.disconnect()
        except Exception:
            pass
        self.sign_up_button.clicked.connect(self.new_account)

    def new_account(self):
        lines = [self.line1, self.line2, self.line3, self.line4, self.line5, self.line6]
        for line in lines:
            line.show()
        self.sign_up_button.setGeometry(265, 580, 120, 50)
        self.sign_up_button.setText("Create")
        self.home_layout_label.setGeometry(120, 10, 600, 70)
        self.home_layout_label.setStyleSheet("color: grey;"
                                             "font-size: 35px;")
        self.line1.setGeometry(170, 110, 300, 30)
        self.line2.setGeometry(170, 185, 300, 30)
        self.line3.setGeometry(170, 260, 300, 30)
        self.line4.setGeometry(170, 335, 300, 30)
        self.line5.setGeometry(170, 410, 300, 30)
        self.line6.setGeometry(170, 485, 300, 30)

        self.sign_up_label.hide()
        self.home_layout_label.setText("Sign up to create new account. ")
        self.sign_in_layout_button.hide()
        self.sign_out_layout_button.hide()
        self.automatic_button.hide()
        self.confirm_button.hide()
        self.no_button.hide()
        self.line_edit1.hide()
        self.line_edit2.hide()
        self.allow_button.hide()
        self.credentials_label.hide()
        self.line_edit1_label.hide()
        self.line_edit2_label.hide()


    def verifier(self):
        username = self.line_edit1.text().strip()
        passkey = self.line_edit2.text().strip()
        # List of fields and their labels
        fields = [
            (self.line_edit1, self.line_edit1_label, username, "Username is required"),
            (self.line_edit2, self.line_edit2_label, passkey, "Passkey is required"),
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

        if all_valid:
            self.read_credentials()

    def read_credentials(self):
        passkey = self.line_edit2.text().strip()
        import json
        file_path = "Cred.json"
        with open(file_path, "r") as file:
            data = json.load(file)
            customers = data.get("GetAllCustomers", {})
            username = self.line_edit1.text().strip().capitalize()
            valid = False
            for cust_id, info in customers.items():
                fname = info.get("FirstName", "")
                if  username == fname and passkey == cust_id:
                    valid = True
                    break
            if valid:
                self.error_label.hide()
                self.verifying_sign()
            else:
                self.error_label.show()
                self.error_label.setGeometry(220, 130, 400, 40)
                self.error_label.setStyleSheet("color: red;"
                                               "font-size: 18px;")
                self.error_label.setText("Invalid username or password.")

    def verifying_sign(self):
        self.sign_up_button.hide()
        self.sign_up_label.hide()
        self.home_layout_label.setGeometry(220, 240, 400, 40)
        self.home_layout_label.setStyleSheet("color: orange;"
                                       "font-size: 30px;")

        self.home_layout_label.setText("Please wait...")
        self.sign_in_layout_button.hide()
        self.sign_out_layout_button.hide()
        self.automatic_button.hide()
        self.confirm_button.hide()
        self.no_button.hide()
        self.line_edit1.hide()
        self.line_edit2.hide()
        self.allow_button.hide()
        self.credentials_label.hide()
        self.line_edit1_label.hide()
        self.line_edit2_label.hide()
        QTimer.singleShot(500, self.intro)

    def intro(self):
        self.home_layout_label.hide()
        self.sign_in_layout_button.hide()
        self.sign_out_layout_button.hide()
        self.automatic_button.hide()
        self.confirm_button.hide()
        self.no_button.hide()
        self.proceed_button.show()
        self.cancel_button.show()
        self.intro_label.show()
        self.line_edit1.hide()
        self.line_edit2.hide()
        self.credentials_label.hide()
        self.allow_button.hide()
        self.line_edit1_label.hide()
        self.line_edit2_label.hide()
        self.creator_label.setGeometry(520, 810, 150, 30)
        self.intro_label.setGeometry(40, 40, 800, 300)
        self.intro_label.setStyleSheet("font-size: 28px;" "color: grey;")

        self.intro_label.setText("Welcome to a game powered by probability,\nprecision, and pure machine intelligence."
                                 " Every\nmatch reveals a pattern."
                                 " You are about to enter\na live environment where results are recorded in\nreal time."
                                 " Click 'Proceed' to read instructions on\nhow software machine operates.")
        self.hide_staffs()
        self.proceed_button.clicked.connect(self.clicking)

    def clicking(self):
        try:
            self.allow_button.clicked.disconnect()
        except:
            pass
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
        self.intro_label.setText(
            "1. You will choose your Mode\n       Manual Mode: You control the card draws one step at a time.\n"
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


    def arranging_mechanics(self):
        try:
            self.automatic_button.clicked.disconnect()
        except Exception:
            pass
        self.hide_staffs()
        self.automatic_button.hide()
        self.proceed_button.hide()
        self.cancel_button.hide()
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
        self.check1.show(),
        self.check1.setText("Initializing button responsiveness....."),
        self.check1.setChecked(False),
        QTimer.singleShot(20, lambda: self.check1.setChecked(True))

        QTimer.singleShot(1500, lambda: (
            self.check2.show(),
            self.check2.setText("Checking game engine configurations...."),
            self.check2.setChecked(False),
            QTimer.singleShot(100, lambda: self.check2.setChecked(True))
        ))

        QTimer.singleShot(1500, lambda: (
            self.check3.show(),
            self.check3.setText("Initializing scores before game time..."),
            self.check3.setChecked(False),
            QTimer.singleShot(100, lambda: self.check3.setChecked(True))

        ))
        try:
            self.record_button.clicked.disconnect()
        except Exception:
            pass
        QTimer.singleShot(3500, self.automatic_mode_layout)


    def automatic_mode_layout(self):
        try:
            self.record_button.clicked.disconnect()
        except:
            pass
        for flex in self.flexes:
            flex.show()
        self.check1.hide()
        self.check2.hide()
        self.check3.hide()
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
        self.prize_label.setText("Aut.:")

        self.rating_label.setText("E/C:")
        self.developers_wallet_label.setText("Wallet Bal(Ksh):")
        self.developers_wallet_button.setText("12,500.00")
        self.total_amount_label.setText("Payout(+/-)(Ksh):")
        self.total_users_label.setText("Contact:")
        self.users_remaining_label.setText("Disjoint:")
        self.amount_cashed_out_label.setText("Cases A/B:")

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

        self.prize_label.setGeometry(225, 240, 100, 30)
        self.prize_button.setGeometry(300, 248, 125, 23)
        self.rating_label.setGeometry(5, 240, 100, 30)
        self.rating_button.setGeometry(90, 248, 125, 23)
        self.developers_wallet_button.setStyleSheet("background-color: white;"
                                                    "font-size: 22px;"
                                                    "color: black;"
                                                    "border-radius: 10px;")
        self.developers_wallet_label.setStyleSheet("font-size: 16px;"
                                                   "color: white;")
        self.total_amount_button.setStyleSheet("background-color: white;"
                                               "font-size: 22px;"
                                               "color: black;"
                                               "border-radius: 10px;")
        self.total_amount_label.setStyleSheet("font-size: 16px;"
                                              "color: white;")
        self.amount_cashed_out_button.setStyleSheet("background-color: white;"
                                                    "font-size: 22px;"
                                                    "color: black;"
                                                    "border-radius: 10px;")
        self.amount_cashed_out_label.setStyleSheet("font-size: 16px;"
                                                   "color: white;")

        self.total_users_button.setStyleSheet("background-color: white;"
                                              "font-size: 22px;"
                                              "color: black;"
                                              "border-radius: 10px;")
        self.total_users_label.setStyleSheet("font-size: 16px;"
                                             "color: white;")
        self.users_remaining_button.setStyleSheet("background-color: white;"
                                                  "font-size: 22px;"
                                                  "color: black;"
                                                  "border-radius: 10px;")
        self.users_remaining_label.setStyleSheet("font-size: 16px;"
                                                 "color: white;")

        self.prize_button.setStyleSheet("background-color: white;"
                                        "font-size: 22px;")
        self.prize_label.setStyleSheet("font-size: 22px;"
                                       "color: white;")
        self.rating_button.setStyleSheet("background-color: white;")

        self.rating_label.setStyleSheet("font-size: 22px;"
                                        "color: white;")

        self.automatic_mode_label.show()
        self.automatic_button.hide()
        self.show_staffs()
        self.lineEdit.hide()
        self.instruction_label.setText("Click 'Connect' to get into Game")
        self.record_button.setText("Connect")
        self.record_button.setStyleSheet("font-size: 22px;")
        self.automatic_mode_label.setText("Automatic Mode")
        self.automatic_mode_label.setGeometry(270, 0, 100, 30)
        self.automatic_mode_label.setStyleSheet("color: orange;")

        try:
            self.record_button.clicked.disconnect()
        except:
            pass
        self.record_button.clicked.connect(self.system_on_standby)

    def system_on_standby(self):
        self.instruction_label.show()
        self.instruction_label.setText("Please wait......")
        self.record_button.hide()
        self.instruction_label.setGeometry(200, 20, 700, 40)
        self.instruction_label.setStyleSheet("font-size: 24px;"
                                             "color: orange;")
        QTimer.singleShot(2500,self.start_automatic_prep)
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

        self.instruction_label.setText("Waiting for session....")
        self.instruction_label.setStyleSheet("font-size: 24px;"
                                             "color: red;")
        self.record_button.hide()
        QTimer.singleShot(7000, self.start_automation)

    def start_automation(self):
        self.loading_button1.hide()
        self.current_value = 1.00
        self.prize_button.setText("1.00")  # initial visible display
        self.instruction_label.setGeometry(250, 100, 700, 50)
        self.instruction_label.setText("In session 🚀")
        self.automation_timer.start()


    def get_multipliers(self, total=64):
        # Each range has min, max, and possible count (min_count, max_count)
        range_limits = [
            {"min": 1.00, "max": 1.99, "min_count": 25, "max_count": 40},
            {"min": 2.00, "max": 6.99, "min_count": 20, "max_count": 47},
            {"min": 7.00, "max": 9.99, "min_count": 0, "max_count": 5},
            {"min": 10.00, "max": 29.99, "min_count": 0, "max_count": 5},
            {"min": 30.00, "max": 49.99, "min_count": 0, "max_count": 5},
            {"min": 50.00, "max": 999.99, "min_count": 0, "max_count": 5},
            {"min": 1000.00, "max": 10000.00, "min_count": 0, "max_count": 3}
        ]

        counts = []
        # Pick random counts within min-max first😎
        for r in range_limits:
            counts.append(random.randint(r["min_count"], r["max_count"]))
        # Adjust proportionally to match total
        current_total = sum(counts)
        while current_total != total:
            diff = total - current_total

            # Randomly pick an index to increase or decrease
            idx = random.randint(0, len(counts) - 1)

            # Calculate allowable adjustment
            min_allowed = range_limits[idx]["min_count"]
            max_allowed = range_limits[idx]["max_count"]
            if diff > 0 and counts[idx] < max_allowed:
                counts[idx] += 1
                current_total += 1
            elif diff < 0 and counts[idx] > min_allowed:
                counts[idx] -= 1
                current_total -= 1
        return counts


    def read_all_flex_multipliers(self):
        multipliers = []
        for flex in self.flexes:
            value = flex.text().replace("x", "").strip()
            try:
                multipliers.append(float(value))
            except:
                multipliers.append(0.0)
        return multipliers

    def perform_case_A(self):
        multipliers = self.read_all_flex_multipliers()
        total = 0
        seven_counter = 0
        mode = "seven"  # 70-tap mode
        first_seven_index = None

        for i, m in enumerate(multipliers):
            if mode == "seven":
                if m >= 7 and m < 30:
                    total += 70
                    seven_counter += 1
                    if seven_counter == 1:
                        first_seven_index = i  # mark the first tapped seven
                elif m > 30:
                    total += 70  # first >30x tapped as 70
                    mode = "thirty"
            elif mode == "thirty":
                if m > 30:
                    total += 300


            # After first two ≥7 tapped, continue scanning
            if seven_counter >= 2 and mode == "seven":
                continue
        self.amount_cashed_out_button.setText(str(total))
        return total


    def perform_case_B(self):
        multipliers = self.read_all_flex_multipliers()
        total = 0

        first = None
        second = None
        first_index = None
        second_index = None

        # find first multiplier ≥ 7
        for i, m in enumerate(multipliers):
            if m >= 7:
                first = m
                first_index = i
                break

        # condition: first must be >30
        if first is None or first <= 30:
            return 0

        # tap first at 7x
        total += 70

        # find second multiplier ≥ 7 (after first)
        for i in range(first_index + 1, len(multipliers)):
            if multipliers[i] >= 7:
                second = multipliers[i]
                second_index = i
                break

        # tap second at 7x (both rule1 and rule2)
        if second is not None:
            total += 70
            start_index = second_index + 1
        else:
            start_index = first_index + 1

        # after second: tap only >30x
        for m in multipliers[start_index:]:
            if m > 30:
                total += 300

        self.amount_cashed_out_button.setText(str(total))
        return total

    def perform_contact(self):
        multipliers = self.read_all_flex_multipliers()
        final = self.contact_penalty()
        self.contact_count = 0  # reset count for this run
        for i in range(len(multipliers) - 1):
            A = multipliers[i]
            B = multipliers[i + 1]

            if A >= 10 and B > 30:
                self.contact_count += 1
        payout = (self.contact_count * 300) - final
        self.total_users_button.setText(str(payout))

    def contact_penalty(self):
        multipliers = self.read_all_flex_multipliers()
        charges = 0
        for i in range(len(multipliers) - 1):
            A = multipliers[i]
            if A >= 10:
                charges += 1
        final = charges * 10
        return final

    def perform_disjoint(self):
        final = self.disjoint_penalty()
        multipliers = self.read_all_flex_multipliers()
        payout = 0
        for i in range(len(multipliers) - 2):
            A = multipliers[i]
            B = multipliers[i+1]
            C = multipliers[i+2]
            if A >= 10 > B and C > 30:
                self.disjoint_count += 1
                payout = (self.disjoint_count * 300) - final
        # Update GUI only ONCE after processing all
        self.users_remaining_button.setText(str(payout - final if payout else 0 - final))

    def disjoint_penalty(self):
        multipliers = self.read_all_flex_multipliers()
        charges = 0
        for i in range(len(multipliers) - 2):
            A = multipliers[i]
            B = multipliers[i + 1]
            if A >= 10 and B < 10:
                charges += 1
        final = charges * 10
        return final

    def calculate_penalty_and_payout(self):
        multipliers = self.read_all_flex_multipliers()

        cost = 0
        safety_started = False
        exit_multiplier = None

        for i, m in enumerate(multipliers):

            if not safety_started and m > 30:
                if all(prev < 7 for prev in multipliers[:i]):
                    safety_started = True
                    continue

            if safety_started:
                cost += 10

                if m >= 7:
                    exit_multiplier = m
                    safety_started = False
                    break

        # Case 1: safety never started
        if not safety_started and exit_multiplier is None:
            self.total_amount_button.setText("0")
            return 0

        # Case 2: safety started but never exited → pure loss
        if safety_started and exit_multiplier is None:
            result = -cost
            self.total_amount_button.setText(str(result))
            return result

        # Case 3: safety exited normally
        if exit_multiplier > 30:
            result = 300 - cost
        else:
            result = -cost
        return result


    def final_payout(self):
        penalty = self.calculate_penalty_and_payout()
        try:
            value1 = float(self.total_users_button.text().strip() or 0)
        except ValueError:
            value1 = 0

        try:
            value2 = float(self.users_remaining_button.text().strip() or 0)
        except ValueError:
            value2 = 0

        try:
            value3 = float(self.amount_cashed_out_button.text().strip() or 0)
        except ValueError:

            value3 = 0

        tally1 = (value3 + (value1 + value2))
        tally3 = tally1 + penalty
        tally4 = tally3 - self.constant_output
        final_tally = f"{tally4:,.2f}"
        self.total_amount_button.setText(final_tally)

    def generate_all_values(self):
        range_limits = [
            {"min": 1.00, "max": 1.99, "min_count": 25, "max_count": 40},
            {"min": 2.00, "max": 6.99, "min_count": 22, "max_count": 37},
            {"min": 7.00, "max": 9.99, "min_count": 0, "max_count": 8},
            {"min": 10.00, "max": 29.99, "min_count": 0, "max_count": 4},
            {"min": 30.00, "max": 49.99, "min_count": 0, "max_count": 3},
            {"min": 50.00, "max": 99.99, "min_count": 0, "max_count": 3},
            {"min": 100.00, "max": 999.99, "min_count": 0, "max_count": 3},
            {"min": 1000.00, "max": 10000.00, "min_count": 0, "max_count": 1},
        ]
        counts = self.get_multipliers()
        all_values = []
        for r, count in zip(range_limits, counts):
                for _ in range(count):
                    value = random.uniform(r["min"], r["max"])
                    all_values.append(f"{value:.2f}x")
        random.shuffle(all_values)
        return all_values



    def set_flexes(self):
        all_values = self.generate_all_values()
        for i in range(64):
            flex = self.flexes[i]
            flex.setText(all_values[i])



    def final_wallet_update(self):
        try:
            real_time_amount =float(self.total_amount_button.text().replace(",", "").strip() or 0)
            dev_wal = self.developers_wallet_button.text().replace(",", "").replace(",", "").strip()
            dev_wallet = float(dev_wal)
            dev_total_balance = real_time_amount + dev_wallet
            append_amount = f"{dev_total_balance:,.2f}"
            self.developers_wallet_button.setText(append_amount)
        except Exception as e:
            print("final_wallet_update error:", e)

    def write_payout_to_file(self):
        value = self.total_amount_button.text().strip()
        file_path = "data.txt"
        try:
            with open(file_path, "a") as file:
                file.write(value + "\n")
        except Exception as e:
            print("File write error:", e)

    def prize_layout_display(self):
        try:
            text = self.prize_button.text().replace("x", "").replace(",", "").strip()
            xx = float(text)
            if xx < 2.00:
                color = "red"
            elif 2 <= xx < 10.00:
                color = "black"

            else:
                color = "blue"
            self.prize_button.setStyleSheet(f"background-color: white;"
                                            f"font-size: 22px;"
                                            f"color: {color};"
                                            f"border-radius: 10px;"
                                            )

            self.rating_button.setStyleSheet(f"background-color: white;"
                                            f"font-size: 22px;"
                                            f"color: {color};"
                                            f"border-radius: 10px;"
                                            )
        except:
            pass

    def speed_check(self):
        checker = float(self.prize_button.text().replace(",", "").replace("x", "").strip())
        # 1 - 2
        if checker < 2:
            self.automation_timer.setInterval(12)
        # 2 - 5
        elif checker < 5:
            self.automation_timer.setInterval(10)
        # 5 - 10
        elif checker < 10:
            self.automation_timer.setInterval(5)
        # 10 - 20
        elif checker < 20:
            self.automation_timer.setInterval(5)
        # 20 - 40
        elif checker < 40:
            self.automation_timer.setInterval(0)
        # 40 - 70
        elif checker < 70:
            self.automation_timer.setInterval(0)
        # 70 - 130
        elif checker < 130:
            self.automation_timer.setInterval(0)
        # 130 - 500
        elif checker < 500:
            self.automation_timer.setInterval(0)  # begins flashing 😂⚡
        # 500+
        else:
            self.automation_timer.setInterval(0)  # MAX SPEED BOOOOM 😭💥💥

    def prize_determinant(self):
        real_display = f"{self.current_value:,.2f}x"
        self.prize_button.setText(real_display)
        self.speed_check()
        self.prize_layout_display()
        if self.current_value >= self.stop_value:
            self.session_end()
            return
        self.current_value = round(self.current_value + 0.1, 2)

    def total_rounds(self):
        if self.current_value >= self.stop_value:
            self.rounds += 1
            self.total_users_button.setText(str(self.rounds))

    def total_simulated_days(self):
        if self.rounds % 40 == 0 and self.rounds != 0:
            self.days += 1
            self.users_remaining_button.setText(str(self.days))

    def session_end(self):
        self.automation_timer.stop()
        self.prize_layout_display()
        self.multiplier_label.show()
        stop_mult = f"{self.current_value:,.2f}x"
        self.rating_button.setText(stop_mult)
        self.instruction_label.setText("Session ended.")
        multiplier = self.prize_button.text().strip()
        self.multiplier_label.setText(multiplier)
        self.instruction_label.setGeometry(230, 50, 700, 50)
        self.multiplier_label.setGeometry(240, 90, 700, 80)
        self.instruction_label.setStyleSheet("color: red;"
                                             "font-size: 25px;")

        self.multiplier_label.setStyleSheet("color: red;"
                                             "font-size: 45px;")
        self.set_flexes()
        self.perform_case_A()
        self.perform_case_B()
        self.perform_contact()
        self.perform_disjoint()
        self.final_payout()
        self.final_wallet_update()
        self.write_payout_to_file()

        QTimer.singleShot(2500, lambda: (
            self.reset()
        ))

    def reset(self):
        self.multiplier_label.hide()
        self.instruction_label.setGeometry(230, 100, 700, 50)
        self.instruction_label.setStyleSheet("font-size: 24px;"
                                                 "color: orange;")
        self.instruction_label.setText("Session resetting...")
        self.prize_button.setText("")
        self.rating_button.setText("")
        self.total_amount_button.setText("")
        self.users_remaining_button.setText("")
        self.total_users_button.setText("")
        self.amount_cashed_out_button.setText("")
        self.prize_button.setStyleSheet("color: black;"
                                            "background-color: white;"
                                            )
        QTimer.singleShot(2500, self.start_round)



    def start_round(self):
        # 1️⃣ Reset necessary round values
        self.contact_count = 0
        self.disjoint_count = 0
        self.contact_total = 0
        self.current_value = 1.00
        self.stop_value = 0.00
        total = 0
        self.stop_value = round(random.uniform(1.00, 2000.00), 2)
        self.automation_timer.start()
        # 2️⃣ Update UI fresh
        self.instruction_label.setGeometry(250, 100, 700, 50)
        self.instruction_label.setText("In session 🚀")
        self.prize_layout_display()
        self.prize_determinant()

    def hide_staffs(self):
        self.lineEdit.hide()
        self.label.hide()
        self.instruction_label.hide()
        self.record_button.hide()


    def show_staffs(self):
        self.lineEdit.show()
        self.label.show()
        self.instruction_label.show()
        self.record_button.show()


    def cancel_stage(self):
        try:
            self.proceed_button.clicked.disconnect()
        except Exception:
            pass
        try:
            self.cancel_button.clicked.disconnect()
        except Exception:
            pass
        self.intro_label.hide()
        self.home_layout_label.hide()
        self.sign_out_layout_button.hide()
        self.sign_in_layout_button.hide()
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
        self.popup_label = QLabel("So soon😲? Are you sure\n you want to exit app?", self.popup)
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

    def exit_game2(self):
        self.popup.hide()
        self.intro_label.setText("")
        QTimer.singleShot(100, self.close)  # close after 3 sec


    def exit_game(self):
        self.popup.hide()
        self.intro_label.show()
        self.intro_label.setText("Goodbye👋")
        self.intro_label.setGeometry(210, 220, 500, 250)
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
