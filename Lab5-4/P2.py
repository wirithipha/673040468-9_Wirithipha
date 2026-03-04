# Name: Wirithipa Duangchan
# Student ID: 673040468-9

import sys
import random

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QTextEdit, QFileDialog,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QSlider, QToolBar, QStatusBar, QFrame
)

from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


class CharacterBuilder(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RPG Character Builder")
        self.resize(760,420)

        self.setup_ui()
        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()


    def setup_ui(self):

        main_widget = QWidget()
        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        form_layout = QGridLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter character name...")

        self.race = QComboBox()
        self.race.addItems([
            "Choose race",
            "Human","Elf","Dwarf","Orc","Undead"
        ])

        self.cls = QComboBox()
        self.cls.addItems([
            "Choose class",
            "Warrior","Mage","Rogue","Paladin","Ranger"
        ])

        self.gender = QComboBox()
        self.gender.addItems([
            "Choose gender",
            "Male","Female","Other"
        ])

        form_layout.addWidget(QLabel("Character Name:"),0,0)
        form_layout.addWidget(self.name_edit,0,1)

        form_layout.addWidget(QLabel("Race:"),1,0)
        form_layout.addWidget(self.race,1,1)

        form_layout.addWidget(QLabel("Class:"),2,0)
        form_layout.addWidget(self.cls,2,1)

        form_layout.addWidget(QLabel("Gender:"),3,0)
        form_layout.addWidget(self.gender,3,1)

        left_layout.addLayout(form_layout)


        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        left_layout.addWidget(line)


        stat_title = QLabel("Stat Allocation")
        stat_title.setStyleSheet(
            "color:#6a3fb5;font-weight:bold"
        )

        left_layout.addWidget(stat_title)

        stat_layout = QGridLayout()

        self.str_slider = QSlider(Qt.Horizontal)
        self.dex_slider = QSlider(Qt.Horizontal)
        self.int_slider = QSlider(Qt.Horizontal)
        self.vit_slider = QSlider(Qt.Horizontal)

        sliders = [
            ("⚔ STR",self.str_slider),
            ("🏹 DEX",self.dex_slider),
            ("🔮 INT",self.int_slider),
            ("🖤 VIT",self.vit_slider)
        ]

        self.value_labels=[]

        for i,(name,slider) in enumerate(sliders):

            slider.setRange(1,20)
            slider.setValue(5)

            slider.setStyleSheet("""
            QSlider::groove:horizontal{
                height:6px;
                background:#d0d0d0;
                border-radius:3px;
            }

            QSlider::handle:horizontal{
                background:#2d7dd2;
                width:14px;
                margin:-4px 0;
                border-radius:3px;
            }
            """)

            value = QLabel("5")

            self.value_labels.append(value)

            slider.valueChanged.connect(self.update_points)

            stat_layout.addWidget(QLabel(name),i,0)
            stat_layout.addWidget(slider,i,1)
            stat_layout.addWidget(value,i,2)

        left_layout.addLayout(stat_layout)


        self.points = QLabel("Points used: 20 / 40")
        left_layout.addWidget(self.points)


        self.generate_btn = QPushButton("⚔ Generate Character Sheet")

        self.generate_btn.setStyleSheet("""
        QPushButton{
            border:2px solid #8b6bd6;
            border-radius:6px;
            padding:8px;
            background:#f5f3ff;
            font-weight:600;
        }
        """)

        self.generate_btn.clicked.connect(self.generate_sheet)

        left_layout.addWidget(self.generate_btn)

        left_layout.addStretch()


        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setFixedWidth(250)

        self.display.setStyleSheet("""
        QTextEdit{
            background:#1b1b2f;
            color:white;
            font-family:monospace;
            padding:20px;
            border-radius:18px;
        }
        """)

        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.display)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


    def create_menu(self):

        menu = self.menuBar()

        game = menu.addMenu("Game")

        new = QAction("📄 New Character",self)
        new.triggered.connect(self.new_character)

        gen = QAction("⚔ Generate Sheet",self)
        gen.triggered.connect(self.generate_sheet)

        save = QAction("💾 Save Sheet",self)
        save.triggered.connect(self.save_sheet)

        exit = QAction("❌ Exit",self)
        exit.triggered.connect(self.close)

        game.addActions([new,gen,save,exit])

        edit = menu.addMenu("Edit")

        reset = QAction("🔄 Reset Stats",self)
        reset.triggered.connect(self.reset_stats)

        rand = QAction("🎲 Randomize",self)
        rand.triggered.connect(self.randomize)

        edit.addActions([reset,rand])


    def create_toolbar(self):

        tb = QToolBar()

        new = QAction("📄 New",self)
        new.triggered.connect(self.new_character)

        gen = QAction("⚔ Generate",self)
        gen.triggered.connect(self.generate_sheet)

        rand = QAction("🎲 Randomize",self)
        rand.triggered.connect(self.randomize)

        save = QAction("💾 Save",self)
        save.triggered.connect(self.save_sheet)

        tb.addActions([new,gen,rand,save])

        self.addToolBar(tb)



    def create_statusbar(self):

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.status.showMessage("Ready — create your character")

        self.status.addPermanentWidget(
            QLabel("Created by YourName")
        )



    def get_values(self):

        return [
            self.str_slider.value(),
            self.dex_slider.value(),
            self.int_slider.value(),
            self.vit_slider.value()
        ]


    def update_points(self):

        values = self.get_values()

        for i,v in enumerate(values):
            self.value_labels[i].setText(str(v))

        total = sum(values)

        if total > 40:
            self.points.setStyleSheet("color:red")
        else:
            self.points.setStyleSheet("color:black")

        self.points.setText(f"Points used: {total} / 40")


    def generate_sheet(self):

        name = self.name_edit.text()
        if name == "":
            name = "Character Name"

        race = self.race.currentText()
        cls = self.cls.currentText()

        values = self.get_values()

        def bar(value):

            max_stat = 20
            bar_length = 14

            filled = int((value/max_stat)*bar_length)

            return "█"*filled + "░"*(bar_length-filled)

        sheet = f"""
<center>

<span style="color:#c7a6ff;font-size:16pt;font-weight:600;">
— {name} —
</span>

<br>

<span style="color:#9db3ff;">
{race} • {cls}
</span>

<hr style="border:1px solid #444;width:90%;">

<pre style="font-family:monospace;color:#d0d6ff;">

STR  {bar(values[0])}  —

DEX  {bar(values[1])}  —

INT  {bar(values[2])}  —

VIT  {bar(values[3])}  —

</pre>

</center>
"""

        self.display.setHtml(sheet)

        self.status.showMessage("Character generated",3000)



    def save_sheet(self):

        file,_ = QFileDialog.getSaveFileName(
            self,"Save","","Text Files (*.txt)"
        )

        if file:
            with open(file,"w") as f:
                f.write(self.display.toPlainText())



    def new_character(self):

        self.name_edit.clear()
        self.display.clear()
        self.reset_stats()



    def reset_stats(self):

        self.str_slider.setValue(5)
        self.dex_slider.setValue(5)
        self.int_slider.setValue(5)
        self.vit_slider.setValue(5)

        self.update_points()



    def randomize(self):

        while True:

            vals = [random.randint(1,20) for _ in range(4)]

            if sum(vals) <= 40:
                break

        self.str_slider.setValue(vals[0])
        self.dex_slider.setValue(vals[1])
        self.int_slider.setValue(vals[2])
        self.vit_slider.setValue(vals[3])

        self.update_points()


app = QApplication(sys.argv)

window = CharacterBuilder()
window.show()

sys.exit(app.exec())