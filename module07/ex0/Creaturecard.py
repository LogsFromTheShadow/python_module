from ex0.card import Card

class Creature_card(Card):
    def __init__(self, name: str, cost: int, rarity: str, type: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = type

    def play(self, game_state):
        creature_info = {"name": self.name,
                         "cost": self.cost,
                         "rarity": self.rarity,
                         "attack": self.attack,
                         "health": self.health}
        return creature_info

    def attack_target(self, target) -> dict:
        print(f"{self.name} attacks {target}")
        result = {"attacker": self.name,
                  "target": target,
                  "damage_dealt": self.attack,
                  "combat_resolved": True}
        print(f"Attack result: {result}")