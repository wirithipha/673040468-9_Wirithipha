# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import sys
from PyQt5.QtWidgets import *

class LoginUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        title = QLabel("LOGIN")
        layout.addWidget(title)

        email = QLineEdit()
        email.setPlaceholderText("Email")
        layout.addWidget(email)

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)
        layout.addWidget(password)

        remember = QCheckBox("Remember me?")
        layout.addWidget(remember)

        login_btn = QPushButton("LOGIN")
        layout.addWidget(login_btn)

        forgot = QLabel("Forgot Password?")
        layout.addWidget(forgot)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = LoginUI()
window.show()
sys.exit(app.exec_())
