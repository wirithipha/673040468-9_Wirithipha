# Name: Wirithipha Duangjan
# Student ID: 673040468-9


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox
)
from PyQt5.QtCore import Qt


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: BMI Calculator")
        self.setGeometry(300, 200, 400, 520)
        self.initUI()

    def initUI(self):

        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(15, 15, 15, 15)

        
        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            background-color: #A52A2A;
            color: white;
            padding: 8px;
            font-weight: bold;
            font-size: 18px;
        """)
        main_layout.addWidget(title)

        
        age_layout = QHBoxLayout()
        age_label = QLabel("BMI age group:")
        self.age_combo = QComboBox()
        self.age_combo.addItems([
            "Adults 20+",
            "Children and Teenagers (5-19)"
        ])
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_combo)
        main_layout.addLayout(age_layout)

        
        weight_layout = QHBoxLayout()
        weight_label = QLabel("Weight:")
        self.weight_input = QLineEdit()
        self.weight_unit = QComboBox()
        self.weight_unit.addItems(["kilograms", "pounds"])
        weight_layout.addWidget(weight_label)
        weight_layout.addWidget(self.weight_input)
        weight_layout.addWidget(self.weight_unit)
        main_layout.addLayout(weight_layout)

        
        height_layout = QHBoxLayout()
        height_label = QLabel("Height:")
        self.height_input = QLineEdit()
        self.height_unit = QComboBox()
        self.height_unit.addItems(["centimeters", "inches"])
        height_layout.addWidget(height_label)
        height_layout.addWidget(self.height_input)
        height_layout.addWidget(self.height_unit)
        main_layout.addLayout(height_layout)

        
        btn_layout = QHBoxLayout()
        self.clear_btn = QPushButton("Clear")
        self.calc_btn = QPushButton("Submit Registration")
        btn_layout.addWidget(self.clear_btn)
        btn_layout.addWidget(self.calc_btn)
        main_layout.addLayout(btn_layout)

        
        self.result_container = QWidget()
        self.result_container.setStyleSheet("background-color: #FAF0E6;")
        result_layout = QVBoxLayout()

        self.result_label = QLabel("Your BMI")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.bmi_value = QLabel("0.00")
        self.bmi_value.setAlignment(Qt.AlignCenter)
        self.bmi_value.setStyleSheet("""
            font-size: 28px;
            color: #4B5BDC;
            font-weight: bold;
        """)

        
        self.table_widget = QWidget()

        outer_table_layout = QHBoxLayout()
        outer_table_layout.setAlignment(Qt.AlignCenter)

        table_layout = QHBoxLayout()
        table_layout.setSpacing(25)

        bmi_column = QVBoxLayout()
        bmi_title = QLabel("BMI")
        bmi_title.setStyleSheet("font-weight: bold;")
        bmi_column.addWidget(bmi_title)
        bmi_column.addWidget(QLabel("< 18.5"))
        bmi_column.addWidget(QLabel("18.5 - 25.0"))
        bmi_column.addWidget(QLabel("25.1 - 30.0"))
        bmi_column.addWidget(QLabel("> 30.0"))

        condition_column = QVBoxLayout()
        condition_title = QLabel("Condition")
        condition_title.setStyleSheet("font-weight: bold;")
        condition_column.addWidget(condition_title)
        condition_column.addWidget(QLabel("Thin"))
        condition_column.addWidget(QLabel("Normal"))
        condition_column.addWidget(QLabel("Overweight"))
        condition_column.addWidget(QLabel("Obese"))

        table_layout.addLayout(bmi_column)
        table_layout.addLayout(condition_column)

        outer_table_layout.addLayout(table_layout)
        self.table_widget.setLayout(outer_table_layout)
        self.table_widget.hide()

        
        self.child_widget = QWidget()
        child_layout = QVBoxLayout()
        child_layout.setAlignment(Qt.AlignCenter)

        info_label = QLabel(
            "For child's BMI interpretation, please click one of the following links."
        )
        info_label.setWordWrap(True)
        info_label.setAlignment(Qt.AlignCenter)

        boys_link = QLabel('<a href="https://www.nhs.uk/">BMI graph for BOYS</a>')
        boys_link.setOpenExternalLinks(True)
        boys_link.setAlignment(Qt.AlignCenter)

        girls_link = QLabel('<a href="https://www.nhs.uk/">BMI graph for GIRLS</a>')
        girls_link.setOpenExternalLinks(True)
        girls_link.setAlignment(Qt.AlignCenter)

        child_layout.addWidget(info_label)
        child_layout.addSpacing(5)
        child_layout.addWidget(boys_link)
        child_layout.addWidget(girls_link)

        self.child_widget.setLayout(child_layout)
        self.child_widget.hide()

        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.bmi_value)
        result_layout.addSpacing(15)
        result_layout.addWidget(self.table_widget)
        result_layout.addWidget(self.child_widget)
        result_layout.addStretch()

        self.result_container.setLayout(result_layout)
        main_layout.addWidget(self.result_container)

        self.setLayout(main_layout)

        
        self.calc_btn.clicked.connect(self.calculate_bmi)
        self.clear_btn.clicked.connect(self.clear_fields)

    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            if self.weight_unit.currentText() == "pounds":
                weight *= 0.453592

            if self.height_unit.currentText() == "inches":
                height *= 2.54

            height_m = height / 100
            bmi = weight / (height_m ** 2)

            self.bmi_value.setText(f"{bmi:.2f}")

            if self.age_combo.currentText() == "Adults 20+":
                self.table_widget.show()
                self.child_widget.hide()
            else:
                self.table_widget.hide()
                self.child_widget.show()

        except:
            self.bmi_value.setText("Error")
            self.table_widget.hide()
            self.child_widget.hide()

    
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_value.setText("0.00")
        self.table_widget.hide()
        self.child_widget.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())
