# Concept: Inheritance

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

car1 = Car("BMW", "X7", 4)
bike1 = Bike("Royal Enfield", "Super Meteor", 650)

print(f"Car: {car1.brand} Model: {car1.model} Seats: {car1.seats}")
print(f"Bike: {bike1.brand} Model: {bike1.model} Engine: {bike1.engine_cc} cc")