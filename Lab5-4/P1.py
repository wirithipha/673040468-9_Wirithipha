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


from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
                               QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton,
                               QFrame, QSpinBox, QColorDialog, QFileDialog, QToolBar)
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QColor, QAction, QPixmap, QGuiApplication, QIcon
import sys
import os
import re

default_color = "#B0E0E6"

class PersonalCard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Personal Info Card")
        self.setGeometry(100, 100, 420, 550)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        self.input_layout = QFormLayout()
        self.create_form()
        self.main_layout.addLayout(self.input_layout)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        self.main_layout.addWidget(line)

        self.bg_widget = QWidget()
        self.output_layout = QVBoxLayout(self.bg_widget)
        self.create_display()
        self.main_layout.addWidget(self.bg_widget)

        self.create_menu()
        self.create_toolbar()

        self.statusBar().showMessage("Fill in your details and click Generate")


    def create_form(self):
        self.name = QLineEdit()
        self.name.setPlaceholderText("First name and Lastname")

        self.age = QSpinBox()
        self.age.setRange(1,120)
        self.age.setValue(25)
        self.age.setLocale(QLocale(QLocale.Language.English))

        self.email = QLineEdit()
        self.email.setPlaceholderText("username@domain.name")

        self.position = QComboBox()
        self.position.addItems(["Choose your position","Teaching Staff","Supporting Staff","Student","Visitor"])
        self.position.setCurrentIndex(0)


        color_row = QWidget()
        color_layout = QHBoxLayout(color_row)

        self.fav_color = QColor(default_color)

        self.color_swatch = QLabel()
        self.color_swatch.setFixedSize(22,22)
        self.color_swatch.setStyleSheet(
            f"background-color: {self.fav_color.name()}; border:1px solid #888;"
        )

        color_button = QPushButton("Pick New Color")
        color_button.clicked.connect(self.pick_color)

        color_layout.addWidget(self.color_swatch)
        color_layout.addWidget(color_button)

        self.input_layout.addRow("Full name:", self.name)
        self.input_layout.addRow("Age:", self.age)
        self.input_layout.addRow("Email:", self.email)
        self.input_layout.addRow("Position:", self.position)
        self.input_layout.addRow("Favorite color:", color_row)


    def pick_color(self):
        color = QColorDialog.getColor(self.fav_color, self, "Pick a Color")
        if color.isValid():
            self.fav_color = color

            self.color_swatch.setStyleSheet(
                f"background-color:{self.fav_color.name()}; border:1px solid #888;"
            )

            self.bg_widget.setStyleSheet(
                f"background-color:{self.fav_color.name()}; border-radius:6px;"
            )

            self.statusBar().showMessage("Color updated")


    def create_display(self):

        self.bg_widget.setStyleSheet(
            f"background-color:{default_color}; border-radius:6px;"
        )


        text_style = "color:black;"

        self.name_label = QLabel("Your name here")
        self.name_label.setStyleSheet("font-size:18pt; font-weight:bold; color:black;")

        self.age_label = QLabel("(Age)")
        self.age_label.setStyleSheet(text_style)

        self.position_label = QLabel("Your position here")
        self.position_label.setStyleSheet("font-size:14pt; color:black;")


        email_row = QWidget()
        email_layout = QHBoxLayout(email_row)
        email_layout.setContentsMargins(0,0,0,0)
        email_layout.setSpacing(5)
        email_layout.setAlignment(Qt.AlignLeft)

        self.email_icon = QLabel()
        base_path = os.path.dirname(__file__)
        pix = QPixmap(os.path.join(base_path, "email.png"))
        if not pix.isNull():
            self.email_icon.setPixmap(
                pix.scaled(18,18,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            )

        self.email_label = QLabel("your_username@domain.name")
        self.email_label.setStyleSheet(text_style)

        email_layout.addWidget(self.email_icon)
        email_layout.addWidget(self.email_label)

        self.output_layout.addWidget(self.name_label)
        self.output_layout.addWidget(self.age_label)
        self.output_layout.addSpacing(5)
        self.output_layout.addWidget(self.position_label)
        self.output_layout.addSpacing(8)
        self.output_layout.addWidget(email_row)

    def _is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        return re.match(pattern, email) is not None

    def update_display(self):
        if self.name.text() == '':
            print(self.name.text())
            self.statusBar().showMessage("Need valid name")
            return
        #name = self.name.text().strip() 

        if self.position.currentIndex() == -1:
            self.statusBar().showMessage("Please select a position")
            return


        if not self._is_valid_email(self.email.text().strip()):
            self.statusBar().showMessage("Invalid email format (e.g. user@domain.com)")
            return
        
        name = self.name.text().strip()
        age = self.age.value()
        position = self.position.currentText()
        email = self.email.text().strip()  
        #age = self.age.value()
        #position = self.position.currentText() or "Your position here"
        #email = self.email.text().strip() or "your_username@domain.name"

        self.name_label.setText(name)
        self.age_label.setText(f"({age})")
        self.position_label.setText(position)
        self.email_label.setText(email)
        self.bg_widget.setStyleSheet(f"background-color: {self.fav_color.name()}; "
                                     f"border-radius: 6px;")
        self.statusBar().showMessage("Generate card, displaying")

    def save_card(self):
        if self.name_label.text() == "Your name here":
            self.statusBar().showMessage("Please generate card first")
            return

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Card As",
            "my_card.txt",
            "Text Files (*.txt);;All Files (*)"
        )

        if not filename:
            self.statusBar().showMessage("Save cancelled")
            return

        content = (
            f"{self.name_label.text()}\n"
            f"{self.age_label.text()}\n"
            f"{self.position_label.text()}\n"
            f"Email: {self.email_label.text()}"
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        self.statusBar().showMessage(f"Saved to {filename}")


    def copy_card(self):
        text = (
            f"{self.name.text()}\n"
            f"({self.age.value()})\n"
            f"{self.position.currentText()}\n"
            f"Email: {self.email.text()}"
        )
        QGuiApplication.clipboard().setText(text)
        self.statusBar().showMessage("Card copied")

    def clear_form(self):
        self.name.clear()
        self.age.setValue(25)
        self.position.setCurrentIndex(-1)
        self.email.clear()
        self.statusBar().showMessage("Form cleared")

    def clear_display(self):
        self.name_label.setText("Your name here")
        self.age_label.setText("(Age)")
        self.position_label.setText("Your position here")
        self.email_label.setText("your_username@domain.name")
        self.bg_widget.setStyleSheet(
            f"background-color:{default_color}; border-radius:6px;"
        )
        self.statusBar().showMessage("Display cleared")

    def clear_all(self):
        self.clear_form()
        self.clear_display()

    def create_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction("Generate Card", self.update_display)
        file_menu.addAction("Save Card", self.save_card)
        file_menu.addAction("Clear Display", self.clear_display)
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)

        edit_menu = menu.addMenu("Edit")
        edit_menu.addAction("Copy Card", self.copy_card)
        edit_menu.addAction("Clear Form", self.clear_form)

    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(28,28))
        self.addToolBar(toolbar)
        base_path = os.path.dirname(__file__)

        gen_icon = QIcon(os.path.join(base_path, "green.jpg"))
        gen_action = QAction(gen_icon, "Generate Card", self)
        gen_action.triggered.connect(self.update_display)
        toolbar.addAction(gen_action)

        save_icon = QIcon(os.path.join(base_path, "save.jpg"))
        save_action = QAction(save_icon, "Save Card", self)
        save_action.triggered.connect(self.save_card)
        toolbar.addAction(save_action)

        clear_icon = QIcon(os.path.join(base_path, "bin.jpg"))
        clear_action = QAction(clear_icon, "Clear", self)
        clear_action.triggered.connect(self.clear_all)
        toolbar.addAction(clear_action)

def main():
    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.Language.English))

    window = PersonalCard()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()