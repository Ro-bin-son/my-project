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
        self.home_layout_label = QLabel(self)
        self.sign_in_layout_button = QPushButton(self)
        self.sign_out_layout_button = QPushButton(self)
        self.loading_sign1 = QLabel("Verifying", self)
        self.loading_sign2 = QLabel(".", self)
        self.loading_sign3 = QLabel(".", self)
        self.loading_sign4 = QLabel(".", self)
        self.creator_label = QLabel("Developed by Robin", self)
        self.maximum_attempts_label = QLabel("Selected\nAttempts:", self)
        self.attempts_so_far_label = QLabel("Attempts\nUsed:", self)
        self.remaining_attempts_label = QLabel("Attempts\nRemaining:", self)
        self.maximum_attempts_button = QPushButton("", self)
        self.attempts_so_far_button = QPushButton("", self)
        self.remaining_attempts_button = QPushButton("", self)
        self.record_button = QPushButton("Record", self)
        self.popup = QWidget(self)
        self.popup_label = QLabel(self)
        self.automatic_mode_label = QLabel(self)
        self.no_button = QPushButton(self)
        self.confirm_button = QPushButton(self)
        self.automatic_button = QPushButton(self)
        self.okay_button = QPushButton("Okay", self)
        self.num_of_matched_buttons = QPushButton(self)
        self.num_of_matched_buttonsL = QPushButton(self)
        self.num_of_matched_label = QLabel(self)
        self.num_of_matched_labelL = QLabel(self)
        self.all_matched_label = QLabel(self)
        self.all_matched_button = QPushButton(self)
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
        self.flexes = [self.flex1, self.flex2, self.flex3, self.flex4, self.flex5, self.flex6, self.flex7,
                       self.flex8, self.flex9, self.flex10, self.flex11, self.flex12, self.flex13, self.flex14,
                       self.flex15, self.flex16, self.flex17, self.flex18, self.flex19, self.flex20, self.flex21,
                       self.flex22, self.flex23, self.flex24, self.flex25, self.flex26, self.flex27, self.flex28,
                       self.flex29, self.flex30, self.flex31, self.flex32, self.flex33, self.flex34, self.flex35,
                       self.flex36, self.flex37, self.flex38, self.flex39, self.flex40, self.flex41, self.flex42,
                       self.flex43, self.flex44, self.flex45, self.flex46, self.flex47, self.flex48, self.flex49,
                       self.flex50, self.flex51, self.flex52, self.flex53, self.flex54, self.flex55, self.flex56,
                       self.flex57, self.flex58, self.flex59, self.flex60, self.flex61, self.flex62, self.flex63,
                       self.flex64]
        self.group1 = [self.flex1, self.flex2, self.flex3, self.flex4, self.flex5, self.flex6, self.flex7, self.flex8]
        self.group2 = [self.flex9, self.flex10, self.flex11, self.flex12, self.flex13, self.flex14, self.flex15,
                       self.flex16]
        self.group3 = [self.flex17, self.flex18, self.flex19, self.flex20, self.flex21, self.flex22, self.flex23,
                       self.flex24]
        self.group4 = [self.flex25, self.flex26, self.flex27, self.flex28, self.flex29, self.flex30, self.flex31,
                       self.flex32]
        self.group5 = [self.flex33, self.flex34, self.flex35, self.flex36, self.flex37, self.flex38, self.flex39,
                       self.flex40]
        self.group6 = [self.flex41, self.flex42, self.flex43, self.flex44, self.flex45, self.flex46, self.flex47,
                       self.flex48]
        self.group7 = [self.flex49, self.flex50, self.flex51, self.flex52, self.flex53, self.flex54, self.flex55,
                       self.flex56]
        self.group8 = [self.flex57, self.flex58, self.flex59, self.flex60, self.flex61, self.flex62, self.flex63,
                       self.flex64]

        self.segment1 = [
            [self.flex1, self.flex2, self.flex3, self.flex4, self.flex5, self.flex6, self.flex7, self.flex8],
            [self.flex9, self.flex10, self.flex11, self.flex12, self.flex13, self.flex14, self.flex15, self.flex16],
            [self.flex17, self.flex18, self.flex19, self.flex20, self.flex21, self.flex22, self.flex23, self.flex24],
            [self.flex25, self.flex26, self.flex27, self.flex28, self.flex29, self.flex30, self.flex31, self.flex32]
            ]
        self.segment2 = [
            [self.flex33, self.flex34, self.flex35, self.flex36, self.flex37, self.flex38, self.flex39, self.flex40],
            [self.flex41, self.flex42, self.flex43, self.flex44, self.flex45, self.flex46, self.flex47, self.flex48],
            [self.flex49, self.flex50, self.flex51, self.flex52, self.flex53, self.flex54, self.flex55, self.flex56],
            [self.flex57, self.flex58, self.flex59, self.flex60, self.flex61, self.flex62, self.flex63, self.flex64]
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
        self.matched_buttons = 0
        self.matched_buttonsL = 0
        self.all_matched = 0
        self.rating_label = QLabel(self)
        self.rating_button = QPushButton(self)
        self.maximum_attempts = 0
        self.attempts_used = 0
        self.remaining_attempts = 0
        self.number_of_rounds = 0
        self.total_amount = 0
        self.automation_timer = QTimer(self)
        self.automation_timer.timeout.connect(self.automatic_click)

        self.initUI()

    def initUI(self):
        for flex in self.flexes:
            flex.hide()
        self.loading_sign1.hide()
        self.loading_sign2.hide()
        self.loading_sign3.hide()
        self.loading_sign4.hide()
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
        self.creator_label.setGeometry(520, 790, 500, 55)
        self.proceed_button.setGeometry(130, 450, 130, 50)
        self.cancel_button.setGeometry(410, 450, 130, 50)
        self.maximum_attempts_button.setGeometry(35, 230, 80, 27)
        self.attempts_so_far_button.setGeometry(200, 230, 80, 27)
        self.remaining_attempts_button.setGeometry(365, 230, 80, 27)
        self.maximum_attempts_label.setGeometry(25, 180, 90, 45)
        self.attempts_so_far_label.setGeometry(189, 180, 90, 42)
        self.remaining_attempts_label.setGeometry(355, 180, 90, 42)
        self.intro_label.setGeometry(40, 40, 800, 300)
        for flex in self.group1:
            self.flex1.setGeometry(40, 365, 70, 27), self.flex2.setGeometry(113, 365, 70, 27), self.flex3.setGeometry(
                188, 365, 70, 27)
            self.flex4.setGeometry(263, 365, 70, 27), self.flex5.setGeometry(338, 365, 70, 27), self.flex6.setGeometry(
                413, 365, 70, 27)
            self.flex7.setGeometry(488, 365, 70, 27), self.flex8.setGeometry(563, 365, 70, 27)
        for flex in self.group2:
            self.flex9.setGeometry(40, 395, 70, 27), self.flex10.setGeometry(113, 395, 70, 27), self.flex11.setGeometry(
                188, 395, 70, 27)
            self.flex12.setGeometry(263, 395, 70, 27), self.flex13.setGeometry(338, 395, 70,
                                                                               27), self.flex14.setGeometry(413, 395,
                                                                                                            70, 27)
            self.flex15.setGeometry(488, 395, 70, 27), self.flex16.setGeometry(563, 395, 70, 27)
        for flex in self.group3:
            self.flex17.setGeometry(40, 425, 70, 27), self.flex18.setGeometry(113, 425, 70,
                                                                              27), self.flex19.setGeometry(188, 425, 70,
                                                                                                           27)
            self.flex20.setGeometry(263, 425, 70, 27), self.flex21.setGeometry(338, 425, 70,
                                                                               27), self.flex22.setGeometry(413, 425,
                                                                                                            70, 27)
            self.flex23.setGeometry(488, 425, 70, 27), self.flex24.setGeometry(563, 425, 70, 27)
        for flex in self.group4:
            self.flex25.setGeometry(40, 455, 70, 27), self.flex26.setGeometry(113, 455, 70,
                                                                              27), self.flex27.setGeometry(188, 455, 70,
                                                                                                           27)
            self.flex28.setGeometry(263, 455, 70, 27), self.flex29.setGeometry(338, 455, 70,
                                                                               27), self.flex30.setGeometry(413, 455,
                                                                                                            70, 27)
            self.flex31.setGeometry(488, 455, 70, 27), self.flex32.setGeometry(563, 455, 70, 27)
        for flex in self.group5:
            self.flex33.setGeometry(40, 485, 70, 27), self.flex34.setGeometry(113, 485, 70,
                                                                              27), self.flex35.setGeometry(188, 485, 70,
                                                                                                           27)
            self.flex36.setGeometry(263, 485, 70, 27), self.flex37.setGeometry(338, 485, 70,
                                                                               27), self.flex38.setGeometry(413, 485,
                                                                                                            70, 27)
            self.flex39.setGeometry(488, 485, 70, 27), self.flex40.setGeometry(563, 485, 70, 27)
        for flex in self.group6:
            self.flex41.setGeometry(40, 515, 70, 27), self.flex42.setGeometry(113, 515, 70,
                                                                              27), self.flex43.setGeometry(188, 515, 70,
                                                                                                           27)
            self.flex44.setGeometry(263, 515, 70, 27), self.flex45.setGeometry(338, 515, 70,
                                                                               27), self.flex46.setGeometry(413, 515,
                                                                                                            70, 27)
            self.flex47.setGeometry(488, 515, 70, 27), self.flex48.setGeometry(563, 515, 70, 27)
        for flex in self.group7:
            self.flex49.setGeometry(40, 545, 70, 27), self.flex50.setGeometry(113, 545, 70,
                                                                              27), self.flex51.setGeometry(188, 545, 70,
                                                                                                           27)
            self.flex52.setGeometry(263, 545, 70, 27), self.flex53.setGeometry(338, 545, 70,
                                                                               27), self.flex54.setGeometry(413, 545,
                                                                                                            70, 27)
            self.flex55.setGeometry(488, 545, 70, 27), self.flex56.setGeometry(563, 545, 70, 27)
        for flex in self.group8:
            self.flex57.setGeometry(40, 575, 70, 27), self.flex58.setGeometry(113, 575, 70,
                                                                              27), self.flex59.setGeometry(188, 575, 70,
                                                                                                           27)
            self.flex60.setGeometry(263, 575, 70, 27), self.flex61.setGeometry(338, 575, 70,
                                                                               27), self.flex62.setGeometry(413, 575,
                                                                                                            70, 27)
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

        self.maximum_attempts_label.setStyleSheet("font-size: 17px;"  "color: grey;")

        self.attempts_so_far_label.setStyleSheet("font-size: 17px;"  "color: grey;")

        self.remaining_attempts_label.setStyleSheet("font-size: 17px;"  "color: grey;")
        self.maximum_attempts_button.setStyleSheet("font-size: 20px;"   "color: grey;")
        self.remaining_attempts_button.setStyleSheet("font-size: 20px;"  "color: grey;")
        self.attempts_so_far_button.setStyleSheet("font-size: 20px;" "color: grey;")

        self.lineEdit.setGeometry(210, 70, 250, 40)
        self.lineEdit.setPlaceholderText("Type your number here (1 - 100)")
        self.lineEdit.setStyleSheet(
            "font-size:16px;"  "background-color: grey;"   "border-radius: 1px;" "font-family:sans-serif;"
        )

        self.button1.setGeometry(95, 365, 90, 190)
        self.button2.setGeometry(275, 365, 90, 190)
        self.button3.setGeometry(455, 365, 90, 190)
        self.button4.setGeometry(95, 590, 90, 190)
        self.button5.setGeometry(275, 590, 90, 190)
        self.button6.setGeometry(455, 590, 90, 190)
        self.record_button.setGeometry(275, 130, 110, 40)
        self.loading_sign1.setGeometry(220, 250, 130, 40)
        self.loading_sign2.setGeometry(350, 250, 130, 40)
        self.loading_sign3.setGeometry(365, 250, 130, 40)
        self.loading_sign4.setGeometry(380, 250, 130, 40)

        self.loading_sign1.setStyleSheet("font-size: 32px;"  "color: orange;")
        self.loading_sign2.setStyleSheet("font-size: 36px;"  "color: orange;")
        self.loading_sign3.setStyleSheet("font-size: 36px;"  "color: orange;")
        self.loading_sign4.setStyleSheet("font-size: 36px;"  "color: orange;")
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
        self.credentials_label.setText("Sign in:")
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

        self.allow_button.setStyleSheet("font-size: 22px;"
                                        "color: white;"
                                        "background-color: #008fcc;")
        self.line_edit1_label.setStyleSheet("font-size: 17px;"
                                            "color: white;")
        self.line_edit2_label.setStyleSheet("font-size: 17px;"
                                            "color: white;")
        self.home_layout_label.setGeometry(150, 20, 800, 80)
        self.home_layout_label.setText("Sign in to your account\n to continue.")
        self.home_layout_label.setStyleSheet("font-size: 35px;" "color: grey;")
        self.sign_in_layout_button.setStyleSheet("font-size: 25px;"
                                                 "Background-color: #008fcc;"
                                                 "color: white")
        self.sign_out_layout_button.setStyleSheet("font-size: 25px;"
                                                  "Background-color: grey;"
                                                  "color: white")
        self.sign_out_layout_button.setText("Cancel")

        self.credentials_label.setGeometry(280, 120, 400, 40)
        self.sign_out_layout_button.setGeometry(380, 450, 120, 50)
        self.line_edit1.setGeometry(140, 200, 400, 40)
        self.line_edit2.setGeometry(140, 300, 400, 40)
        self.allow_button.setGeometry(160, 450, 120, 50)
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

        if all_valid:
            # self.verifying_sign()
            self.store_credentials_safely()

    def store_credentials_safely(self):
        try:
            import json
            file_path = "Credentials.json"
            with open(file_path, "w") as file:
                file_content1 = self.line_edit1.text().strip().capitalize()
                file_content2 = self.line_edit2.text().strip()
                format = {"Name": f"{file_content1}",
                          "Password": f"{file_content2}"}
                json.dump(format, file, indent=4)
                print(f"json file '{file_path}' has been created and\ncontent appended"
                      f" successfully😎.\nCheck IDE side bar to view.")

        except FileExistsError:
            print("That file exists already ")
        self.read_credential()

    def read_credential(self):
        import json
        file_path = "Cred.json"
        with open(file_path, "r") as file:
            data = json.load(file)
            customers = data.get("GetAllCustomers", {})
            customer_id = "10168"
            first_name = customers[customer_id].get("FirstName")
            if customer_id in customers:
                print(first_name)
            else:
                print("Customer ID not found💀💀")

        self.verifying_sign()

    def verifying_sign(self):
        self.home_layout_label.hide()
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
        self.loading_sign1.show()
        QTimer.singleShot(500, self.loading_sign2.show)
        QTimer.singleShot(1000, self.loading_sign3.show)
        QTimer.singleShot(1200, self.loading_sign4.show)
        QTimer.singleShot(2000, self.intro)

    def intro(self):
        self.loading_sign1.hide()
        self.loading_sign2.hide()
        self.loading_sign3.hide()
        self.loading_sign4.hide()
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
                                 " Click 'Proceed' to read instructions on\nhow to play or 'Cancel' to exit game.")
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
        QTimer.singleShot(1000, lambda: self.check1.setChecked(True))

        QTimer.singleShot(8000, lambda: (
            self.check2.show(),
            self.check2.setText("Checking game engine configurations...."),
            self.check2.setChecked(False),
            QTimer.singleShot(1000, lambda: self.check2.setChecked(True))
        ))

        QTimer.singleShot(12000, lambda: (
            self.check3.show(),
            self.check3.setText("Initializing scores before game time..."),
            self.check3.setChecked(False),
            QTimer.singleShot(1000, lambda: self.check3.setChecked(True))

        ))
        try:
            self.record_button.clicked.disconnect()
        except Exception:
            pass
        QTimer.singleShot(15000, self.automatic_mode_layout)

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
        self.developers_wallet_button.setText("12,500.00")
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
        self.show_staffs()
        self.lineEdit.hide()
        self.instruction_label.setText("Click 'Connect' to get into Game")
        self.record_button.setText("Connect")
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

        robot_number = random.randint(50000, 85000)
        robot_str = str(robot_number)
        length = len(robot_str)
        self.maximum_attempts = robot_number
        self.remaining_attempts = robot_number
        self.attempts_used = 0
        amount = random.choice([400, 500, 1000, 2000, 4000, 5000, 10000])
        players = random.choice([800, 1000, 2000, 3000])
        tot_amount = amount * players

        QTimer.singleShot(2500, lambda: (
            self.total_users_button.setText(str(f"{players:,.0f}")),
            self.total_amount_button.setText(str(f"{tot_amount:,.0f}")),

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

    def get_multipliers(self, total=64):
        # Each range has min, max, and possible count (min_count, max_count)
        range_limits = [
            {"min": 1.00, "max": 1.99, "min_count": 25, "max_count": 30},
            {"min": 2.00, "max": 6.99, "min_count": 22, "max_count": 34},
            {"min": 7.00, "max": 9.99, "min_count": 0, "max_count": 5},
            {"min": 10.00, "max": 29.99, "min_count": 0, "max_count": 5},
            {"min": 30.00, "max": 49.99, "min_count": 0, "max_count": 5},
            {"min": 50.00, "max": 99.99, "min_count": 0, "max_count": 5},
            {"min": 100.00, "max": 10000.00, "min_count": 0, "max_count": 3}
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

    # Analyze flexes using restart scanning logic
    def analyze_with_restart(self, values):
        clean = [float(v.replace("x", "")) for v in values]
        TOTAL_FLEXES = 64
        BASE_COST = 640
        assert len(clean) == TOTAL_FLEXES
        payouts = 0
        contact_triggers = []
        disjoint_triggers = []

        # Compute stage seven counts for 30x eligibility
        stage_seven_counts = {"upper": 0, "lower": 0}
        for i, v in enumerate(clean):
            if v >= 7.00:
                stage = "upper" if i < 32 else "lower"
                stage_seven_counts[stage] += 1
        stage_eligible_30 = {s: (c <= 2) for s, c in stage_seven_counts.items()}
        # Standard payouts
        for i, v in enumerate(clean):
            if 7.00 <= v < 30.00:
                payouts += 70
            elif v >= 30.00:
                stage = "upper" if i < 32 else "lower"
                payouts += 300 if stage_eligible_30[stage] else 70

        # Sequential scan with restart on trigger
        i = 0
        while i < TOTAL_FLEXES:
            v = clean[i]
            if v >= 10.00:
                if i + 1 < TOTAL_FLEXES and clean[i + 1] >= 30.00:
                    contact_triggers.append((i, i + 1))
                    payouts += 600
                    i = i + 1
                    continue
                if i + 2 < TOTAL_FLEXES and clean[i + 2] >= 30.00:
                    disjoint_triggers.append((i, i + 2))
                    payouts += 600
                    i = i + 2
                    continue
            i += 1
        penalties = (len(contact_triggers) + len(disjoint_triggers)) * 10
        total_cost = BASE_COST + penalties
        final = payouts - total_cost
        return final

    def run_simulations(self, starting_wallet=0):
        raw_wallet = starting_wallet
        vals = self.generate_all_values()
        final = self.analyze_with_restart(vals)
        raw_wallet += final
        wallet = f"{raw_wallet:,.0f}"
        return wallet

    def generate_all_values(self):
        range_limits = [
            {"min": 1.00, "max": 1.99, "min_count": 25, "max_count": 45},
            {"min": 2.00, "max": 6.99, "min_count": 22, "max_count": 45},
            {"min": 7.00, "max": 9.99, "min_count": 0, "max_count": 4},
            {"min": 10.00, "max": 29.99, "min_count": 0, "max_count": 3},
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
            # Assuming self.flexes is a list of 64 flex objects
            flex.setText(all_values[i])

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
            self.natural_liquidation()
            self.prize_determinant()
            self.prize_layout_display()
            self.update_user_card()
            self.loading_button1.hide()

        elif self.remaining_attempts == 0:
            self.automation_timer.stop()
            dd = int(self.users_remaining_button.text().replace(" ", "").strip())
            print(f"{dd} did not manage to cash out🥶🥶.")
            self.instruction_label.setText("Automation Complete")
            self.instruction_label.setStyleSheet("color: white; font-size: 32px;")
            QTimer.singleShot(3000, self.reset)

    def final_wallet_update(self, starting_m=12500):
        try:
            condition = int(self.all_matched_button.text().strip())
            new_amount = float(self.developers_wallet_button.text().replace(",", "").strip())
            real_time_amount = int(self.rating_button.text().replace(",", "").strip())
            dev_total_balance = starting_m + real_time_amount
            money1 = f"{dev_total_balance:,.2f}"
            dev_total_balance_old = new_amount + real_time_amount
            money2 = f"{dev_total_balance_old:,.2f}"
            # self.developers_wallet_button.setText(f"{dev_total_balance:,.2f}")
            self.developers_wallet_button.setText(money1) if condition <= 1 else self.developers_wallet_button.setText(
                money2)

        except Exception as e:
            print("final_wallet_update error:", e)

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

    def natural_liquidation(self):
        dd = float(self.total_amount_button.text().replace(",", "").strip() or 0)
        deduct = float(self.amount_cashed_out_button.text().replace(",", "").strip() or 0)
        init = float(self.developers_wallet_button.text().replace(",", "").strip() or 0)
        addition = dd + init
        add = init + (dd - deduct)
        try:
            prize_value = float(self.prize_button.text().strip() or 0)
            all_cards = int(self.all_matched_button.text().strip() or 0)
            if (prize_value <= -1000 and all_cards <= 2) or (prize_value <= -1800 and all_cards <= 10):
                ee = int(self.total_users_button.text().replace(",", "").strip() or 0)
                eee = int(self.users_remaining_button.text().replace(",", "").strip() or 0)
                self.trigger_liquidation()
                if eee == 0:
                    print(f"😶 All {ee} users liquidated 💀💀")
                if eee != 0:
                    print(f"😶 Remaining {eee} users liquidated 💀💀")
                self.developers_wallet_button.setText(
                    f"{addition:,.2f}") if deduct == 0 else self.developers_wallet_button.setText(f"{add:,.2f}")

        except ValueError as e:
            print(e)

    def amount_display(self):
        try:
            total_amount = float(self.total_amount_button.text().replace(",", "").strip() or 0)
            total_users = int(self.total_users_button.text().replace(",", "").strip() or 0)
            users_remaining = int(self.users_remaining_button.text().replace(",", "").strip() or 0)
            prize_value = float(self.prize_button.text().strip() or 0)

            # Avoid division errors
            if total_users == 0:
                return

            # Amount per user
            amount_per_user = total_amount / total_users

            # Users who have cashed out so far
            users_cashed_so_far = total_users - users_remaining

            # New total cashed = users_cashed * amount_per_user
            new_total_cashed = users_cashed_so_far * amount_per_user

            if prize_value > 1:
                self.amount_cashed_out_button.setText(f"{new_total_cashed:,.0f}")

        except Exception as e:
            print("Status layout error:", e)

    def users(self):
        try:
            total_users = int(self.total_users_button.text().replace(",", "").strip() or 0)
            users_remaining = int(self.users_remaining_button.text().replace(",", "").strip() or 0)
            raw = self.prize_button.text()
            clean = raw.replace(",", "").replace("++", "").replace("+", "").replace(" ", "").strip()
            prize_text = float(clean or 0)

            # ✅ Read all 6 card values
            cards = [
                self.button1.text().strip(),
                self.button2.text().strip(),
                self.button3.text().strip(),
                self.button4.text().strip(),
                self.button5.text().strip(),
                self.button6.text().strip()
            ]

            # ✅ Initialize users_remaining properly
            if users_remaining == 0:
                users_remaining = total_users

            # ✅ Stop when no users left
            if users_remaining <= 0:
                print("🚫 All users finished. No more deductions.")
                return

            # ✅ If all cards = 5 or 6 → no cashout
            if all(c == "5" for c in cards) or all(c == "6" for c in cards):
                print("😶 No player cashed out.")
                return

            # ✅ Pick random users to cash out
            users_cashed_out = random.randint(1, max(1, users_remaining // 2))
            remaining_users = max(0, users_remaining - users_cashed_out)

            # ✅ Update UI
            if prize_text > 0:
                print(f"💨 {users_cashed_out} users cashed out. {remaining_users} remaining.")
                self.users_remaining_button.setText(f"{remaining_users:,}")

        except Exception as e:
            print("Users() error:", e)

    def prize_determinant(self):
        try:
            v1 = int(self.num_of_matched_buttonsL.text().strip() or 0)
            v2 = int(self.num_of_matched_buttons.text().strip() or 0)
            x1 = self.button1.text().strip()
            x2 = self.button2.text().strip()
            x3 = self.button3.text().strip()
            x4 = self.button4.text().strip()
            x5 = self.button5.text().strip()
            x6 = self.button6.text().strip()

            if x1 == x2 == x3 == x4 == x5 == x6:
                new_tot = float(self.prize_button.text().replace("+", "").strip() or 0)
                if x1 == "1":
                    total = (new_tot + (v1 + (v2 + 1))) * 0.008

                elif x1 == "3":
                    total = (new_tot + (v1 + (v2 + 1))) * 0.007

                elif x1 == "2":
                    total = (new_tot + (v1 + (v2 + 1))) * 0.005

                elif x1 == "4":
                    total = (new_tot + (v1 + (v2 + 1)) + 250) * 0.009

                elif x1 in ["5", "6"]:
                    total = new_tot - new_tot
                    self.prize_button.setText(f"{total:.2f}")

                self.prize_button.setText(f"{total:.2f}") if total < 0 else self.prize_button.setText(
                    f"+{total:.2f}")

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
                # sign = "" if total < 0 else "+"
                # self.prize_button.setText(f"{sign}{total:.2f}")
                self.prize_button.setText(f"{total:.2f}") if total < 0 else self.prize_button.setText(
                    f"+{total:.2f}")

        except:
            pass

    def reset_r(self):
        self.rating_button.setText("")

    def trigger_liquidation(self):
        self.automation_timer.stop()
        self.instruction_label.setText("Liquidated")
        self.instruction_label.setGeometry(245, 100, 110, 35)
        self.instruction_label.setStyleSheet("""
            background-color: red;
            font-size: 24px;
            color: white;
            border-radius: 10px;
        """)
        QTimer.singleShot(3000, self.reset)

    def prize_layout_display(self):
        try:
            text = self.prize_button.text().replace("+", "").replace("++", "").strip()
            xx = float(text)

            if xx < 0:
                color = "red"
            elif xx == 0:
                color = "black"
            else:
                color = "blue"
            self.prize_button.setStyleSheet(f"background-color: white;"
                                            f"font-size: 22px;"
                                            f"color: {color};"
                                            f"border-radius: 10px;"
                                            )
        except:
            pass

    def rating_layout_display(self):
        self.rating_button.setStyleSheet(f"background-color: white;"
                                         f"font-size: 22px;"
                                         f"color: blue;"
                                         f"border-radius: 10px;"
                                         )

    def save_file(self):
        file_path = "data.txt"
        with open(file_path, "a") as file:
            for x in range(1):
                file_content = self.users_remaining_button.text().strip()
                file.write(f"{file_content}\n")
            print(f"File '{file_path}' has been created and\ncontent appended"
                  f" successfully😎.\nOpen IDE side bar to view.")

    def reset(self):
        self.instruction_label.hide()

        def do_reset():
            self.instruction_label.setGeometry(200, 20, 700, 40)
            self.instruction_label.setStyleSheet("font-size: 24px;"
                                                 "color: orange;")

            self.instruction_label.setText("Please wait......")
            # ✅ Reset internal game variables
            self.remaining_attempts = 0
            self.attempts_used = 0
            self.matched_buttons = 0
            self.matched_buttonsL = 0
            self.total_amount = 0
            self.total_amount_button.setText(str(self.total_amount))
            self.total_users = 0
            self.total_users_button.setText(str(self.total_users))
            self.users_remaining = 0
            self.users_remaining_button.setText(str(self.users_remaining))
            self.amount_cashed_out = 0
            self.amount_cashed_out_button.setText(str(self.amount_cashed_out))

            # ✅ Reset UI values (everything except wallet)
            self.remaining_attempts_button.setText("0")
            self.num_of_matched_buttonsL.setText("0")
            self.num_of_matched_buttons.setText("0")
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

        QTimer.singleShot(3000, do_reset)

    def pause2(self):
        self.automation_timer.stop()
        self.instruction_label.setText("Automation paused.")
        self.instruction_label.setGeometry(230, 80, 700, 50)
        self.instruction_label.setStyleSheet("color: red;"
                                             "font-size: 25px;")
        self.users()
        self.prize_determinant()
        self.amount_display()
        self.save_file()
        self.set_flexes()
        QTimer.singleShot(4500, lambda: (
            self.resume_after_pause()
        ))

    def resume_after_pause(self):
        self.rating_layout_display()
        self.reset_r()
        self.automation_timer.start(1)
        # 👇 Now safe to simulate (NOT inside UI freeze moment)
        final_wallet = self.run_simulations()
        self.rating_button.setText(str(final_wallet))
        self.final_wallet_update()

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

    def exit_game2(self):
        self.popup.hide()
        self.intro_label.setText("")
        QTimer.singleShot(100, self.close)  # close after 3 sec

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
