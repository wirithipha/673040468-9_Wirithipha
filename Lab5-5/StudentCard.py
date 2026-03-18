from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QFrame,
)
from PySide6.QtCore import Qt, Signal, QMimeData, QPoint
from PySide6.QtGui import QFont, QCursor, QDrag, QPixmap
 
 
# รับ C มาจาก P2.py ตอน import
C: dict = {}
 
def set_colors(colors: dict):
    global C
    C = colors
 
 
class StudentCard(QFrame):
 
    delete_requested = Signal(object)
 
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)
        self.data = data
        self._drag_start: QPoint | None = None
        self.setAcceptDrops(False)
        self.setCursor(QCursor(Qt.OpenHandCursor))
        self._build()
 
    def _build(self):
        courses = [
            self.data.get(k, "")
            for k in ("course1", "course2", "course3")
            if self.data.get(k, "")
        ]
 
        self.setMinimumHeight(70 + len(courses) * 20)
        self.setStyleSheet(f"""
            QFrame {{
                background:{C['card']};
            }}
            QFrame:hover {{
                background:{C['surface']};
            }}
        """)
 
        outer = QHBoxLayout(self)
        outer.setContentsMargins(12, 10, 12, 10)
        outer.setSpacing(8)
 
        handle = QLabel("⠿")
        handle.setFixedWidth(16)
        handle.setAlignment(Qt.AlignTop)
        handle.setStyleSheet(
            f"background:transparent; color:{C['muted']};"
            f"font-size:18px; padding-top:2px;"
        )
 
        info = QVBoxLayout()
        info.setSpacing(2)
 
        name_row = QHBoxLayout()
        fullname = f"{self.data.get('first_name','')} {self.data.get('last_name','')}".strip()
        self.data['fullname'] = fullname
 
        lbl_name = QLabel(fullname)
        lbl_name.setFont(QFont("Segoe UI", 11, QFont.Bold))
        lbl_name.setStyleSheet(f"color:{C['text']};")
 
        lbl_sid = QLabel(self.data.get("student_id", ""))
        lbl_sid.setStyleSheet(f"color:{C['muted']}; font-size:12px; margin-left:8px;")
 
        name_row.addWidget(lbl_name)
        name_row.addWidget(lbl_sid)
        name_row.addStretch()
 
        dept = f"{self.data.get('faculty','')}  ·  {self.data.get('major','')}"
        lbl_dept = QLabel(dept)
        lbl_dept.setStyleSheet(f"color:{C['muted']}; font-size:12px;")
 
        info.addLayout(name_row)
        info.addWidget(lbl_dept)
 
        for c in courses:
            lbl_c = QLabel(c)
            lbl_c.setStyleSheet(f"color:{C['text']}; font-size:12px;")
            info.addWidget(lbl_c)
 
        btn_del = QPushButton("✕")
        btn_del.setFixedSize(28, 28)
        btn_del.setCursor(QCursor(Qt.PointingHandCursor))
        btn_del.setStyleSheet(f"""
            QPushButton {{
                background:transparent;
                color:{C['muted']};
                border:none;
                border-radius:14px;
                font-size:11px;
                font-weight:bold;
            }}
            QPushButton:hover {{
                background:{C['red']};
                color:white;
                border:none;
            }}
        """)
        btn_del.clicked.connect(lambda: self.delete_requested.emit(self))
 
        outer.addWidget(handle)
        outer.addLayout(info, 1)
        outer.addWidget(btn_del, 0, Qt.AlignTop)
 
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_start = event.pos()
        super().mousePressEvent(event)
 
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self._drag_start is not None:
            if (event.pos() - self._drag_start).manhattanLength() > 10:
                drag = QDrag(self)
                mime = QMimeData()
                mime.setText("student_card")
                drag.setMimeData(mime)
                pix = QPixmap(self.size())
                pix.fill(Qt.transparent)
                self.render(pix)
                drag.setPixmap(pix)
                drag.setHotSpot(event.pos())
                drag.exec(Qt.MoveAction)
        super().mouseMoveEvent(event)