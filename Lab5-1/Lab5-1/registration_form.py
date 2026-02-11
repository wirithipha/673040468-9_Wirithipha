# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QLocale,Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P2: Student Registration")
        self.setFixedSize(400, 600)

        layout = QVBoxLayout()
        title_label = QLabel("Student Registration Form")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size:18px;front-weight:bold;")
        layout.addWidget(title_label)

        layout.addSpacing(10)

        layout.addWidget(QLabel("Full Name:"))
        layout.addWidget(QLineEdit())

        layout.addWidget(QLabel("Email:"))
        layout.addWidget(QLineEdit())

        layout.addWidget(QLabel("Phone:"))
        layout.addWidget(QLineEdit())

        layout.addWidget(QLabel("Date of Birth (dd/MM/yyyy):"))

        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        # บังคับใช้เลขสากล + ค.ศ.
        date_edit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        date_edit.setDisplayFormat("dd/MM/yyyy")
        date_edit.setDate(QDate(2000, 1, 1))
        layout.addWidget(date_edit)


        layout.addWidget(QLabel("Gender:"))
        gender_layout = QHBoxLayout()
        gender_group = QButtonGroup()

        for g in ["Male", "Female", "Non-binary", "Prefer not to say"]:
            rb = QRadioButton(g)
            gender_group.addButton(rb)
            gender_layout.addWidget(rb)
            
        layout.addLayout(gender_layout)

        layout.addWidget(QLabel("Program:"))
        program = QComboBox()
        program.addItem("Select your program")
        program.addItems([
            "Computer Engineering", "Digital Media Engineering",
            "Environmental Engineering", "Electrical Engineering",
            "Semiconductor Engineering", "Mechanical Engineering",
            "Industrial Engineering", "Logistic Engineering",
            "Power Engineering", "Electronic Engineering",
            "Telecommunication Engineering", "Agricultural Engineering",
            "Civil Engineering", "ARIS"
        ])
        layout.addWidget(program)

        layout.addWidget(QLabel("Tell us a little bit about yoursel:"))
        about = QTextEdit()
        about.setMaximumHeight(100)
        layout.addWidget(about)

        accept = QCheckBox("I accept the terms and conditions")
        layout.addWidget(accept)

        submit = QPushButton("Submit Registration")
        layout.addWidget(submit)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = RegistrationForm()
window.show()
sys.exit(app.exec_())

