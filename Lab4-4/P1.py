# Name: Wirithipha Duangjan
# Student ID: 673040468-9

from room import Bedroom, Kitchen

bedroom = Bedroom(10, 12, 5)
kitchen1 = Kitchen(15, 10)
kitchen2 = Kitchen(15, 10, False)

print(bedroom.describe_room())
print("Bed size:", bedroom.bed_size)
print("Lighting:", bedroom.get_recommended_lighting())
print()

print(kitchen1.describe_room())
island, wall = kitchen1.calculate_counter_space()
print("Island:", island)
print("Wall:", wall)
print()

print(kitchen2.describe_room())
island, wall = kitchen2.calculate_counter_space()
print("Island:", island)
print("Wall:", wall)

print(Kitchen.calculate_counter_space.__doc__)