# Name: Wirithipa Duangchan
# Student ID: 673040468-9

import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QLineEdit, QSpinBox,
    QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView
)
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QColor


class GradeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Grade Calculator")
        self.resize(950, 620)

        self.students = {}
        self.setup_ui()
        self.load_students()

    #UI
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        #Input Layout
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)

        self.id_combo = QComboBox()
        self.id_combo.currentIndexChanged.connect(self.update_name)

        self.name_edit = QLineEdit()
        self.name_edit.setReadOnly(True)

        
        english_locale = QLocale(QLocale.English, QLocale.UnitedStates)

        self.math_spin = QSpinBox()
        self.math_spin.setRange(0, 100)
        self.math_spin.setLocale(english_locale)
        self.math_spin.setButtonSymbols(QSpinBox.UpDownArrows)
        self.math_spin.setAlignment(Qt.AlignCenter)

        self.science_spin = QSpinBox()
        self.science_spin.setRange(0, 100)
        self.science_spin.setLocale(english_locale)
        self.science_spin.setButtonSymbols(QSpinBox.UpDownArrows)
        self.science_spin.setAlignment(Qt.AlignCenter)

        self.english_spin = QSpinBox()
        self.english_spin.setRange(0, 100)
        self.english_spin.setLocale(english_locale)
        self.english_spin.setButtonSymbols(QSpinBox.UpDownArrows)
        self.english_spin.setAlignment(Qt.AlignCenter)

        input_layout.addWidget(QLabel("Student ID"))
        input_layout.addWidget(self.id_combo)
        input_layout.addWidget(QLabel("Name"))
        input_layout.addWidget(self.name_edit)
        input_layout.addWidget(QLabel("Math"))
        input_layout.addWidget(self.math_spin)
        input_layout.addWidget(QLabel("Science"))
        input_layout.addWidget(self.science_spin)
        input_layout.addWidget(QLabel("English"))
        input_layout.addWidget(self.english_spin)

        main_layout.addLayout(input_layout)

        #Buttons
        button_layout = QHBoxLayout()

        self.add_btn = QPushButton("Add Student")
        self.reset_btn = QPushButton("Reset Input")
        self.clear_btn = QPushButton("Clear All")

        self.add_btn.clicked.connect(self.add_student)
        self.reset_btn.clicked.connect(self.reset_inputs)
        self.clear_btn.clicked.connect(self.clear_table)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.reset_btn)
        button_layout.addWidget(self.clear_btn)

        main_layout.addLayout(button_layout)

        #Table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Student ID", "Name", "Math",
            "Science", "English",
            "Total", "Average", "Grade"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        main_layout.addWidget(self.table)

        central.setLayout(main_layout)
        self.apply_styles()

    #Load Students
    def load_students(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, "students.txt")

        if not os.path.exists(file_path):
            QMessageBox.critical(self, "Error", "students.txt file not found")
            return

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                sid, name = line.strip().split(",")
                self.students[sid] = name
                self.id_combo.addItem(sid)

    #Update Name
    def update_name(self):
        sid = self.id_combo.currentText()
        if sid in self.students:
            self.name_edit.setText(self.students[sid])

    #Grade Logic
    def calculate_grade(self, avg):
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    #Add Student
    def add_student(self):
        sid = self.id_combo.currentText()

        
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).text() == sid:
                QMessageBox.warning(self, "Duplicate",
                                    "This student ID is already added.")
                return

        name = self.name_edit.text()
        math = self.math_spin.value()
        science = self.science_spin.value()
        english = self.english_spin.value()

        total = math + science + english
        average = total / 3
        grade = self.calculate_grade(average)

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        values = [
            sid, name, str(math), str(science),
            str(english), str(total),
            f"{average:.2f}", grade
        ]

        for col, value in enumerate(values):
            item = QTableWidgetItem(value)

           
            if col >= 2:
                item.setTextAlignment(Qt.AlignCenter)

            
            if col in [2, 3, 4] and int(value) < 50:
                item.setBackground(QColor("#f5b5b5"))
                item.setForeground(Qt.black)

            
            if col == 7 and value == "F":
                item.setBackground(QColor("#f5b5b5"))
                item.setForeground(Qt.black)

            
            if col == 7 and value == "A":
                item.setBackground(QColor("#b6e3b6"))
                item.setForeground(Qt.black)

            self.table.setItem(row_position, col, item)

        self.table.sortItems(0, Qt.AscendingOrder)

    #Reset Inputs
    def reset_inputs(self):
        self.id_combo.setCurrentIndex(0)
        self.math_spin.setValue(0)
        self.science_spin.setValue(0)
        self.english_spin.setValue(0)

    #Clear Table
    def clear_table(self):
        self.table.setRowCount(0)

    #Style
    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fb;
            }

            QLabel {
                color: #444444;
                font-size: 13px;
            }

            QLineEdit, QComboBox, QSpinBox {
                background-color: white;
                border: 1px solid #e3e6eb;
                border-radius: 8px;
                padding: 6px;
            }

            QPushButton {
                padding: 8px 16px;
                border-radius: 10px;
                font-weight: 500;
                border: none;
                background-color: #ffd6e5;
            }

            QPushButton:hover {
                background-color: #ffc2da;
            }

            QTableWidget {
                background-color: white;
                border: 1px solid #e3e6eb;
                gridline-color: #f0f0f0;
                border-radius: 10px;
            }

            QHeaderView::section {
                background-color: #eef5ff;
                padding: 6px;
                font-weight: 600;
                color: #444444;
                border: none;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradeApp()
    window.show()
    sys.exit(app.exec())
