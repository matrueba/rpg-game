from characters.base_character import BaseCharacter


class Warrior(BaseCharacter):
    def __init__(self, name, character_data):
        super().__init__(name, character_data)
        self.rage = 0
        self.max_rage = 1000

    def apply_class_stats(self):
        self.attack += 200
        self.defense += 100
        self.special_attack -= 50
        self.special_defense -= 20
        self.actions.append(self.madness)

    def madness(self):
        hit_power = None
        if self.rage > 100:
            hit_power = self.attack * 2 + self.rage
            self.rage = 0
        return hit_power, "physical"
