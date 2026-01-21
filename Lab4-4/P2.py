# Name: Wirithipha Duangjan
# Student ID: 673040468-9

from vehicle import Car, Trailer, DeliveryVan


if __name__ == "__main__":
    print("=== Car Test ===")
    car = Car("Toyota", "Camry", 2020, 4)
    print(car.get_info())
    car.start_engine()
    car.stop_engine()

    print("\n=== Trailer Test ===")
    trailer = Trailer("AB-123", 1000)
    trailer.load_cargo(400)
    print("Weight per axle:", trailer.get_weight_per_axle())

    print("\n=== DeliveryVan Test ===")
    van = DeliveryVan("Ford", "Transit", 2022, 4, "DV-999", 500)
    van.begin_service()
