# Name: Wirithipa Duangchan
# Student ID: 673040468-9
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout, QScrollArea,
    QLabel, QLineEdit, QPushButton, QComboBox, QFrame,
    QMessageBox,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QCursor
 
from StudentCard import StudentCard, set_colors
 
COURSES = [
    "CS101 · Intro to Programming",
    "CS102 · Data Structures",
    "CS201 · Algorithms",
    "CS202 · Database Systems",
    "MATH101 · Calculus I",
    "MATH102 · Calculus II",
    "EN101 · English for Engineers",
    "PHY101 · Physics I",
]

C = {
    "bg":      "#ffffff",
    "surface": "#f0bcab",
    "card":    "#efd0d0",
    "border":  "#dee2e6",
    "accent":  "#2563eb",
    "purple":  "#7c3aed",
    "green":   "#16a34a",
    "red":     "#dc2626",
    "text":    "#111827",
    "muted":   "#6b7280",
    "gold":    "#d97706",
}
 
set_colors(C)  # ส่ง colors ให้ StudentCard
 
BASE = (
    f"background-color:{C['bg']};"
    f"color:{C['text']};"
    f"font-family:'Segoe UI','Helvetica Neue',sans-serif;"
)
 
INPUT_SS = f"""
QLineEdit {{
    background:{C['bg']};
    border:1px solid {C['border']};
    border-radius:6px;
    padding:8px 12px;
    color:{C['text']};
    font-size:13px;
}}
QLineEdit:focus {{
    border:1.5px solid {C['accent']};
}}
"""
 
COMBO_SS = f"""
QComboBox {{
    background:{C['bg']};
    border:1px solid {C['border']};
    border-radius:6px;
    padding:8px 12px;
    color:{C['text']};
    font-size:13px;
}}
QComboBox:focus {{
    border:1.5px solid {C['accent']};
}}
QComboBox::drop-down {{
    border:none;
    width:24px;
}}
QComboBox QAbstractItemView {{
    background:{C['bg']};
    border:1px solid {C['border']};
    color:{C['text']};
    selection-background-color:{C['accent']};
    selection-color:white;
    padding:4px;
}}
"""
 
SCROLL_SS = f"""
QScrollArea {{
    border:none;
    background:transparent;
}}
QScrollBar:vertical {{
    background:{C['surface']};
    width:6px;
    border-radius:3px;
}}
QScrollBar::handle:vertical {{
    background:{C['border']};
    border-radius:3px;
    min-height:30px;
}}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height:0;
}}
"""
 
 
def btn_ss(bg: str, hover: str, fg: str = "#ffffff", border: str = "none") -> str:
    return f"""
        QPushButton {{
            background:{bg}; color:{fg};
            border:{border};
            border-radius:6px; padding:8px 20px;
            font-size:13px; font-weight:600;
        }}
        QPushButton:hover {{ background:{hover}; }}
    """
 
 
def section_label(text: str) -> QLabel:
    lbl = QLabel(text)
    lbl.setStyleSheet(
        f"color:{C['muted']};font-size:11px;font-weight:700;"
        f"letter-spacing:0.5px;text-transform:uppercase;"
    )
    return lbl
 
 
def field_label(text: str) -> QLabel:
    lbl = QLabel(text)
    lbl.setStyleSheet(f"color:{C['text']};font-size:13px;")
    lbl.setFixedWidth(110)
    return lbl
 
 
def divider() -> QFrame:
    line = QFrame()
    line.setFrameShape(QFrame.HLine)
    line.setStyleSheet(f"border:none; border-top:1px solid {C['border']};")
    line.setFixedHeight(1)
    return line

class StudentListPage(QWidget):
 
    go_to_add = Signal()
 
    def __init__(self):
        super().__init__()
        self._cards: list[StudentCard] = []
        self.setAcceptDrops(True)
        self._build()
 
    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
 
        bar = QFrame()
        bar.setFixedHeight(64)
        bar.setStyleSheet(
            f"background:{C['bg']}; border-bottom:1px solid {C['border']};"
        )
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(32, 0, 32, 0)
 
        title = QLabel("Students")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet(f"color:{C['text']};")
 
        self.lbl_count = QLabel("0 enrolled")
        self.lbl_count.setStyleSheet(f"color:{C['muted']};font-size:13px;")
 
        btn_add = QPushButton("+ Add Student")
        btn_add.setCursor(QCursor(Qt.PointingHandCursor))
        btn_add.setStyleSheet(btn_ss(C['accent'], "#1d4ed8"))
        btn_add.clicked.connect(self.go_to_add.emit)
 
        bl.addWidget(title)
        bl.addSpacing(12)
        bl.addWidget(self.lbl_count, alignment=Qt.AlignVCenter)
        bl.addStretch()
        bl.addWidget(btn_add)
 
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setStyleSheet(SCROLL_SS)
 
        self._container = QWidget()
        self._container.setStyleSheet(f"background:{C['bg']};")
        self._card_lay = QVBoxLayout(self._container)
        self._card_lay.setContentsMargins(32, 16, 32, 16)
        self._card_lay.setSpacing(8)
        self._card_lay.addStretch()
 
        self._scroll.setWidget(self._container)
 
        self._lbl_empty = QLabel("No students yet.\nClick '+ Add Student' to begin.")
        self._lbl_empty.setAlignment(Qt.AlignCenter)
        self._lbl_empty.setStyleSheet(f"color:{C['muted']};font-size:14px;")
 
        root.addWidget(bar)
        root.addWidget(self._lbl_empty, stretch=1)
        root.addWidget(self._scroll, stretch=1)
 
        self._refresh_empty()
 
    def add_student(self, data: dict):
        card = StudentCard(data)
        card.delete_requested.connect(self._remove_card)
        self._cards.append(card)
        self._card_lay.insertWidget(self._card_lay.count() - 1, card)
        self._refresh_count()
        self._refresh_empty()
 
    def _remove_card(self, card: StudentCard):
        reply = QMessageBox.question(
            self, "Remove student",
            f"Remove {card.data['fullname']}?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self._cards.remove(card)
            self._card_lay.removeWidget(card)
            card.deleteLater()
            self._refresh_count()
            self._refresh_empty()
 
    def _refresh_count(self):
        n = len(self._cards)
        self.lbl_count.setText(f"{n} enrolled")
 
    def _refresh_empty(self):
        has = bool(self._cards)
        self._lbl_empty.setVisible(not has)
        self._scroll.setVisible(has)
 
    def dragEnterEvent(self, event):
        if event.mimeData().hasText() and event.mimeData().text() == "student_card":
            event.acceptProposedAction()
 
    def dragMoveEvent(self, event):
        event.acceptProposedAction()
 
    def dropEvent(self, event):
        src = event.source()
        if not isinstance(src, StudentCard) or src not in self._cards:
            return
 
        local_y = self._container.mapFrom(self, event.position().toPoint()).y()
        target = len(self._cards) - 1
        for i, card in enumerate(self._cards):
            if local_y < card.y() + card.height() // 2:
                target = i
                break
 
        src_idx = self._cards.index(src)
        if src_idx == target:
            return
 
        self._cards.pop(src_idx)
        self._cards.insert(target, src)
        for card in self._cards:
            self._card_lay.removeWidget(card)
        for i, card in enumerate(self._cards):
            self._card_lay.insertWidget(i, card)
 
        event.acceptProposedAction()

class AddStudentPage(QWidget):
 
    go_cancel = Signal()
    go_review = Signal(dict)
 
    def __init__(self):
        super().__init__()
        self._build()
 
    def _inp(self, ph: str = "") -> QLineEdit:
        e = QLineEdit()
        e.setPlaceholderText(ph)
        e.setMinimumHeight(38)
        e.setStyleSheet(INPUT_SS)
        return e
 
    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
 
        bar = QFrame()
        bar.setFixedHeight(64)
        bar.setStyleSheet(
            f"background:{C['bg']}; border-bottom:1px solid {C['border']};"
        )
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(32, 0, 32, 0)
        t = QLabel("Add Student")
        t.setFont(QFont("Segoe UI", 16, QFont.Bold))
        t.setStyleSheet(f"color:{C['text']};")
        bl.addWidget(t)
        bl.addStretch()
 
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet(SCROLL_SS)
 
        body = QWidget()
        body.setStyleSheet(f"background:{C['bg']};")
        form = QVBoxLayout(body)
        form.setContentsMargins(40, 28, 40, 28)
        form.setSpacing(20)

        form.addWidget(section_label("Personal Information"))
 
        self._sid = self._inp("e.g. 65010001")
        sid_row = QHBoxLayout()
        sid_col = QVBoxLayout()
        sid_col.setSpacing(4)
        sid_col.addWidget(field_label("Student ID *"))
        sid_col.addWidget(self._sid)
        sid_row.addLayout(sid_col)
        sid_row.addStretch()
        form.addLayout(sid_row)
 
        self._fname = self._inp("First name")
        self._lname = self._inp("Last name")
        name_row = QHBoxLayout()
        name_row.setSpacing(16)
        for lbl_txt, widget in [("First Name *", self._fname), ("Last Name *", self._lname)]:
            col = QVBoxLayout()
            col.setSpacing(4)
            col.addWidget(field_label(lbl_txt))
            col.addWidget(widget)
            name_row.addLayout(col)
        form.addLayout(name_row)
 
        self._faculty = self._inp("e.g. Science & Technology")
        self._major   = self._inp("e.g. Computer Science")
        fac_row = QHBoxLayout()
        fac_row.setSpacing(16)
        for lbl_txt, widget in [("Faculty *", self._faculty), ("Major *", self._major)]:
            col = QVBoxLayout()
            col.setSpacing(4)
            col.addWidget(field_label(lbl_txt))
            col.addWidget(widget)
            fac_row.addLayout(col)
        form.addLayout(fac_row)
 
        form.addWidget(divider())

        form.addWidget(section_label("Course Selection  (choose 1–3)"))
 
        self._c1 = QComboBox(); self._c1.setStyleSheet(COMBO_SS)
        self._c2 = QComboBox(); self._c2.setStyleSheet(COMBO_SS)
        self._c3 = QComboBox(); self._c3.setStyleSheet(COMBO_SS)
 
        for combo in (self._c1, self._c2, self._c3):
            combo.addItem("— Select Course —")
            combo.addItems(COURSES)
            combo.setMinimumHeight(38)
 
        for lbl_txt, combo in [("Course 1", self._c1), ("Course 2", self._c2), ("Course 3", self._c3)]:
            row = QHBoxLayout()
            row.setSpacing(16)
            lbl = QLabel(lbl_txt)
            lbl.setFixedWidth(80)
            lbl.setStyleSheet(f"color:{C['text']};font-size:13px;")
            row.addWidget(lbl)
            row.addWidget(combo)
            form.addLayout(row)
 
        self.lbl_err = QLabel("")
        self.lbl_err.setStyleSheet(f"color:{C['red']};font-size:13px;")
        form.addWidget(self.lbl_err)
 
        form.addStretch()
 
        btn_row = QHBoxLayout()
        bc = QPushButton("← Cancel")
        bc.setCursor(QCursor(Qt.PointingHandCursor))
        bc.setStyleSheet(btn_ss(C['bg'], C['surface'], C['muted'], border=f"1px solid {C['border']}"))
        bc.clicked.connect(self._on_cancel)
 
        br = QPushButton("Review →")
        br.setCursor(QCursor(Qt.PointingHandCursor))
        br.setStyleSheet(btn_ss(C['accent'], "#1d4ed8"))
        br.clicked.connect(self._on_review)
 
        btn_row.addWidget(bc)
        btn_row.addStretch()
        btn_row.addWidget(br)
        form.addLayout(btn_row)
 
        scroll.setWidget(body)
        root.addWidget(bar)
        root.addWidget(scroll, stretch=1)
 
    def _on_cancel(self):
        self.clear_form()
        self.go_cancel.emit()
 
    def _on_review(self):
        errors = []
        if not self._sid.text().strip():     errors.append("Student ID")
        if not self._fname.text().strip():   errors.append("First Name")
        if not self._lname.text().strip():   errors.append("Last Name")
        if not self._faculty.text().strip(): errors.append("Faculty")
        if not self._major.text().strip():   errors.append("Major")
        if self._c1.currentIndex() == 0:     errors.append("at least 1 course")
 
        if errors:
            self.lbl_err.setText("Required: " + ",  ".join(errors))
            return
 
        self.lbl_err.setText("")
        self.go_review.emit({
            "student_id": self._sid.text().strip(),
            "first_name":  self._fname.text().strip(),
            "last_name":   self._lname.text().strip(),
            "faculty":     self._faculty.text().strip(),
            "major":       self._major.text().strip(),
            "course1":     self._c1.currentText() if self._c1.currentIndex() > 0 else "",
            "course2":     self._c2.currentText() if self._c2.currentIndex() > 0 else "",
            "course3":     self._c3.currentText() if self._c3.currentIndex() > 0 else "",
        })
 
    def load_data(self, d: dict):
        self._sid.setText(d.get("student_id", ""))
        self._fname.setText(d.get("first_name", ""))
        self._lname.setText(d.get("last_name", ""))
        self._faculty.setText(d.get("faculty", ""))
        self._major.setText(d.get("major", ""))
        for combo, key in [(self._c1,"course1"),(self._c2,"course2"),(self._c3,"course3")]:
            val = d.get(key, "")
            idx = combo.findText(val)
            combo.setCurrentIndex(idx if idx >= 0 else 0)
 
    def clear_form(self):
        for w in (self._sid, self._fname, self._lname, self._faculty, self._major):
            w.clear()
        for c in (self._c1, self._c2, self._c3):
            c.setCurrentIndex(0)
        self.lbl_err.setText("")

class ReviewPage(QWidget):
 
    go_edit    = Signal(dict)
    go_confirm = Signal(dict)
 
    def __init__(self):
        super().__init__()
        self._data: dict = {}
        self._build()
 
    def _row(self, layout, label: str) -> QLabel:
        row = QHBoxLayout()
        row.setSpacing(0)
        lbl = QLabel(label)
        lbl.setFixedWidth(130)
        lbl.setStyleSheet(f"color:{C['muted']};font-size:13px;")
        val = QLabel("—")
        val.setStyleSheet(f"color:{C['text']};font-size:13px;")
        val.setWordWrap(True)
        row.addWidget(lbl)
        row.addWidget(val, stretch=1)
        layout.addLayout(row)
        return val
 
    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
 
        bar = QFrame()
        bar.setFixedHeight(64)
        bar.setStyleSheet(
            f"background:{C['bg']}; border-bottom:1px solid {C['border']};"
        )
        bl = QHBoxLayout(bar)
        bl.setContentsMargins(32, 0, 32, 0)
        t = QLabel("Review & Confirm")
        t.setFont(QFont("Segoe UI", 16, QFont.Bold))
        t.setStyleSheet(f"color:{C['text']};")
        bl.addWidget(t)
        bl.addStretch()
 
        body = QWidget()
        body.setStyleSheet(f"background:{C['bg']};")
        form = QVBoxLayout(body)
        form.setContentsMargins(40, 28, 40, 28)
        form.setSpacing(12)
 
        form.addWidget(section_label("Student Information"))
        self._v_sid   = self._row(form, "Student ID")
        self._v_name  = self._row(form, "Full Name")
        self._v_fac   = self._row(form, "Faculty")
        self._v_major = self._row(form, "Major")
 
        form.addWidget(divider())
        form.addWidget(section_label("Courses"))
        self._v_c1 = self._row(form, "Course 1")
        self._v_c2 = self._row(form, "Course 2")
        self._v_c3 = self._row(form, "Course 3")
 
        form.addStretch()
 
        btn_row = QHBoxLayout()
        be = QPushButton("← Edit")
        be.setCursor(QCursor(Qt.PointingHandCursor))
        be.setStyleSheet(btn_ss(C['bg'], C['surface'], C['muted'], border=f"1px solid {C['border']}"))
        be.clicked.connect(lambda: self.go_edit.emit(self._data))
 
        bc = QPushButton("Confirm Registration")
        bc.setCursor(QCursor(Qt.PointingHandCursor))
        bc.setStyleSheet(btn_ss(C['green'], "#15803d"))
        bc.clicked.connect(lambda: self.go_confirm.emit(self._data))
 
        btn_row.addWidget(be)
        btn_row.addStretch()
        btn_row.addWidget(bc)
        form.addLayout(btn_row)
 
        root.addWidget(bar)
        root.addWidget(body, stretch=1)
 
    def load_data(self, d: dict):
        self._data = d
        self._v_sid.setText(d.get("student_id", "—"))
        self._v_name.setText(
            f"{d.get('first_name','')} {d.get('last_name','')}".strip() or "—"
        )
        self._v_fac.setText(d.get("faculty", "—"))
        self._v_major.setText(d.get("major", "—"))
        self._v_c1.setText(d.get("course1","") or "—")
        self._v_c2.setText(d.get("course2","") or "—")
        self._v_c3.setText(d.get("course3","") or "—")
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Registration")
        self.setMinimumSize(860, 580)
        self.resize(980, 660)
        self.setStyleSheet(BASE)
        self._build()
 
    def _build(self):
        central = QWidget()
        outer = QVBoxLayout(central)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)
        self.setCentralWidget(central)
 
        self._stack = QStackedWidget()
        self._p1 = StudentListPage()
        self._p2 = AddStudentPage()
        self._p3 = ReviewPage()
 
        self._stack.addWidget(self._p1)   # index 0
        self._stack.addWidget(self._p2)   # index 1
        self._stack.addWidget(self._p3)   # index 2
 
        outer.addWidget(self._stack)

        self._p1.go_to_add.connect(lambda: self._stack.setCurrentIndex(1))
        self._p2.go_cancel.connect(lambda: self._stack.setCurrentIndex(0))
        self._p2.go_review.connect(self._on_review)
        self._p3.go_edit.connect(self._on_edit)
        self._p3.go_confirm.connect(self._on_confirm)
 
    def _on_review(self, data: dict):
        self._p3.load_data(data)
        self._stack.setCurrentIndex(2)
 
    def _on_edit(self, data: dict):
        self._p2.load_data(data)
        self._stack.setCurrentIndex(1)
 
    def _on_confirm(self, data: dict):
        self._p1.add_student(data)
        self._p2.clear_form()
        self._stack.setCurrentIndex(0)
        QMessageBox.information(
            self, "Success",
            f"{data.get('first_name','')} {data.get('last_name','')} registered!"
        )
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec())