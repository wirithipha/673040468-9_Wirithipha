# Name: Wirithipha Duangjan
# Student ID: 673040468-9

from Libraryitem import Book, TextBook, Magazine


book = Book("Harry Potter", "B001", "J.K. Rowling")
book.set_pages_count(300)
book.display_info()
book.check_out()
book.display_info()

print("----------")

tb = TextBook("Math", "T001", "John", "Math", 10)
tb.set_pages_count(450)
tb.display_info()

print("----------")

mag = Magazine("Time", "M001", 120)
mag.display_info()
mag.check_out()
mag.display_info()
