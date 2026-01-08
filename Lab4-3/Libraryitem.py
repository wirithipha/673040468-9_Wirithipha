# Name: Wirithipha Duangjan
# Student ID: 673040468-9

from datetime import datetime


class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self._checked_out = False

    def get_status(self):
        if self._checked_out:
            return "Checked out"
        else:
            return "Available"

    def check_out(self):
        if self._checked_out == False:
            self._checked_out = True
            return True
        return False

    def return_item(self):
        if self._checked_out == True:
            self._checked_out = False
            return True
        return False

    def display_info(self):
        print("title:", self.title)
        print("Status:", self.get_status())


# Book
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        self.pages_count = 0

    def set_pages_count(self, pages):
        self.pages_count = pages

    def display_info(self):
        print("Pages:", self.pages_count)
        print("Status:", self.get_status())
        print("title:", self.title)
        print("Author:", self.author)


# TextBook
class TextBook(Book):
    def __init__(self, title, item_id, author, subject, grade_level):
        super().__init__(title, item_id, author)
        self.subject = subject
        self.grade_level = grade_level

    def display_info(self):
        print("page:", self.pages_count)
        print("subject:", self.subject)
        print("Grade:", self.grade_level)
        print("status:", self.get_status())



# Magazin
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

        now = datetime.now()
        self.month = now.month
        self.year = now.year

    def display_info(self):
        print("title:", self.title)
        print("Status:", self.get_status())
