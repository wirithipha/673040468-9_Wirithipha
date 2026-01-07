class Cat:
    # Class attributes
    species = "Felis catus"
    total_cats = 0
    average_lifespan = 15

    def __init__(self, name, age, breed, color):
        # Basic info
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

        # State
        self.hungry = False
        self.energy = 100
        self.happiness = 100

        Cat.total_cats += 1


    # Instance methods
    def meow(self):
        if self.hungry:
            return "Meow! I'm hungry"
        return "Meow~"

    def eat(self, food_amount):
        self.hungry = False
        self.energy = min(100, self.energy + food_amount)
        return "Eating..."

    def play(self, play_time):
        self.energy = max(0, self.energy - play_time * 10)
        self.happiness = min(100, self.happiness + play_time * 5)
        self.hungry = True
        return "Playing..."

    def sleep(self, hours):
        self.energy = min(100, self.energy + hours * 10)
        return "Sleeping..."

    def get_status(self):
        return {
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
            "color": self.color,
            "hungry": self.hungry,
            "energy": self.energy,
            "happiness": self.happiness
        }


    # Class methods
    @classmethod
    def from_birth_year(cls, name, birth_year, breed, color, current_year=2026):
        return cls(name, current_year - birth_year, breed, color)

    @classmethod
    def get_species_info(cls):
        return cls.species


    # Static methods
    @staticmethod
    def is_senior(age):
        return age > 7

    @staticmethod
    def calculate_healthy_food_amount(weight_kg):
        return weight_kg * 20
