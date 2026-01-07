# Name: Wirithipha Dungjan
# Student ID: 673040468-9

from datetime import datetime, timedelta
from cat import Cat   # ชื่อไฟล์ต้องเป็น cat.py


cat1 = Cat("Milo", "British Shorthair", 2, "Alice")
cat2 = Cat("Luna", "Siamese", 3, "Bob")
cat3 = Cat("Kitty", "Persian", 1, "Chris")


print("First cat date_in:")
print(cat1.get_time_in())

print("First cat greets you:")
cat1.greet()

print("-" * 30)


print("Second cat date_out (before):")
print(cat2.get_time_out())


new_date_out = datetime.now() + timedelta(days=2)
cat2.set_time_out(new_date_out)

print("Second cat date_out (after +2 days):")
print(cat2.get_time_out())

print("-" * 30)


cat3.owner = "David"
cat3.age = 4

print("Third cat owner and age updated")

print("-" * 30)


cat1.print_cat()
cat2.print_cat()
cat3.print_cat()

print("-" * 30)


print("Total number of cats:")
print(Cat.get_num())


Cat.reset_cat()

print("Total number of cats after reset:")
print(Cat.get_num())
