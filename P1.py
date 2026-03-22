# Name: Wirithipa Duangchan
# Student ID: 673040468-9

import sys
import json
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtCore import QLocale
QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))


# TASK CARD
class TaskCard(QFrame):

    def __init__(self, task, done_callback):
        super().__init__()

        self.task = task
        self.done_callback = done_callback

        layout = QVBoxLayout()
        layout.setSpacing(20)

        row1 = QHBoxLayout()

        title = QLabel(task["title"])
        title.setStyleSheet("""
        background:#e9ecef;
        padding:8px;
        border-radius:4px;
        font-weight:bold;
        border:none;
        """)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.done_btn = QPushButton("✓ Done")
        self.done_btn.setFixedWidth(80)
        self.done_btn.clicked.connect(self.mark_done)

        row1.addWidget(title,1)
        row1.addWidget(self.done_btn)

        row2 = QHBoxLayout()

        date = QLabel("📅 " + task["deadline"])
        date.setStyleSheet("""
        background:#f1f3f5;
        padding:4px 6px;
        border-radius:4px;
        border:none;
        """)

        self.priority = QLabel(task["priority"].upper())
        self.priority.setAlignment(Qt.AlignCenter)
        self.priority.setFixedWidth(80)

        row2.addWidget(date)
        row2.addStretch()
        row2.addWidget(self.priority)

        layout.addLayout(row1)
        layout.addLayout(row2)

        self.setLayout(layout)

        self.apply_style()

    def apply_style(self):

        styles = {
            "Low": ("#d4edda", "#28a745"),
            "Medium": ("#cfe2ff", "#0d6efd"),
            "High": ("#fff3cd", "#ffc107"),
            "Critical": ("#f8d7da", "#dc3545")
        }

        badge = {
            "Low": "#28a745",
            "Medium": "#0d6efd",
            "High": "#ffc107",
            "Critical": "#dc3545"
        }

        bg, border = styles[self.task["priority"]]
        color = badge[self.task["priority"]]

        self.setStyleSheet(f"""
        QFrame {{
            background:{bg};
            border:2px solid {border};
            border-radius:12px;
            padding:12px;
        }}
        """)

        self.priority.setStyleSheet(f"""
        background:{color};
        color:white;
        padding:4px 10px;
        border-radius:10px;
        font-weight:bold;
        """)

        self.done_btn.setStyleSheet(f"""
        background:white;
        color:{color};
        border:1px solid {color};
        border-radius:6px;
        padding:4px;
        """)

    def mark_done(self):
        self.task["done"] = True
        self.done_callback(self)


# ADD TASK DIALOG
class AddTaskDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add New Task")
        self.resize(320,180)

        layout = QVBoxLayout()

        self.title = QLineEdit()
        self.title.setPlaceholderText("Enter task name...")

        self.priority = QComboBox()
        self.priority.addItems(["Low","Medium","High","Critical"])

        self.deadline = QDateEdit()
        self.deadline.setCalendarPopup(True)
        self.deadline.setDate(QDate.currentDate())
        self.deadline.setDisplayFormat("yyyy-MM-dd")

        form = QFormLayout()
        form.addRow("Task:",self.title)
        form.addRow("Priority:",self.priority)
        form.addRow("Deadline:",self.deadline)

        layout.addLayout(form)

        buttons = QHBoxLayout()

        cancel = QPushButton("Cancel")
        add = QPushButton("Add Task")

        add.setStyleSheet("""
        background:#4a90e2;
        color:white;
        padding:6px;
        border-radius:6px;
        """)

        cancel.clicked.connect(self.reject)
        add.clicked.connect(self.accept)

        buttons.addWidget(cancel)
        buttons.addWidget(add)

        layout.addLayout(buttons)

        self.setLayout(layout)

    def get_data(self):

        return {
            "title":self.title.text(),
            "deadline":self.deadline.date().toString("yyyy-MM-dd"),
            "priority":self.priority.currentText(),
            "done":False
        }


# MAIN WINDOW
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List")
        self.resize(460,520)

        self.tasks = []

        central = QWidget()
        self.setCentralWidget(central)

        main = QVBoxLayout()
        main.setSpacing(10)

        header = QHBoxLayout()

        title = QLabel("My To-Do List")
        title.setStyleSheet("font-size:22px;font-weight:bold")

        self.counter = QLabel("0 tasks")

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.counter)

        main.addLayout(header)

        buttons = QHBoxLayout()

        add = QPushButton("+ Add Task")
        load = QPushButton("📂 Load JSON")
        save = QPushButton("💾 Save JSON")

        add.setStyleSheet("background:#4a90e2;color:white;padding:6px;border-radius:6px")
        load.setStyleSheet("background:#6c757d;color:white;padding:6px;border-radius:6px")
        save.setStyleSheet("background:#28a745;color:white;padding:6px;border-radius:6px")

        add.clicked.connect(self.add_task)
        load.clicked.connect(self.load_json)
        save.clicked.connect(self.save_json)

        buttons.addWidget(add)
        buttons.addWidget(load)
        buttons.addWidget(save)

        main.addLayout(buttons)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color:#cccccc")

        main.addWidget(line)

        # SCROLL AREA
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()
        self.task_layout = QVBoxLayout(self.container)

        self.empty = QLabel("No tasks yet.\nClick + Add Task to get started!")
        self.empty.setAlignment(Qt.AlignCenter)
        self.empty.setStyleSheet("color:gray")

        self.task_layout.addWidget(self.empty)
        self.task_layout.addStretch()

        self.scroll.setWidget(self.container)

        main.addWidget(self.scroll)

        central.setLayout(main)

    def add_task(self):

        dialog = AddTaskDialog()

        if dialog.exec():

            task = dialog.get_data()
            self.tasks.append(task)

            self.add_card(task)
            self.update_counter()

    def add_card(self,task):

        if self.empty.isVisible():
            self.empty.hide()

        card = TaskCard(task,self.finish_task)

        self.task_layout.insertWidget(self.task_layout.count()-1,card)

    def finish_task(self,card):

        card.deleteLater()

        self.update_counter()

        if not any(not t["done"] for t in self.tasks):
            self.empty.show()

    def update_counter(self):

        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])

        if total == 0:
            self.counter.setText("0 tasks")
        else:
            self.counter.setText(f"{done}/{total} done")

    def save_json(self):

        file,_ = QFileDialog.getSaveFileName(
            self,"Save JSON","","JSON (*.json)"
        )

        if file:

            with open(file,"w") as f:
                json.dump(self.tasks,f,indent=4)

    def load_json(self):

        file,_ = QFileDialog.getOpenFileName(
            self,"Load JSON","","JSON (*.json)"
        )

        if file:

            # clear tasks here
            

            with open(file,"r") as f:
                self.tasks = json.load(f)

            for i in reversed(range(self.task_layout.count())):
                item = self.task_layout.itemAt(i)
                widget = item.widget()

                if widget and widget != self.empty:
                    self.task_layout.removeWidget(widget)
                    widget.deleteLater()

            for t in self.tasks:

                if not t["done"]:
                    self.add_card(t)

            if not any(not t["done"] for t in self.tasks):
                self.empty.show()
            else:
                self.empty.hide()

            self.update_counter()

            # Popup ตาม Lab
            QMessageBox.information(self,"Loaded",f"Loaded {len(self.tasks)} tasks.")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())