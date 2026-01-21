# Name: Wirithipha Duangjan
# Student ID: 673040468-9

from abc import ABC, abstractmethod


# Abstract Class: Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def get_info(self):
        return str(self.year) + " " + self.make + " " + self.model


# Superclass: CommercialVehicle
class CommercialVehicle:
    def __init__(self, license_number, max_load):
        self.license_number = license_number
        self.max_load = max_load
        self.current_load = 0

    def load_cargo(self, weight):
        if self.current_load + weight <= self.max_load:
            self.current_load += weight
            return True
        return False

    def unload_cargo(self, weight):
        if weight <= self.current_load:
            self.current_load -= weight
        else:
            self.current_load = 0
        return self.current_load


# Child Class: Car
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def start_engine(self):
        self.is_running = True
        print("Car engine started")

    def stop_engine(self):
        self.is_running = False
        print("Car engine stopped")


# Child Class: Trailer
class Trailer(CommercialVehicle):
    def __init__(self, license_number, max_load, num_axles=2):
        super().__init__(license_number, max_load)
        self.num_axles = num_axles

    def get_weight_per_axle(self):
        if self.num_axles == 0:
            return 0
        return self.current_load / self.num_axles


# Multiple Inheritance Class: DeliveryVan
class DeliveryVan(Car, CommercialVehicle):
    def __init__(self, make, model, year, num_doors,
                 license_number, max_load):
        Car.__init__(self, make, model, year, num_doors)
        CommercialVehicle.__init__(self, license_number, max_load)
        self.delivery_mode = False

    def toggle_delivery_mode(self):
        self.delivery_mode = not self.delivery_mode
        return "Delivery mode: " + str(self.delivery_mode)

    def begin_service(self):
        print(self.get_info())

        self.load_cargo(50)
        self.start_engine()
        print(self.toggle_delivery_mode())

        self.stop_engine()
        self.unload_cargo(50)
        print(self.toggle_delivery_mode())
