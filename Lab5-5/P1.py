# Name: Wirithipa Duangchan
# Student ID: 673040468-9

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCore import QLocale

QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))


# -------------------------
# ROOM CARD
# -------------------------
class RoomCard(QWidget):

    clicked = Signal(str, int)

    def __init__(self, icon, name, price, desc, max_guests):
        super().__init__()

        self.name = name
        self.price = price
        self.max_guests = max_guests

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(4)

        icon_label = QLabel(icon)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("font-size:32px")

        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("font-weight:600")

        price_label = QLabel(f"${price} / night")
        price_label.setAlignment(Qt.AlignCenter)

        desc_label = QLabel(desc)
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setStyleSheet("color:gray;font-size:11px")

        self.button = QPushButton("Select Room")
        self.button.setFixedWidth(150)

        self.button.setStyleSheet("""
        QPushButton{
            background:#5b5bd6;
            color:white;
            border-radius:6px;
            padding:6px;
        }
        """)

        self.button.clicked.connect(self.select_room)

        layout.addWidget(icon_label)
        layout.addWidget(name_label)
        layout.addWidget(price_label)
        layout.addWidget(desc_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_room(self):
        self.clicked.emit(self.name, self.price)

    def set_selected(self, selected):

        if selected:
            self.button.setText("✓ Selected")
            self.button.setStyleSheet("""
            QPushButton{
                background:#2bb24c;
                color:white;
                border-radius:6px;
                padding:6px;
                font-weight:600;
            }
            """)
        else:
            self.button.setText("Select Room")
            self.button.setStyleSheet("""
            QPushButton{
                background:#5b5bd6;
                color:white;
                border-radius:6px;
                padding:6px;
            }
            """)


# -------------------------
# CONFIRM MODAL DIALOG
# -------------------------
class ConfirmDialog(QDialog):

    def __init__(self, name, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Booking Confirmed")
        self.setFixedSize(360,220)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(12)

        icon = QLabel("✅")
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet("font-size:40px")

        title = QLabel("Booking Successful!")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
        font-size:18px;
        font-weight:700;
        color:#1fa44a;
        """)

        message = QLabel(f"Dear {name},\nDeluxe Room is ready to welcome you! 🎉")
        message.setAlignment(Qt.AlignCenter)
        message.setStyleSheet("color:gray")

        ok_btn = QPushButton("OK")
        ok_btn.setFixedHeight(36)
        ok_btn.setStyleSheet("""
        QPushButton{
            background:#2bb24c;
            color:white;
            border-radius:10px;
            font-weight:600;
        }
        """)

        ok_btn.clicked.connect(self.accept)

        layout.addWidget(icon)
        layout.addWidget(title)
        layout.addWidget(message)
        layout.addWidget(ok_btn)

        self.setLayout(layout)


# -------------------------
# PAGE 1
# -------------------------
class BookingPage(QWidget):

    def __init__(self, stack):
        super().__init__()

        self.stack = stack
        self.selected_room = None
        self.price = 0

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20,15,20,15)

        title = QLabel("🏨 Book Your Stay at CozyStay")
        title.setStyleSheet("font-size:22px;font-weight:700")

        subtitle = QLabel("Fill in your details and choose your room")
        subtitle.setStyleSheet("color:gray")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        guest_frame = QFrame()
        guest_frame.setStyleSheet("""
        QFrame{
            background:#f6f7fb;
            border-radius:10px;
            padding:10px;
        }
        """)

        guest_layout = QFormLayout()
        guest_layout.setVerticalSpacing(8)

        self.name = QLineEdit()
        self.name.setPlaceholderText("e.g. John Smith")

        self.phone = QLineEdit()
        self.phone.setPlaceholderText("e.g. 081-234-5678")

        self.checkin = QDateEdit()
        self.checkin.setDate(QDate.currentDate())
        self.checkin.setDisplayFormat("dd/MM/yyyy")

        self.checkout = QDateEdit()
        self.checkout.setDate(QDate.currentDate().addDays(1))
        self.checkout.setDisplayFormat("dd/MM/yyyy")

        self.guests = QSpinBox()
        self.guests.setRange(1,10)
        self.guests.setSuffix(" guest(s)")

        guest_layout.addRow("Full Name :", self.name)
        guest_layout.addRow("Phone Number :", self.phone)
        guest_layout.addRow("Check-in Date :", self.checkin)
        guest_layout.addRow("Check-out Date :", self.checkout)
        guest_layout.addRow("Guests :", self.guests)

        guest_frame.setLayout(guest_layout)

        main_layout.addWidget(QLabel("📋 Guest Information"))
        main_layout.addWidget(guest_frame)

        room_layout = QHBoxLayout()
        room_layout.setSpacing(30)

        card1 = RoomCard("🛏","Standard Room",50,"Single bed, Free Wi-Fi",1)
        card2 = RoomCard("🌊","Deluxe Room",120,"Double bed, Ocean view",2)
        card3 = RoomCard("👑","Suite Room",250,"Living room, Jacuzzi",3)
        card4 = RoomCard("👨‍👩‍👧‍👦","Family Room",160,"2 Bedrooms, Perfect for families",4)

        self.cards=[card1,card2,card3,card4]

        for c in self.cards:
            c.clicked.connect(self.select_room)
            room_layout.addWidget(c)

        main_layout.addWidget(QLabel("🛏 Select a Room"))
        main_layout.addLayout(room_layout)

        btn_layout = QHBoxLayout()

        clear_btn = QPushButton("🗑 Clear Info")
        clear_btn.clicked.connect(self.clear_info)

        next_btn = QPushButton("Next →")
        next_btn.clicked.connect(self.go_review)

        btn_layout.addWidget(clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(next_btn)

        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def select_room(self,name,price):

        self.selected_room = name
        self.price = price

        for c in self.cards:
            if c.name == name:
                self.guests.setMaximum(c.max_guests)

            c.set_selected(c.name == name)

    def clear_info(self):

        self.name.clear()
        self.phone.clear()

        self.checkin.setDate(QDate.currentDate())
        self.checkout.setDate(QDate.currentDate().addDays(1))

        self.guests.setValue(1)

        self.selected_room=None
        self.price=0

        for c in self.cards:
            c.set_selected(False)

    def go_review(self):

        if not self.selected_room:
            QMessageBox.warning(self,"Error","Please select a room")
            return

        nights=self.checkin.date().daysTo(self.checkout.date())

        self.stack.review_page.load_data(
            self.name.text(),
            self.phone.text(),
            self.selected_room,
            self.price,
            self.checkin.date(),
            self.checkout.date(),
            nights,
            self.guests.value()
        )

        self.stack.setCurrentIndex(1)


# -------------------------
# PAGE 2
# -------------------------
class ReviewPage(QWidget):

    def __init__(self,stack):
        super().__init__()

        self.stack=stack

        main_layout=QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(30,20,30,20)
        main_layout.setSpacing(12)

        title=QLabel("📄 Booking Summary")
        title.setStyleSheet("font-size:24px;font-weight:700;color:#2f2f6e")

        subtitle=QLabel("Please review your details before confirming")
        subtitle.setStyleSheet("color:#8b8ba7")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        box=QFrame()
        box.setStyleSheet("""
        QFrame{
            background:#f5f6fb;
            border-radius:12px;
            padding:15px;
        }
        """)

        grid=QGridLayout()
        grid.setVerticalSpacing(6)

        self.room=QLabel()
        self.price=QLabel()
        self.name=QLabel()
        self.phone=QLabel()
        self.checkin=QLabel()
        self.checkout=QLabel()
        self.nights=QLabel()
        self.guests=QLabel()

        grid.addWidget(QLabel("🛏️ Room"),0,0)
        grid.addWidget(self.room,0,1)

        grid.addWidget(QLabel("💰 Price / Night"),1,0)
        grid.addWidget(self.price,1,1)

        grid.addWidget(QLabel("👤 Guest Name"),2,0)
        grid.addWidget(self.name,2,1)

        grid.addWidget(QLabel("📞 Phone"),3,0)
        grid.addWidget(self.phone,3,1)

        grid.addWidget(QLabel("📅 Check-in"),4,0)
        grid.addWidget(self.checkin,4,1)

        grid.addWidget(QLabel("📅 Check-out"),5,0)
        grid.addWidget(self.checkout,5,1)

        grid.addWidget(QLabel("🌙 Nights"),6,0)
        grid.addWidget(self.nights,6,1)

        grid.addWidget(QLabel("👥 Guests"),7,0)
        grid.addWidget(self.guests,7,1)

        box.setLayout(grid)

        main_layout.addWidget(box)

        line=QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color:#e2e3ee")

        main_layout.addWidget(line)

        self.total=QLabel()
        self.total.setStyleSheet("font-size:20px;font-weight:700;color:#5b5bd6")

        main_layout.addWidget(self.total,alignment=Qt.AlignRight)

        btn_layout=QHBoxLayout()

        back_btn=QPushButton("← Back")
        back_btn.clicked.connect(lambda:self.stack.setCurrentIndex(0))

        confirm_btn=QPushButton("✔ Confirm Booking")
        confirm_btn.setStyleSheet("""
        QPushButton{
            background:#2bb24c;
            color:white;
            padding:10px 25px;
            border-radius:8px;
            font-weight:600;
        }
        """)

        confirm_btn.clicked.connect(self.confirm)

        btn_layout.addWidget(back_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(confirm_btn)

        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def load_data(self,name,phone,room,price,checkin,checkout,nights,guests):

        self.customer=name

        self.room.setText(room)
        self.price.setText(f"${price}")
        self.name.setText(name)
        self.phone.setText(phone)

        self.checkin.setText(checkin.toString("dd/MM/yyyy"))
        self.checkout.setText(checkout.toString("dd/MM/yyyy"))

        self.nights.setText(f"{nights} night(s)")
        self.guests.setText(f"{guests} guest(s)")

        total=price*nights
        self.total.setText(f"💳 Total Amount: ${total}")

    def confirm(self):

        dialog = ConfirmDialog(self.customer)
        dialog.exec()

        self.stack.setCurrentIndex(0)
        self.stack.booking_page.clear_info()


# -------------------------
# MAIN WINDOW
# -------------------------
class MainWindow(QStackedWidget):

    def __init__(self):
        super().__init__()

        self.booking_page=BookingPage(self)
        self.review_page=ReviewPage(self)

        self.addWidget(self.booking_page)
        self.addWidget(self.review_page)

        self.setWindowTitle("CozyStay — Hotel Booking System")
        self.resize(950,620)


app=QApplication(sys.argv)

window=MainWindow()
window.show()

sys.exit(app.exec())