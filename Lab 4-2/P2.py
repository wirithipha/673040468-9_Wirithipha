# Name: Wirithipha Dungjan
# Student ID: 673040468-9

from cat import Cat

cat1 = Cat("Milo", 3, "British Shorthair", "Gray")
cat2 = Cat.from_birth_year("Luna", 2016, "Siamese", "White")

print(cat1.meow())
cat1.play(2)
cat1.eat(5)
cat1.sleep(3)

print(cat1.get_status())
print(cat2.get_status())

print("Species:", Cat.get_species_info())
print("Total cats:", Cat.total_cats)

print("Is Milo senior?", Cat.is_senior(cat1.age))
print("Food for 4kg cat:", Cat.calculate_healthy_food_amount(4))
