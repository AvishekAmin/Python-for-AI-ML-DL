# Concept: Multiple Inheritance

class Herbivore:
    def eat_plants(self):
        print("Eats plants.")

class Carnivore:
    def eat_meat(self):
        print("Eats meat.")

class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat.")

class Bear(Herbivore, Carnivore, Omnivore):
    def show(self):
        print("I am a bear and I inherit from all three classes.")

bear1 = Bear()

bear1.show()
bear1.eat_plants()
bear1.eat_meat()
bear1.eat_both()