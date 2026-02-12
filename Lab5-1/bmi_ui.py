# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox, QFrame, QGroupBox,
    QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor


class BMIUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(430, 720)
        self.setStyleSheet("background-color: #eeeeee;")

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)


        card = QFrame()
        card.setFixedWidth(360)
        card.setStyleSheet("""
            QFrame {
                background-color: #f3f3f3;
                border: 1px solid #cccccc;
                border-radius: 6px;
            }
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(15, 15, 15, 15)
        card_layout.setSpacing(18)


        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 11, QFont.Bold))
        title.setStyleSheet("""
            background-color: #b74a3a;
            color: white;
            padding: 8px;
            border-radius: 4px;
        """)
        card_layout.addWidget(title)


        age_layout = QHBoxLayout()

        age_label = QLabel("Calculate BMI for")
        age_label.setStyleSheet("background: transparent; border: none;")
        age_layout.addWidget(age_label)

        age_combo = QComboBox()
        age_combo.addItems(["Adult Age 20+", "Child Age 2-19"])
        age_combo.setFixedWidth(160)
        age_combo.setFocusPolicy(Qt.NoFocus)
        age_layout.addWidget(age_combo)

        age_layout.addStretch()
        card_layout.addLayout(age_layout)


        weight_layout = QHBoxLayout()

        weight_label = QLabel("Weight:")
        weight_label.setStyleSheet("background: transparent; border: none;")
        weight_layout.addWidget(weight_label)

        weight_input = QLineEdit()
        weight_input.setFixedWidth(80)
        weight_layout.addWidget(weight_input)

        weight_unit = QComboBox()
        weight_unit.addItems(["pounds", "kilograms"])
        weight_unit.setFixedWidth(110)
        weight_unit.setFocusPolicy(Qt.NoFocus)
        weight_layout.addWidget(weight_unit)

        weight_layout.addStretch()
        card_layout.addLayout(weight_layout)


        height_layout = QHBoxLayout()

        height_label = QLabel("Height:")
        height_label.setStyleSheet("background: transparent; border: none;")
        height_layout.addWidget(height_label)

        height_input = QLineEdit()
        height_input.setFixedWidth(80)
        height_layout.addWidget(height_input)

        height_unit = QComboBox()
        height_unit.addItems(["feet", "meters", "centimeters"])
        height_unit.setFixedWidth(110)
        height_unit.setFocusPolicy(Qt.NoFocus)
        height_layout.addWidget(height_unit)

        height_layout.addStretch()
        card_layout.addLayout(height_layout)

        
        inch_layout = QHBoxLayout()
        inch_layout.addSpacing(56)

        inch_input = QLineEdit()
        inch_input.setFixedWidth(80)
        inch_layout.addWidget(inch_input)

        inch_label = QLabel("inches")
        inch_label.setStyleSheet("background: transparent; border: none;")
        inch_layout.addWidget(inch_label)

        inch_layout.addStretch()
        card_layout.addLayout(inch_layout)


        btn_layout = QHBoxLayout()

        clear_btn = QPushButton("Clear")
        clear_btn.setFixedWidth(90)

        calc_btn = QPushButton("Calculate")
        calc_btn.setFixedWidth(90)

        btn_layout.addWidget(clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(calc_btn)

        card_layout.addLayout(btn_layout)


        answer_group = QGroupBox("Answer:")
        answer_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #cccccc;
                border-radius: 4px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: #f3f3f3;
            }
        """)

        answer_layout = QVBoxLayout(answer_group)

        bmi_label = QLabel("BMI =")
        bmi_label.setAlignment(Qt.AlignCenter)
        bmi_label.setFont(QFont("Arial", 11, QFont.Bold))
        bmi_label.setStyleSheet("background: transparent; border: none;")
        answer_layout.addWidget(bmi_label)

        adult_label = QLabel("Adult BMI")
        adult_label.setAlignment(Qt.AlignCenter)
        adult_label.setFont(QFont("Arial", 10, QFont.Bold))
        adult_label.setStyleSheet("background: transparent; border: none;")
        answer_layout.addWidget(adult_label)


        table = QTableWidget(4, 2)
        table.setHorizontalHeaderLabels(["BMI", "Status"])
        table.verticalHeader().setVisible(False)
        table.setFixedSize(250, 200)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setFrameShape(QFrame.NoFrame)

        table.setStyleSheet("""
            QTableWidget {
                border: none;
                background: white;
                gridline-color: #cfcfcf;
            }
            QHeaderView::section {
                background-color: #d9d9d9;
                padding: 6px;
                border: 1px solid #c0c0c0;
                font-weight: bold;
            }
        """)

        data = [
            ("≤ 18.4", "Underweight", "#f7d774"),
            ("18.5 - 24.9", "Normal", "#9bd18c"),
            ("25.0 - 39.9", "Overweight", "#f5b041"),
            ("≥ 40.0", "Obese", "#f25c54")
        ]

        for row, (bmi, status, color) in enumerate(data):
            bmi_item = QTableWidgetItem(bmi)
            bmi_item.setTextAlignment(Qt.AlignCenter)
            bmi_item.setBackground(QColor(color))

            status_item = QTableWidgetItem(status)
            status_item.setTextAlignment(Qt.AlignCenter)

            table.setItem(row, 0, bmi_item)
            table.setItem(row, 1, status_item)

        table_layout = QHBoxLayout()
        table_layout.addStretch()
        table_layout.addWidget(table)
        table_layout.addStretch()

        answer_layout.addLayout(table_layout)
        card_layout.addWidget(answer_group)

        main_layout.addWidget(card)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMIUI()
    window.show()
    sys.exit(app.exec_())
