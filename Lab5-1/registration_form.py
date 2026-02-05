# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Registration Form")
        self.setFixedSize(400, 600)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Full Name:"))
        layout.addWidget(QLineEdit())

        layout.addWidget(QLabel("Email:"))
        layout.addWidget(QLineEdit())

        layout.addWidget(QLabel("Phone:"))
        layout.addWidget(QLineEdit())

        layout.addWidget(QLabel("Date of Birth:"))
        date = QDateEdit()
        date.setCalendarPopup(True)
        date.setDate(QDate(2000,1,1))
        layout.addWidget(date)

        layout.addWidget(QLabel("Gender:"))
        gender_layout = QHBoxLayout()
        gender_group = QButtonGroup()

        male = QRadioButton("Male")
        female = QRadioButton("Female")
        other = QRadioButton("Other")

        gender_group.addButton(male)
        gender_layout.addWidget(female)
        gender_layout.addWidget(other)

        layout.addLayout(gender_layout)

        layout.addWidget(QLabel("Program:"))
        program = QComboBox()
        program.addItem("Select your program")
        program.addItems([
            "computer Engineering",
            "Digital Media Engineering",
            "Environmantal Engineering",
            "Electrical Engineering",
            "Mechanicl Engineering"
        ])
        layout.addWidget(program)

        layout.addWidget(QLabel("About yourself:"))
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

