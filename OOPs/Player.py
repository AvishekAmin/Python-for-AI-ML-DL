# Concept: Instance & Class Attributes

class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    @classmethod
    def get_player_count(cls):
        return cls.player_count

p1 = Player("Avishek", 3)
p2 = Player("Rahul", 5)
p3 = Player("Amit", 2)

print(f"Total no of players: {p1.get_player_count()}")