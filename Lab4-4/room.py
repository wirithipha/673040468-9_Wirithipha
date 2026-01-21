# Name: Wirithipha Duangjan
# Student ID: 673040468-9

from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @abstractmethod
    def get_purpose(self):
        """Returns a string describing purposes of the room"""
        pass

    @abstractmethod
    def get_recommended_lighting(self):
        """Returns recommended lighting in lumens per square foot"""
        pass

    def calculate_area(self):
        return self.length * self.width

    def describe_room(self):
        return f"A {self.__class__.__name__} of {self.calculate_area()} sq ft used for {self.get_purpose()}"


class Bedroom(Room):
    def __init__(self, length, width, bed_size):
        super().__init__(length, width)
        self.bed_size = bed_size

    def get_purpose(self):
        return "sleeping"

    def get_recommended_lighting(self):
        return 10


class Kitchen(Room):
    def __init__(self, length, width, has_island=True):
        super().__init__(length, width)
        self.has_island = has_island

    def get_purpose(self):
        return "cooking"

    def get_recommended_lighting(self):
        return 40

    def calculate_counter_space(self):
        """
    Calculate counter space in the kitchen.

    If the kitchen has an island:
    - island counter = 1/5 of room area
    - wall counter = 1/4 of room area

    If the kitchen has no island:
    - island counter = 0
    - wall counter = 1/2 of room area

    Returns:
        island counter area, wall counter area
    """
        area = self.calculate_area()

        if self.has_island:
            island = area / 5
            wall = area / 4
        else:
            island = 0
            wall = area / 2

        return island, wall