class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage_taken: int):
        self.health -= damage_taken
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, heal_received: int):
        self.health += heal_received
