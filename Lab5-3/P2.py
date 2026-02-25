# Name: Wirithipa Duangchan
# Student ID: 673040468-9

import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QSpinBox,
    QPushButton, QMessageBox
)
from PySide6.QtCore import Qt, QLocale
from PySide6.QtCharts import (
    QChart, QChartView, QBarSeries, QBarSet,
    QBarCategoryAxis, QValueAxis
)


class SalesChartApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Monthly Sales Chart")
        self.resize(950, 600)

        self.data = []
        self.setup_ui()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()

        input_layout = QHBoxLayout()

        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("sales_data.txt")

        self.month_combo = QComboBox()
        self.month_combo.addItems([
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ])

        english_locale = QLocale(QLocale.English, QLocale.UnitedStates)

        self.sales_spin = QSpinBox()
        self.sales_spin.setRange(0, 100000)
        self.sales_spin.setLocale(english_locale)
        self.sales_spin.setAlignment(Qt.AlignCenter)

        self.category_combo = QComboBox()
        self.category_combo.addItems([
            "Electronics", "Clothing", "Food", "Others"
        ])

        input_layout.addWidget(QLabel("Filename"))
        input_layout.addWidget(self.file_input)
        input_layout.addWidget(QLabel("Month"))
        input_layout.addWidget(self.month_combo)
        input_layout.addWidget(QLabel("Sales"))
        input_layout.addWidget(self.sales_spin)
        input_layout.addWidget(QLabel("Category"))
        input_layout.addWidget(self.category_combo)

        main_layout.addLayout(input_layout)

        button_layout = QHBoxLayout()

        self.import_btn = QPushButton("Import Data")
        self.add_btn = QPushButton("Add Data")
        self.clear_btn = QPushButton("Clear Chart")

        self.import_btn.clicked.connect(self.import_data)
        self.add_btn.clicked.connect(self.add_data)
        self.clear_btn.clicked.connect(self.clear_chart)

        button_layout.addWidget(self.import_btn)
        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.clear_btn)

        main_layout.addLayout(button_layout)

        self.chart = QChart()
        self.chart.setTitle("Monthly Sales Report")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view = QChartView(self.chart)
        main_layout.addWidget(self.chart_view)

        central.setLayout(main_layout)


    def import_data(self):
        filename = self.file_input.text()

        if not os.path.exists(filename):
            QMessageBox.warning(self, "Error", "File not found.")
            return

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                month, sales, category = line.strip().split(",")
                self.data.append((month, int(sales), category))

        self.update_chart()


    def add_data(self):
        month = self.month_combo.currentText()
        sales = self.sales_spin.value()
        category = self.category_combo.currentText()

        self.data.append((month, sales, category))
        self.update_chart()


    def clear_chart(self):
        self.data.clear()
        self.chart.removeAllSeries()
        for axis in self.chart.axes():
            self.chart.removeAxis(axis)


    def update_chart(self):

        self.chart.removeAllSeries()
        for axis in self.chart.axes():
            self.chart.removeAxis(axis)

        categories = ["Electronics", "Clothing", "Food", "Others"]
        months = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]

        series = QBarSeries()
        barsets = {}

        for cat in categories:
            barset = QBarSet(cat)
            barset.append([0] * 12)
            barsets[cat] = barset

        for month, sales, category in self.data:
            index = months.index(month)
            current_value = barsets[category].at(index)
            barsets[category].replace(index, current_value + sales)

        for cat in categories:
            series.append(barsets[cat])

        self.chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(months)
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText("Sales Amount")
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)



if __name__ == "__main__":

    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))

    app = QApplication(sys.argv)

    window = SalesChartApp()
    window.show()
    sys.exit(app.exec())