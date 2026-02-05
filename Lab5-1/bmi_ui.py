# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import sys
from PyQt5.QtWidgets import *

class BMIUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(350, 450)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Calculate BMI for"))
        age = QComboBox()
        age.addItems(["Adult Age 20+", "Child"])
        layout.addWidget(age)

        weight_layout = QHBoxLayout()
        weight_layout.addWidget(QLabel("Weight:"))
        weight_layout.addWidget(QLineEdit())
        weight_unit = QComboBox()
        weight_unit.addItems(["kg", "pounds"])
        weight_layout.addWidget(weight_unit)
        layout.addLayout(weight_layout)

        height_layout = QHBoxLayout()
        height_layout.addWidget(QLabel("Height:"))
        height_layout.addWidget(QLineEdit())
        height_unit = QComboBox()
        height_unit.addItems(["cm", "feet"])
        height_layout.addWidget(height_unit)
        layout.addLayout(height_layout)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(QPushButton("Clear"))
        btn_layout.addWidget(QPushButton("Calculate"))
        layout.addLayout(btn_layout)

        layout.addWidget(QLabel("Answer:"))
        layout.addWidget(QLabel("BMI ="))

        self.setLayout(layout)

app = QApplication(sys.argv)
window = BMIUI()
window.show()
sys.exit(app.exec_())
